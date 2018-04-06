# -*- coding: UTF-8 -*-

'''
题目：暂停n秒输出。

程序分析：使用 time 模块的 sleep() 函数。
'''

import time

n=int(raw_input('you wanna sleep how long:\n'))
time.sleep(n)
print 'you sleep %d seconds\n' % n

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print key, value
    time.sleep(1) # 暂停 1 秒
