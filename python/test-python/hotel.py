# -*- coding: UTF-8 -*-
import re,os,sys,urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#http://hotel.elong.com/search/list_cn_1001.html?keywords=四星级
#http://hotel.elong.com/search/list_cn_1001.html?keywords=五星级
#http://hotel.elong.com/search/list_cn_1001.html?keywords=三星级
target_url=raw_input()
html = getHtml(target_url)
#print html
hotel_list=re.findall(r'target="_blank" title="(.*)?"><span class',html)
for name in hotel_list:
    print name
print len(hotel_list)


