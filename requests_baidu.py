import requests

response = requests.get('https://www.baidu.com')
baidu_hp = open('baidu.html','a+')
content = response.decode('utf-8')
baidu_hp.write(content.text)
baidu_hp.close()