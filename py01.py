import requests

sanguo = requests.get("https://www.baidu.com")
sanguo.encoding = 'utf-8'

#创建一个文件对象，指针放在文件末尾
k = open("baidu.txt", 'a+')

#把下载的内容写入文件对象
for words in sanguo.text:
    try:
        k.write(words)
    except:
        pass
    continue


k.close()