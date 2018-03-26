#coding:utf-8
import requests
import base64

url ='http://120.24.86.145:8002/web6/'

r =requests.session()

headers = r.get(url).headers
#flag = head['Flag'].split(':')[0]   注意response的键
#print flag

flag = base64.b64decode(base64.b64decode(headers['flag']).split(':')[1])
print flag