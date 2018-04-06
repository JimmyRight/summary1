#encoding=UTF-8

import requests
import base64
import json
import re

url='http://120.24.86.145:8002/web6/'
s=requests.Session()
g=s.get(url)
#print g.text
#print g.headers
h=g.headers

#flag = h['flag'].split(':')[0]
#print flag+'\r\n'
#flag1 = h['flag'].split(':')[1]
#print flag1+'\r\n'

margin = base64.b64decode(base64.b64decode(h['flag']).split(':')[1])
print margin

data={
	'margin':margin
}


p=s.post(url,data=data)
print p.text


#提交答案
url1='http://ctf.bugku.com/chal/29'
header1={
	'Host': 'ctf.bugku.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
	'Accept': '*/*',
	'Accept-Language': 'zh-CN,en-US;q=0.5',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'X-Requested-With': 'XMLHttpRequest',
	'Referer': 'http://ctf.bugku.com/challenges',
	'Content-Length': '140'
}
data1={
	'key':p.text,
	'nonce':'5a65a81ff7205fb795076502f0045c59b4d335242636ab03128887ee5b03d7813f28852dc93823293fb0ad7cbda11dc5f7cb97cb9e623a24fefc733268ec9812'
}
cookie={
'session':'.eJwVj8uKg0AQRX9lqLUbHzMLIQuhRXqgKgQ6I107o8bY2gZGgrFC_n16FndxzuLAfUHT-XGB_NrMax_B2EGexl9ZBMt9aXvIX_BxgRyoLpOwDGv2JHqjmkeSKUbVJmSKnV2xkfpxZOaRqpOgnHdSOkHhm3WFoNHZUQ0p1-f4n1m1GRry6IaMzPdkZZKj0oJuEvZ6s_UptUnwpnxyhTG7zlk3Bac_2dgdk3Knimf2mKLgTu42h0Zo6gO8I3is_e_S-HAALo_hvsL7D8QBTXU.DX5xpw.kgg2Au7qcQHBFvfVnXh989RVY8M'
}
p1=s.post(url1,data=data1,headers=header1,cookies=cookie)
print p1.text





'''
header=g.headers
data={'flag':'6LeR55qE6L+Y5LiN6ZSZ77yM57uZ5L2gZmxhZ+WQpzogTWpVeU1UZzI='}
p=s.post(url,data=data,headers=header)
print p.headers
print p.text
'''
