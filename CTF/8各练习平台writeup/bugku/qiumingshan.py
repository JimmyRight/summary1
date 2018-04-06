#encoding='UTF-8'
import requests   
import json
import re

url = "http://120.24.86.145:8002/qiumingshan/"	
session= requests.Session()
res_g=session.get(url)
res_g.encoding='UTF-8'
#print res_g.text

expression = re.search(r'(\d+[+\-*])+(\d+)', res_g.text).group()
result = eval(expression)

post = {'value': result}
flag_p=session.post(url, data = post)
flag_p.encoding='UTF-8'
print flag_p.text
