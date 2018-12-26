import urllib.request, urllib.parse, urllib.error
import json

count = 0
sum = 0
url = input('Enter location: ')
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
print(json.dumps(js, indent=4))
print('==================================')
for item in js["comments"] :
    count = count + 1
    sum = sum + int(item["count"])
print('Count:', count)
print('Sum:', sum)
