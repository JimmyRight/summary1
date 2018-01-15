#encoding='UTF-8'
import requests

rsp = requests.get('http://chinalover.sinaapp.com/web12/index.php?key=0xccccccccc')
print rsp
#tmp = base64.b64decode(rsp.headers['FLAG']).split(':')
rsp = requests.post('http://ctf5.shiyanbar.com/web/10/10.php', data={'key':tmp[-1]})
print rsp.text    
