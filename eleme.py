import requests,json,random
url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws0ev0vddht8&latitude=23.163753&limit=24&longitude=113.430498&offset=0&terminal=web'
res = requests.get(url)
jsonres = json.loads(res.text)
l = []
for x in jsonres:
    name = x['name']
    rating = x['rating']
    print(name+str(rating))
    l.append(x['name'])
    a = random.choice(l)
    print(a)