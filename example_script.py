"""
Example script for working with the neocities client library
"""

from neocities_client import neocities_client_lib

username = 'sampleuser'
pw = 'samplepassword'

# Get a client object with the user and pass - the object will keep track of
# the session automatically
client_object = neocities_client_lib.NeoClient(username, pw)

# Call login to authenticate before doing other operations
client_object.login()

# Calling new_page will upload the specified file from the current directory
# Remember if a file already exists by that name, it will be overwritten
client_object.new_page('example_file.html')

# This creates a zipfile of the name <username>.zip in the current directory. It contains your
# entire website as it appears on the neocities server
client_object.download_site()

