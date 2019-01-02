import requests
import json
# import logging
# logging.disable(logging.debug)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.debug('Start of program')

url = 'http://ictclas.nlpir.org/nlpir/index/getAllContentNew.do'
headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
playload = {
    'type': 'all',
    'content': '我的名字叫吴枫，我的主要工作是教大家学习Python，这份工作让我每天都感到开心.'
}
res = requests.post(url, headers=headers, data=playload)
# Jason 解析字典
words = json.loads(res.text)['dividewords']
# 把词转成列表
split_words = words.split(' ')

# logging.debug(print(split_words))

# 新建一个分词的列表
new_words = []
# 新建一个词性的列表
cixing = []
for single_word in split_words:
    if single_word == split_words[-1]:
        continue
    else:
        final_word = single_word.split('/')
        # logging.debug(print(final_word[0]))
        new_words.append(final_word[0])
        # logging.debug(print(new_words))
        cixing.append(final_word[1])
newlist = '/'.join(new_words)
# 定义词性词典
dict = {
    'n': '名词',
    'nr': '人名',
    'nr1': '汉语姓氏',
    'nr2': '汉语名字',
    'nrj': '日语人名',
    'nrf': '音译人名',
    'ns': '地名',
    'nsf': '音译地名',
    'nt': '机构团体名',
    'nz': '其它专名',
    'nl': '名词性惯用语',
    'ng': '名词性语素',
    't': '时间词',
    'tg': '时间词性语素',
    's': '处所词',
    'f': '方位词',
    'v': '动词',
    'vd': '副动词',
    'vn': '名动词',
    'vshi': '动词“是”',
    'vyou': '动词“有”',
    'vf': '趋向动词',
    'vx': '形式动词',
    'vi': '不及物动词（内动词）',
    'vl': '动词性惯用语',
    'vg': '动词性语素',
    'a': '形容词',
    'ad': '副形词',
    'an': '名形词',
    'ag': '形容词性语素',
    'al': '形容词性惯用语',
    'b': '区别词',
    '': '',
    'bl': '区别词性惯用语',
    'z': '状态词',
    'r': '代词',
    'rr': '人称代词',
    'rz': '指示代词',
    'rzt': '时间指示代词',
    'rzs': '处所指示代词',
    'rzv': '谓词性指示代词',
    'ry': '疑问代词',
    'ryt': '时间疑问代词',
    'rys': '处所疑问代词',
    'ryv': '谓词性疑问代词',
    'rg': '代词性语素',
    'm': '数词',
    'mq': '数量词',
    'q': '量词',
    'd': '副词',
    'p': '介词',
    'pba': '介词“把”',
    'pbei': '介词“被”',
    'c': '连词',
    'cc': '并列连词',
    'u': '助词',
    'uzhe': '着',
    'ule': '了，喽',
    'uguo': '过',
    'ude1': '的',
    'ude2': '地',
    'ude3': '得',
    'usuo': '所',
    'udeng': '等，等等，云云',
    'uyy': '一样，一般，似的，般',
    'udh': '的话',
    'uls': '来讲，来说，而言，说来',
    'uzhi': '之',
    'ulian': '连',
    'e': '叹词',
    'y': '语气词',
    'o': '拟声词',
    'h': '前缀',
    'k': '后缀',
    'x': '字符串',
    'xe': 'Email字符串',
    'xs': '微博会话分隔符',
    'xm': '表情符合',
    'xu': '网址URL',
    'w': '标点符号',
    'wkz': '左括号',
    'wky': '右括号',
    'wyz': '左引号',
    'wj': '句号',
    'ww': '问号',
    'wt': '叹号',
    'wd': '逗号',
    'wf': '分号',
    'wn': '顿号',
    'wm': '冒号',
    'ws': '省略号',
    'wp': '破折号',
    'wb': '百分号千分号',
    'wh': '单位符号'
}
# logging.debug(print(newlist))
print('\n分词的结果是：' + newlist)

cixinglist = ''
for y in cixing:
    cixinglist = cixinglist + dict[y] + '/'
print('它们的词性分别是： ' + cixinglist + '。')

# logging.debug('End of program')
