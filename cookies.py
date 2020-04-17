#!/usr/bin/python3

"""This script to read cookies """
import urllib.request
host = str(input('Input the link '))
with urllib.request.urlopen(host) as response:
    cookies = response.info()['Set-Cookie']
    content = response.read()
    response.close()
    print(cookies, content)