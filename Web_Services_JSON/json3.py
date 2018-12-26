import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = ''
while True:
    address = input('Enter the location: ')
    if len(address) < 1 : break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieve', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try :
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('====== Failure To Retrieve ======')
        print(data)
        continue
        print(json.dumps(js, indent=4))

    lst = js["results"][0]["geometry"]["location"]["lat"]
    lst = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
