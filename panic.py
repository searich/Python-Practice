phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))

# plist = plist[1:8]
# plist.remove("'")
# plist.insert(2, plist.pop(3))
# plist.remove(" ")
# plist.extend([plist.pop(), plist.pop()])

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)
