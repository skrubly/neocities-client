"""
Example script for working with the neocities client library
"""

import neocities_client_lib

username = 'sampleuser'
pw = 'samplepassword'

client_object = neocities_client_lib.NeoClient(username, pw)
client_object.login()
client_object.new_page('example_file.html')
