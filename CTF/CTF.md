# CTF 入门指南

此笔记内容来源于i春秋上的公开课，讲师幻泉。
视频链接：http://www.ichunqiu.com/section/53909

## 赛棍之路

### 常规做法

A方向：PWN + Reverse + Crypto 随机搭配

B方向：Web + Misc 组合

### 学习内容

都要学的内容：Linux 基础，计算机组成原理，操作系统原理，网络协议分析

A 方向：IDA 工具使用（F5插件），逆向工程，密码学，缓冲区溢出等

B 方向：网络安全，内网渗透，数据库安全等

### 书单

A 方向：

- RE for Beginners
- IDA Pro 权威指南
- 揭秘家庭路由器 0day 漏洞挖掘技术
- 自己动手写操作系统
- 黑客攻防技术宝典：系统实战篇

B 方向：

- Web 应用安全权威指南
- Web 前端黑客技术揭秘
- 黑客秘笈 渗透测试实用指南
- 黑客攻防技术宝典：Web 实战篇
- 代码审计：企业级 Web 代码安全架构

### 基本的题库

- [IDF 实验室 CTF 训练营](http://ctf.idf.cn/)
- [i春秋在线挑战](http://www.ichunqiu.com/tiaozhans)
- [XCTF_OJ练习平台](http://oj.xctf.org.cn/)

### 推荐资源

- [Wechall 题库](http://www.wechall.net/challs)
- [移动安全方面](http://canyouhack.it/)

**A 方向**

- https://microcorruption.com/login
- http://smashthestack.org/
- http://overthewire.org/wargames/
- https://exploit-exercises.com/
- http://pwnable.kr/play.php

**B 方向**

- http://ctf.moonsos.com/pentest/index.php
- http://prompt.ml/0
- http://redtiger.labs.overthewire.org/


## 工具

- burp, IDA
- https://github.com/truongkma/ctf-tools
- https://github.com/zardus/ctf-tools
- https://github.com/P1kachu/v0lt
- https://github.com/TUCTF/Tools

## 后话
- [转载来自Cathon的github](https://github.com/Cathon/ThingsofCTF/blob/master/CTF%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97-2016-06-28.md)

一、CTF简介
CTF比赛通常包含的题目类型包括MISC、PPC、CRYPTO、PWN、REVERSE、WEB、STEGA

二、MISC
 MISC(Miscellaneous)类型，即安全杂项，题目或涉及流量分析、电子取证、人肉搜索、数据分析等等。
    
三、PWN
 PWN类型，PWN在黑客俚语中代表着攻破、取得权限，多为溢出类题目。
 
四、WEB
WEB类型，即题目会涉及到常见的Web漏洞，诸如注入、XSS、文件包含、代码执行、命令执行等漏洞。
常见套路
php弱类型
=== 在进行比较的时候，会先判断两种字符串的类型是否相等，再比较

== 在进行比较的时候，会先将字符串类型转化成相同，再比较
	数字与字符串比较
		var_dump( 0 == "a" );   //true
		var_dump( "0" == "a" );//false
		var_dump("admin"==0);  //true
		var_dump("1admin"==1); //true
		var_dump("admin1"==1) //false
		var_dump("admin1"==0) //true
		var_dump("0e123456"=="0e4456789"); //true 		
		第一个返回的是 true ，第二个返回的是 false
		因为php把字母开头的转化为整型时，转化为0， 前面数字后面字母的话就只取到第一个字母出现的位置之前（如intval(''123abd45gf)结果为123）
	var_dump( 0 == 0.1 );  true
	
php反序列化
	pass=&sercet=
	pop链
urlencode
	00截断
	二次加密%25
ereg
	大小写
	%00
	当ntf为数组时它的返回值不是FALSE
preg_match
strpos
strcmp($pass,$pass1)
	strcmp(array,string) ==
		pass[]=1
	
文件包含
文件备份
	.bak   ultroedit....

	~

	.xxxx.php.swp  .xxxx.php.swo    vim
MD5碰撞
	0e
		
	==
		md5('240610708') 的结果是：0e462097431906509019562988736854   
		md5('QNKCDZO') 的结果是：0e830400451993494058024219903391  
		240610708、QNKCDZO、aabg7XSs、aabC9RqS
	数组、对象
		md5(array) == NULL
变量覆盖
命令执行
文件上传

0.常用爆破，其中就有MD5，验证码识别，爆破随机数。

  1.绕WAF，花式绕Mysql，绕文件读取关键字检测之类的拦截。

  2.几个常见的php特性，其中就有弱类型，反序列化+destruct，\0截断，iconv截断。（最近在学php，等熟练一波后，再补一篇）

  3.密码题中就包括hash长度扩展，异或，移位加密的变形，32位随机数过小，随机数种子可预测。

  4.各种找源码的技巧，git，svn，xxx，php.swp，*www*...（zip|tar.gz|rar|7z），xxx.php.bak。

  5.文件上传，其中就有文件的后缀，php345.inc.phtml.phpt.phps，各种文件内容检测<?php<?<%<script language=php>,花式解析漏洞。

  6.Mysql类型差异，包括和php弱类型类似的特性，0x，0b，0e之类，varchar和integar相互转换，非strict模式截断等。

  7.open_basedir，diable_functions花式绕过技巧，包括dl，mail，imagick，bash漏洞，Directorylterator及各种二进制选手插足的方法。

  8.条件竞争，包括竞争删除前生成shell，竞争数据库无锁多扣线。

  9.社工，花式查社工库，微博，qq签名，whois。

  10.windows特性，包括短文件名，IIS解析漏洞，NTFs文件系统通配符，::$DATA,冒号截断。

  11.SSRF，花式探测端口，302跳转，花式协议利用，gophar直接取shell等。

  12.xss，各种浏览器auditor绕过，富文本过滤黑白名单绕过，flash xss，CSP绕过。

  13.XXE，各种XML存在地方（rss/word/流媒体），各种XEE利用方法（SSRF，文件读取）。

  14.协议，花式IP伪造X-Forwarded-For/X-Client-IP/X-Real-IP/CDN-Src-IP,花式改UA，花式藏FLAG，花式分析数据包

五、PPC
PPC(Professionally Program Coder)类型，即编程类题目，题目涉及到编程算法，相比ACM较为容易。

六、CRYPTO
CRYPTO(Cryptography)类型，即密码学，题目考察各种加解密技术，包括古典加密技术、现代加密技术甚至出题者自创加密技术。
1.编码base64、URL编码、Unicode编码、进制编码、编码函数
2.凯撒密码、维吉尼亚密码、古典密码、弱密码、猪圈密码、栅栏密码、摩斯码、希尔密码、手机密码
维热纳尔方阵、比尔密码、波雷费密码、轮盘密码
3.MD5码、hash码、RSA、wpa
4.js编码：aaencoder、Unicode编码、Jother编码、base64编码、进制编码






七、REVERSE
REVERSE类型，即逆向工程，题目涉及到软件逆向、破解技术。

八、STEGA
STEGA(Steganography)类型，即隐写术，题目的Flag会隐藏到图片、音频、视频等各类数据载体中供参赛者获取。
1.图种
图片内隐藏文件rar/txt/zip/jpg
copy /b 2.jpg+1.zip output.jpg 
正常的jpg结尾都是FF D9的，图片查看器会忽视jpg结束符之后的内容
winhex打开查看二进制数据
binwalk 1.jpg


2.LSB隐写
LSB也就是最低有效位 (Least Significant Bit)。
原理就是图片中的像数一般是由三种颜色组成，即三原色，由这三种原色可以组成其他各种颜色，例如在PNG图片的储存中，每个颜色会有8bit，LSB隐写就是修改了像数中的最低的1bit，在人眼看来是看不出来区别的，也把信息隐藏起来了。
譬如我们想把’A’隐藏进来的话，就可以把A转成16进制的0x61再转成二进制的01100001，再修改为红色通道的最低位为这些二进制串
工具：Stegsolve
Stegsolve——Analyse——Frame Browser
Stegsolve——Analyse——Data Extract
信息载体是PNG、BMP格式的文件


3.二维码解码
http://tool.chinaz.com/qrcode/


4.gif文件
gif文件头格式说明：http://dev.gameres.com/Program/Visual/Other/GIFDoc.htm
gif是动态图，它是可以由多帧组成的可以顺序播放的
Namo_GIF_gr
Stegsolve——Analyse——Frame Brower


5.jpg文件
jpg图片还可以把信息隐藏的exif的部分。exif的信息是jpg的头部插入了数码照片的信息
Power_exif或maigicexif


6.png文件
pngcheck.exe -v sctf.png
前面的4字节是长度，然后是标志位IDAT4字节，然后开始是数据，直到 D9 CF A5 A8是crc32校验位


7.双图
dd if=infile of=outfile bs=512 count=1 skip=1024
dd   [option]
dd指令选项详解
if=file：输入文件名，缺省为标准输入
of=file：输出文件名，缺省为标准输出
ibs=bytes：一次读入 bytes 个字节（即一个块大小为 bytes 个字节）
obs=bytes：一次写 bytes 个字节（即一个块大小为 bytes 个字节）
bs=bytes：同时设置读写块的大小为 bytes ，可代替 ibs 和 obs
cbs=bytes：一次转换 bytes 个字节，即转换缓冲区大小
skip=blocks：从输入文件开头跳过 blocks 个块后再开始复制
seek=blocks：从输出文件开头跳过 blocks 个块后再开始复制。（通常只有当输出文件是磁盘或磁带时才有效）
count=blocks：仅拷贝 blocks 个块，块大小等于 ibs 指定的字节数
conv=ASCII：把EBCDIC码转换为ASCIl码。
conv=ebcdic：把ASCIl码转换为EBCDIC码。
conv=ibm：把ASCIl码转换为alternate EBCDIC码。
conv=block：把变动位转换成固定字符。
conv=ublock：把固定位转换成变动位。
conv=ucase：把字母由小写转换为大写。
conv=lcase：把字母由大写转换为小写。
conv=notrunc：不截短输出文件。
conv=swab：交换每一对输入字节。
conv=noerror：出错时不停止处理。
conv=sync：把每个输入记录的大小都调到ibs的大小（用NUL填充）。 

8.zip文件
明文攻击
伪加密
暴力破解
社工字典

9.搜索引擎图片识别

10.流量分析


11.binwalk二次提取，将二进制数据写入zip文件
binwalk a.jpg

