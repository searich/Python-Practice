import requests

r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8'
baidu = open('baidu.html', 'w')
baidu.write(r.text)
baidu.close()
