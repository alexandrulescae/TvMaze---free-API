import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'https://api.tvmaze.com/shows'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(serviceurl, context = ctx)
data = uh.read().decode()
js = json.loads(data)

#http://json.parser.online.fr/ clear view of json sample

for x in js:
    for i in x['genres']:
        if i == 'Drama':
            print(x['name'])
    