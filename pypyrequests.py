import requests
# sanguo = requests.get('https://static.pandateacher.com/sanguo.md')
# k = open('sanguo.txt', 'a+')
# for words in sanguo.text:
#     try:
#         k.write(words)
#     except:
#         pass
#     continue
# k.close()

# p = open('sanguo.txt','wb')
# for wordsapp in sanguo.content:
#     p.write(sanguo.content)
# p.close()

# getmusic = requests.get('https://static.pandateacher.com/py_1.mp3')
# music = open('py.mp3', 'wb')
# music.write(getmusic.content)
# music.close()

getpic = requests.get('https://gratisography.com/thumbnails/gratisography-318-thumbnail.jpg')
pic = open('py.jpg', 'wb')
pic.write(getpic.content)
pic.close()
