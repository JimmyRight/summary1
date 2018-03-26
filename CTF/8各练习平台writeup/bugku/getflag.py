import requests   
import base64  
      
url='http://ctf4.shiyanbar.com/web/10.php'   
req=requests.get(url)  
print req.text  
key=req.headers['FLAG']  
key=base64.b64decode(key)  
key=key.split(':')[1].strip()  
data={'key':key}  
r=requests.post(url,data=data)   
print(r.text)  
