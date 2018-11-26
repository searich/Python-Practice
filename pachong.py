import requests
sanguo = requests.get('https://static.pandateacher.com/sanguo.md')
k = open('sanguo.txt','w+')
for words in sanguo.text:
try:
    k.write(sanguo.text[:800])
    except:
    pass
    continue
k.close()