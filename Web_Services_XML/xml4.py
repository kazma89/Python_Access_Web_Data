import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

counts = 0
sum = 0
link = input('Enter location: ')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = urllib.request.urlopen(link, context=ctx)
print('Retrieving', link)

data = url.read()
#print(data.decode())
stuff = ET.fromstring(data.decode())
nodes = stuff.findall('comments/comment')
for node in nodes :
    #print('Name', node.find('name').text)
    #print('Count', node.find('count').text)
    counts = counts + 1
    sum = sum + int(node.find('count').text)
print('Count:',counts)
print('Sum:',sum)
