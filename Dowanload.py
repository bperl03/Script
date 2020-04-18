#!/usr/bin/python3
# Download script
import urllib.request
url = input('Enter file link > ') # the file Url
File_name = str(input('input file name > ')) #file name to save it with new name
print('Downloading file')
with urllib.request.urlretrieve(url, File_name) as down :
    down()
    print('File {} downloaded'.format(File_name))