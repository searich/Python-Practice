import pprint, ex1

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileobj = open('ex1.py', 'a')
fileobj.write('cats = ' + pprint.pformat(cats) + '\n')
fileobj.close()

print(ex1.cats)
