import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_161411.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')

count = 0
sum = 0
for tag in tags :
    #print(tag.get('href', None))
     #print (tag.contents[0])
     number = int(tag.contents[0])
     count = count + 1
     sum = sum + number
print('Count', count)
print('Sum', sum)
