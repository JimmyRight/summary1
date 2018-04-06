#逻辑处理漏洞 
##in_array函数
in_array() 函数搜索数组中是否存在指定的值,但是这个这个函数会在比较前做类型转换

比如缺陷代码为：

    <?php  
    if(in_array($_GET['typeid'], array(1,2,3,4,5)))  
    {  
        $sql="select * from hehe where typeid='".$_GET['typeid']."'";  
        echo $sql;  
    }  

这个代码的作用是过滤GET参数typeid在不在1,2,3,4,5这个数组里面，如果在里面就拼接在sql语句里面，看起来好像没有问题，但是这个这个函数会在比较前做类型转换，所以，当请求<http://localhost:8000/fugai.php?typeid=1%27%20union%20select%201,2,3,4,5%20%23>

输出的值为：
	select * from hehe where typeid='1' union select 1,2,3,4,5 #'

这样就可以绕过这个脆弱的函数了

##双等于和三等于
首先双等于会造成安全问题，因为在判断之前，双等于会将变量做类型转换
，而三等于则不会，由于数据类型发生了改变，所以双等于在判断的时候可能存在安全风险

我用这个代码进行测试:

	var_dump($_GET['var']==2);

	当我访问：http://localhost:8000/fugai.php?var=2 返回的是true
	当我访问：http://localhost:8000/fugai.php?var=2aaaa 返回的依然是true
	当我访问：http://localhost:8000/fugai.php?var=3
	或者当我访问：http://localhost:8000/fugai.php?var=3aaaa时，返回的是false
所以双等于把变量的类型进行了转换

而用三等于时:

	var_dump($_GET['var']===2);
	访问： http://localhost:8000/fugai.php?var=2aaaa返回的是false

##php可变变量(间接寻址)

先看代码

    $a="heheda";  
    $$a="123";  
    echo $heheda;  

	这个代码输出的是123,这个123是在$a赋值的，这时候$a被赋值了“heheda”,而$$a就相当于$heheda