﻿#技能要求
laravel
redis
百万级别数据表的联合索引
swoole，长短链接socket通信协议
Nginx，fast-cgi层面的
数据库主从
大数据高并发
jq啊，缓存啊，redis，node
mycat数据库中间件来做数据库的主从支持和分库分表
redis monogdb 消息队列服务rabbitmq或者kafka ，搜索引擎sphinx 或者 es
storm spark sql hadoop---- kafka python java R html(前几个大数据必备)


常用过滤函数
{
mysql_real_escape_string
str_replace
preg_match
fnmatch
trim
addslashes()//get_magic_quotes_gpc()//get_magic_quotes_runtime()//magic_quotes_gpc
htmlspecialchars
intval
}
常用函数及示例
{
	
}







#php输出
<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello World!";
?>

</body>
</html>


#php序列化：serialize
<?php 
class foo { 
	public $ﬁle = "test.txt"; 
	public $data = "123456"; 
	function __destruct() { 
		ﬁle_put_contents($this->ﬁle, $this->data); 
	} 
	public function PrintData()    
    {    
        echo 'content of' . $this->file . ' is ' . $this->data    
             . '.<br />';    
    }    
} 

$f = new foo();
$f->ﬁle = "xx.php"; 
$f->data = "<?php phpinfo(); ?>"; 
$f->PrintData();
echo base64_encode(serialize($f)); 
?>

#php反序列化
<?php 
class foo{ 
	public $file = "test.txt"; 
	public $data = "123456"; 

	function __destruct(){ 
		file_put_contents($this->file,$this->data); 
	} 
} 
$d = $_REQUEST['str']; 
var_dump($d); echo "<br />"; 
$tc = unserialize(base64_decode($d)); 
var_dump($tc); 
?>

#php定义对象和方法
<?php     
class TestClass  //定义一个类
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



#php显示源代码
<?php
show_source("test.php");
highlight_file(__FILE__);
?>
#返回指定的PHP文件，并按照语法语义用高亮颜色突出显示文件内容。其中的突出显示的代码都是用HTML标记处理过的。
<?php
highlight_file("php_script.php");
?>
<?php  
  echo file_get_contents("test.php"); 
?> 

#比较出两个字符串的不同程度。
<?php
$str1 = "carrot";
$str2 = "carrrott";
echo levenshtein($str1, $str2); //Outputs 2
?> 

#获取与设置cookie
<?php
$name = $_COOKIE['user];
$sql = "select * from uservote where user ='".$name."'"; //变量名name 和 user别弄混了

//设置cookie
setcookie("user",$user, time()+3600*24);

?>