import requests
import json
i = 1
while i < 6:
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=36514931546246044&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p='+str(i)+'&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    r = requests.get(url)
    jsonr = json.loads(r.text)
    music = jsonr['data']['song']['list']
    for x in music:
        print(x['name'])
    i += 1
