# -*- coding: UTF-8 -*- 

import requests   
import Cookie
import json

list = []          ## 空列表
with open("mutou.txt") as fo:
    for line in fo:
        #print(line.strip()) # 把末尾的'\n'删掉
		list.append('KEY{'+line.strip()+'}')
#print list		

def ver_key( key ):
	url = "http://ctf.bugku.com/chal/51"
	UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"
	 
	header={
				'Host':'ctf.bugku.com',
				'Accept': '*/*',
				'Accept-Language': 'zh-CN,en-US;q=0.5',
				'Content-Type': 'application/x-www-form-urlencoded', 
				'charset':'UTF-8',
				'X-Requested-With': 'XMLHttpRequest',
				'Referer': 'http://ctf.bugku.com/challenges',
				'Content-Length': '158'
			}

	#cookie = Cookie.SimpleCookie()
	cookie ={'session':'.eJwVj8uKg0AQRX9lqLUbHzMLIQuhRXqgKgQ6I107o8bY2gZGgrFC_n16FndxzuLAfUHT-XGB_NrMax_B2EGexl9ZBMt9aXvIX_BxgRyoLpOwDGv2JHqjmkeSKUbVJmSKnV2xkfpxZOaRqpOgnHdSOkHhm3WFoNHZUQ0p1-f4n1m1GRry6IaMzPdkZZKj0oJuEvZ6s_UptUnwpnxyhTG7zlk3Bac_2dgdk3Knimf2mKLgTu42h0Zo6gO8I3is_e_S-HAALo_hvsL7D8QBTXU.DX5xpw.kgg2Au7qcQHBFvfVnXh989RVY8M'}

	postdata = {
				'key':key,
				'nonce':'5a65a81ff7205fb795076502f0045c59b4d335242636ab03128887ee5b03d7813f28852dc93823293fb0ad7cbda11dc5f7cb97cb9e623a24fefc733268ec9812'
				}

	req_session=requests.Session()		
	res=req_session.post(url,data = postdata,headers = header,cookies=cookie)
	#print cookie

	print key+'\r\n'
	#print res.text
	
	json1=res.json()
	#dic=json1.dumps()
	#print json1['message']
	return json1
	
	
#resp=ver_key( 'KEY{zs19970315}' )	
#print resp['message']


for i in list:
	resp=ver_key(i)
	if (resp['message']=='Correct' or resp['message']=='You already solved this'):
		print i+' is correct!'
		break
