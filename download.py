import urllib
print('Downloading file')
#x = input('Enter Download Link > ')
x = input('Enter file link > ')
c = str(input('input file name > '))
urllib.urlretrieve(x,str(c))
print('File Downloaded')
