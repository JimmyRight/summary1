#encoding:utf8

import base64

fo = open("base64.txt", "r")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
print '\r\n'

str0 = fo.read()
count=0
print str0
print 'decode '+str(count)+' times'+'\r\n'
stri=str0

while (stri!=0):
    miss_pad = 4 - len(stri) % 4
    if miss_pad:
        stri += b'='* miss_pad
    stri=base64.b64decode(stri)
    if (stri==0):
        break
    print stri
    count += 1
    print 'decode ' + str(count) + ' times'+'\r\n'

fo.close()