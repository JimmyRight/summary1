#encoding=utf-8

import string
import re

#破译数据
secret='HCBTSXWCRQGLES'
#print secret
num=[2,5,1,3,6,4,9,7,8,14,10,13,11,12]
#print num

####轮盘字典预处理
wheel=[]
def pre_getwheel():
	wheel0=['1： <ZWAXJGDLUBVIQHKYPNTCRMOSFE <',
			'2： <KPBELNACZDTRXMJQOYHGVSFUWI <',
			'3： <BDMAIZVRNSJUWFHTEQGYXPLOCK <',
			'4： <RPLNDVHGFCUKTEBSXQYIZMJWAO <',
			'5： <IHFRLABEUOTSGJVDKCPMNZQWXY <',
			'6： <AMKGHIWPNYCJBFZDRUSLOQXVET <',
			'7： <GWTHSPYBXIZULVKMRAFDCEONJQ <',
			'8： <NOZUTWDCVRJLXKISEFAPMYGHBQ <',
			'9： <QWATDSRFHENYVUBMCOIKZGJXPL <',
			'10： <WABMCXPLTDSRJQZGOIKFHENYVU <',
			'11： <XPLTDAOIKFZGHENYSRUBMCQWVJ <',
			'12： <TDSWAYXPLVUBOIKZGJRFHENMCQ <',
			'13： <BMCSRFHLTDENQWAOXPYVUIKZGJ <',
			'14： <XPHKZGJTDSENYVUBMLAOIRFCQW <',
			]
	
	for line in wheel0:
		#print line
		line=re.search(r'<(.*)<',line.strip()).group(1)
		#print re.search(r'<(.*)<',line.strip()).group(1)
		wheel.append(line.strip())
	#print wheel

####轮盘按行旋转
list=[]
def get_key():
	for i in range(len(secret)):
		c=secret[i]
		#print i
		#print c
		k=num[i]-1
		str=wheel[k]
		str=c+str.split(c)[1]+str.split(c)[0]
		#print str
		list.append(str)
		#print len(str)
		
###输出轮盘结果
flag=''
def print_wheel():
	for i in range(26):
		str=''
		for line in list:
			str+=line[i]
		print str
		if 'BUGKU' in str:
			print 'the falg is: flag{'+str.lower()+'}'
			break


pre_getwheel()
get_key()
print_wheel()
#flag:flag{XSXSBUGKUADMIN}