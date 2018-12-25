import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count_links = 1

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
counts = int(count) - 1
position = input('Enter position: ')
positions = int(position)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
link = tags[counts].get('href',None)
print('Retrieving',url)
print('Retrieving',link)
while count_links < positions :
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[counts].get('href',None)
    print('Retrieving',link)
    count_links = count_links + 1
