#encoding=UTF-8

import string

str='gndk{rlqhmtkwwp}z'
length=len(str)
#print length
#print str[16]

flag=''

for i in range(0,17):
	#print str[i]
	flag+=chr(ord(str[i])-i-1)
	
print flag
#flag{lei_ci_jiami}