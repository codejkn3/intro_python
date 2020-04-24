#!/usr/bin/python
import requests

url = 'https://novoxen1/dev/json_post_test.php'
myobj = {'parm1': 'value1'}

x = requests.post(url, data = myobj, verify=False)

print(x.text)
