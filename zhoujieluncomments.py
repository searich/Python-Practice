import requests
import json

url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=718475&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=101010'
r = requests.get(url)
jsonr = json.loads(r.text)
comm_list = jsonr['hot_comment']['commentlist']
topic = jsonr['topic_name']
comm = [x['rootcommentcontent'] for x in comm_list]
# comm = []
# for x in comm_list:
#     comm.append(x['rootcommentcontent'])
comments = '\n'.join(comm)
comms = open('comments.txt', 'w')
comms.write(comments)
comms.close()
