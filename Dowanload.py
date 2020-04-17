import urllib.request
url = input('Enter file link > ')
File_name = str(input('input file name > '))
print('Downloading file')
with urllib.request.urlretrieve(url, File_name) as down :
    down()
    print('File {} downloaded'.format(File_name))