#!/usr/bin/python
import requests
import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs='/etc/ssl/certs/novoxen1-selfsigned.crt')
url = 'https://novoxen1/dev/json_post_test.php'
myobj = {'parm1': 'value1'}

#x = requests.post(url, data = myobj, verify=False)
x = http.request('POST',url, fields=myobj)

print(x.data)
