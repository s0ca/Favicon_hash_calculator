#!/usr/bin/env python3
#Author: Mathias "s0ca"
#Calculate the hash of the favicons,
#useful for fingerprint search on shodan 

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
