"""
Python client library for neocities.org websites
"""

import re
import requests
import sys
from bs4 import BeautifulSoup

SITE_FILES = "http://neocities.org/site_files/"
SIGNIN_PAGE = "http://neocities.org/signin"
NEW_PAGE = SITE_FILES + "new"
UPLOAD_ENDPOINT = SITE_FILES + "upload"
DASHBOARD = "http://neocities.org/dashboard"


class NeoClient(object):
  """
  Neocities client object
  """
  def __init__(self, user, pw):
    self.user = user
    self.pw = pw
    self.client = requests.Session()

  def _get_csrf(self, URL):
    """
    Request a page and return csrf token
    """
    page = self.client.get(URL)
    soup = BeautifulSoup(page.text)
    attribs = {'name': 'csrf-token'}
    csrf_tag = soup.find_all(attrs=attribs)[0]
    csrftoken = csrf_tag.attrs['content']
    return csrftoken

  def new_page(self, filename):
    """
    Upload a new page. If the name already exists on the server, it will be overwritten
    Args: filename, str
    Returns: requests object
    """
    token = self._get_csrf(NEW_PAGE)
    files = {'newfile': open(filename, 'rb')}
    page_data = dict(csrf_token=token, newfile=filename)
    headers = {'X-CSRF-Token': token, 'Referer': NEW_PAGE}
    r = self.client.post(UPLOAD_ENDPOINT, data=page_data, files=files, headers=headers)
    return r

  def login(self):
    """
    Authenticate to Neocities.org using the user and pw on the object
    Returns: requests object
    """
    token = self._get_csrf(SIGNIN_PAGE)
    login_data = dict(username=self.user,
                      password=self.pw,
                      csrf_token=token)
    r = self.client.post(SIGNIN_PAGE, data=login_data, headers=dict(Referer=SIGNIN_PAGE))
    return r

  def download_site(self):
    """
    Download the entire website as a zip file
    Returns: requests object, writes file to directory script is run from
    """
    r = self.client.get(SITE_FILES + self.user + ".zip")
    with open(self.user + ".zip", "wb") as savefile:
      savefile.write(r.content)
    return r

  def dashboard(self):
    """
    Downloads the dashboard page. Access r.content for the HTML.
    """
    token = self._get_csrf(DASHBOARD)
    r = self.client.get(DASHBOARD, headers=dict(Referer=SIGNIN_PAGE))
    return r

