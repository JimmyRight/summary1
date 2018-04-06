#encoding=UTF-8

import base64

str='e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA'

#list=[]
s=''
for c in str:
	#print c
	#print( c + " 的ASCII 码为", ord(c))
	#print( a , " 对应的字符为", chr(a))
	s+=chr(ord(c)-4)
	#list.append(s)
	
#print list
print s
key=base64.b64decode(s)
print key