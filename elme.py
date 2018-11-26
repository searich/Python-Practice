import requests
res = requests.get('https://www.ele.me/place/ws100xkkpznf?latitude=22.54055&longitude=113.934401')
print(res.text)