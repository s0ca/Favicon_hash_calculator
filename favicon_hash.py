#!/usr/bin/env python3
#Calcule le hash des favicons, 
#utile pour de la recherche de fingerprint sur shodan

#python3 -m pip install mmh3
#usage :  ./favicon_hash.py https://website.xxx/favicon.ico

import sys
import mmh3
import requests
import codecs

response = requests.get(sys.argv[1])
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print("http.favicon.hash:" + str(hash))
print("https://www.shodan.io/search?query=" + str(hash))
