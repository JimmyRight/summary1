#知识介绍
#实例
一.全局变量覆盖
当register_global=ON时，变量来源可能是各个不同的地方，比如页面的表单，Cookie等。

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

通过$GLOBALS获取的变量，也可能导致变量覆盖。

	<?php
	echo "Register_globals:".(int)ini_get("register_globals")."<br/>";
	if (ini_get('register_globals')) foreach($_REQUEST as $k=>$v) unset(${$k});
	print $a;
	print $_GET[b];
	?>
变量$a未初始化，在register_globals=ON时，再尝试控制“$a”的值（http://www.a.com/test1.php?a=1&b=2），会因为这段代码而出错。
而当尝试注入“GLOBALS[a]”以覆盖全局变量时（http://www.a.com/test1.php?GLOBALS[a]=1&b=2），则可以成功控制变量“$a”的值。这是因为unset()默认只会销毁局部变量，要销毁全局变量必须使用$GLOBALS。
而在register_globals=OFF时，则无法覆盖到全局变量。
小记：register_globals的意思是注册为全局变量，所以当On的时候，传递过来的值会被直接注册为全局变量而直接使用，当为OFF的时候，就需要到特定的数组中去得到它。unset用于释放给定的变量

	PHP的超级全局变量，全是数组。
	$GLOBALS, 所有全局变量数组
	$_SERVER， 服务器环境变量数组
	$_GET，通过GET方法传递给脚本的变量数组
	$_POST， 通过POST方法传递给脚本的变量数组
	$_COOKIE，cookie变量数组
	$_REQUEST，所有用户输入的变量数组，包括$_GET, $_POST和$_COOKIE所包含的输入内容
	$_FILES，与文件上传相关得变量数组
	$_ENV，环境变量数组
	$_SESSION，会话变量数组

二、extract()变量覆盖
extract() 函数从数组中将变量导入到当前的符号表。
该函数使用数组键名作为变量名，使用数组键值作为变量值。针对数组中的每个元素，将在当前符号表中创建对应的一个变量。

	<?php
	
	$auth = '0';
	extract($_GET)；
	
	if($auth==1){
	echo "private!";
	}else{
	echo "public!";
	}
	?>

假设用户构造以下链接：<http://www.a.com/test1.php?auth=1>界面上会打印出private！

当extract的第二个参数变为：EXTR_SKIP，即：extract($a,EXTR_SKIP);就可以不覆盖变量的值了
当extract的第二个参数为EXTR_REFS，变量也会被覆盖

三、遍历初始化变量

常见的一些以遍历的方式释放变量的代码，可能会导致变量覆盖。

	<?
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

四、import_request_variables变量覆盖
import_request_variables 函数可以在 register_global = off 时，把 GET/POST/Cookie 变量导入全局作用域中。
将 GET/POST/Cookie 变量导入到全局作用域中。如果你禁止了 register_globals，但又想用到一些全局变量，那么此函数就很有用。
Ps:这个只用于：php4.1到5.4之间

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

五、parse_str()变量覆盖
parse_str() 函数把查询字符串解析到变量中。
注释：如果未设置 array 参数，则由该函数设置的变量将覆盖已存在的同名变量。

	//var.php?var=new
	$var='init';
	parse_str($_SERVER['QUERY_STRING']);
	print $var;

与parse_str()类似的函数还有mb_parse_str()

小记：parse_str — 将字符串解析成多个变量，如果参数str是URL传递入的查询字符串（query string），则将它解析为变量并设置到当前作用域。	

六、$$变量覆盖(&$a)
PHP 的引用允许你用两个变量来指向同一个内容,其实本质上是变量的间接寻址

	$a="ABC"; 
	$b =&$a; 
	echo $a;//这里输出:ABC 
	echo $b;//这里输出:ABC 
	$b="EFG"; 
	echo $a;//这里$a的值变为EFG 所以输出EFG echo $b;//这里输出EFG

	$a=1;
	foreach (array('_COOKIE','_POST','_GET') as $_request)
	{
	    foreach ($$_request as $_key=>$_value)
	    {
	        echo $_key;
	        
	        $$_key=  addslashes($_value);
	        echo "<br>";
	    }
	}
	echo $a;
	
	当浏览器传递访问：http://localhost:8000/fugai.php?a=555
	输出的的值为555
	
	为什么会导致变量覆盖呢？重点在$$符号，从代码中我们可以看出$_key为COOKIE，POST，GET中的参数，比如提交?a=1，则$key的值为a，而还有一个$在a的前面，结合起来则是$a=addslashes($_values);所以这样会覆盖已有的变量$a的值

#参考链接
<http://blog.csdn.net/hitwangpeng/article/details/45972099>
<http://blog.163.com/blackhair_black/blog/static/262395060201732992652845/>
