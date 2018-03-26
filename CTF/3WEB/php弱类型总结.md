#知识介绍
---
php中有两种比较的符号 == 与 ===

	<?php
	$a = $b ;
	$a===$b ;
	?>

=== 在进行比较的时候，会先判断两种字符串的类型是否相等，再比较

== 在进行比较的时候，会先将字符串类型转化成相同，再比较

如果比较一个数字和字符串或者比较涉及到数字内容的字符串，则字符串会被转换成数值并且比较按照数值来进行

	<?php
	var_dump("admin"==0);  //true
	var_dump("1admin"==1); //true
	var_dump("admin1"==1) //false
	var_dump("admin1"==0) //true
	var_dump("0e123456"=="0e4456789"); //true 
	?>  //上述代码可自行测试

三个角度
	
	1. "admin"==0 比较的时候，会将admin转化成数值，强制转化,由于admin是字符串，转化的结果是0自然和0相等
	2. "1admin"==1 比较的时候会将1admin转化成数值,结果为1，而“admin1“==1 却等于错误，也就是"admin1"被转化成了0,为什么呢？？
	3. "0e123456"=="0e456789"相互比较的时候，会将0e这类字符串识别为科学技术法的数字，0的无论多少次方都是零，所以相等
	4. 与数组比较,置零

	$param = 1;
	$param = array();
	$param = "stringg";

php手册解释

	当一个字符串欸当作一个数值来取值，其结果和类型如下:如果该字符串没有包含'.','e','E'并且其数值值在整形的范围之内
	该字符串被当作int来取值，其他所有情况下都被作为float来取值，该字符串的开始部分决定了它的值，如果该字符串以合法的数值开始，则使用该数值，否则其值为0。

	<?php
	$test=1 + "10.5"; // $test=11.5(float)
	$test=1+"-1.3e3"; //$test=-1299(float)
	$test=1+"bob-1.3e3";//$test=1(int)
	$test=1+"2admin";//$test=3(int)
	$test=1+"admin2";//$test=1(int)
	?>

	所以就解释了"admin1"==1 =>False 的原因

#实例
---
##md5绕过(Hash比较缺陷)//
'0e'=='0e'
	<?php
	if (isset($_GET['Username']) && isset($_GET['password'])) {
	    $logined = true;
	    $Username = $_GET['Username'];
	    $password = $_GET['password'];
	
	     if (!ctype_alpha($Username)) {$logined = false;}
	     if (!is_numeric($password) ) {$logined = false;}
	     if (md5($Username) != md5($password)) {$logined = false;}
	     if ($logined){
	    echo "successful";
	      }else{
	           echo "login failed!";
	        }
	    }
	?>
	
	
	题目大意是要输入一个字符串和数字类型，并且他们的md5值相等，就可以成功执行下一步语句 
	
	介绍一批md5开头是0e的字符串 上文提到过，0e在比较的时候会将其视作为科学计数法，所以无论0e后面是什么，0的多少次方还是0。md5('240610708') == md5('QNKCDZO')成功绕过!
	
		QNKCDZO
		0e830400451993494058024219903391
		
		s878926199a
		0e545993274517709034328855841020
		  
		s155964671a
		0e342768416822451524974117254469
		  
		s214587387a
		0e848240448830537924465865611904
		  
		s214587387a
		0e848240448830537924465865611904
		  
		s878926199a
		0e545993274517709034328855841020
		  
		s1091221200a
		0e940624217856561557816327384675
		  
		s1885207154a
		0e509367213418206700842008763514
##MD5()无法处理传入的数组
md5()对传进来的array无能为力，函数接受到了不符合的类型，将发生错误，函数返回值为FALSE，false==false,从而判断其相等(===也成立)

##SHA1()无法处理传入的数组
md5()对传进来的array无能为力，函数接受到了不符合的类型，将发生错误，函数返回值为FALSE，false==false,从而判断其相等(===也成立)

##json绕过
0=="admin"
	<?php
	if (isset($_POST['message'])) {
	    $message = json_decode($_POST['message']);
	    $key ="*********";
	    if ($message->key == $key) {
	        echo "flag";
	    } 
	    else {
	        echo "fail";
	    }
	 }
	 else{
	     echo "~~~~";
	 }
	?>
	
	输入一个json类型的字符串，json_decode函数解密成一个数组，判断数组中key的值是否等于 $key的值，但是$key的值我们不知道，但是可以利用0=="admin"这种形式绕过
	
	最终payload message={"key":0}

##array_search in_array绕过
0=="admin"
1=="1admin"
	<?php
	if(!is_array($_GET['test'])){exit();}
	$test=$_GET['test'];
	for($i=0;$i<count($test);$i++){
	    if($test[$i]==="admin"){
	        echo "error";
	        exit();
	    }
	    $test[$i]=intval($test[$i]);
	}
	if(array_search("admin",$test)===0){
	    echo "flag";
	}
	else{
	    echo "false";
	}
	?>
	
	上面是自己写的一个，先判断传入的是不是数组，然后循环遍历数组中的每个值，并且数组中的每个值不能和admin相等，并且将每个值转化为int类型，再判断传入的数组是否有admin，有则返回flag
	
	payload test[]=0可以绕过
	
	下面是官方手册对array_search的介绍
	
	mixed array_search ( mixed $needle , array $haystack [, bool $strict = false ] )
	
	$needle，$haystack必需，$strict可选  函数判断$haystack中的值是存在$needle，存在则返回该值的键值 第三个参数默认为false，如果设置为true则会进行严格过滤
	
	<?php
	$a=array(0,1);
	var_dump(array_search("admin",$a)); // int(0) => 返回键值0
	var_dump(array_seach("1admin",$a));  // int(1) ==>返回键值1
	?>
	
	array_search函数 类似于== 也就是$a=="admin" 当然是$a=0  当然如果第三个参数为true则就不能绕过

##strcmp漏洞绕过 php -v <5.3
password[]=xxx	
	<?php
	    $password="***************"
	     if(isset($_POST['password'])){
	
	        if (strcmp($_POST['password'], $password) == 0) {
	            echo "Right!!!login success";n
	            exit();
	        } else {
	            echo "Wrong password..";
	        }
	?>
	

	
	strcmp是比较两个字符串，如果str1<str2 则返回<0 如果str1大于str2返回>0 如果两者相等 返回0
	
	我们是不知道$password的值的，题目要求strcmp判断的接受的值和$password必需相等，strcmp传入的期望类型是字符串类型，如果传入的是个数组会怎么样呢
	
	我们传入 password[]=xxx 可以绕过 是因为函数接受到了不符合的类型，将发生错误，但是还是判断其相等
	
	payload: password[]=xxx

##switch绕过
4="4admin"
	<?php
	$a="4admin";
	switch ($a) {
	    case 1:
	        echo "fail1";
	        break;
	    case 2:
	        echo "fail2";
	        break;
	    case 3:
	        echo "fail3";
	        break;
	    case 4:
	        echo "sucess";  //结果输出success;
	        break;
	    default:
	        echo "failall";
	        break;
	}
	?>

#参考链接
<http://blog.csdn.net/hitwangpeng/article/details/45972099>