import requests,json

url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws0efg7jyc8d&latitude=23.178028&limit=24&longitude=113.328385&offset=0&terminal=web'
res = requests.get(url)
jsonres = json.loads(res.text)
print(type(jsonres))
for x in jsonres:
    print(x['name'],x['phone'])

