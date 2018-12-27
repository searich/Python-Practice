import sys, pyperclip


adress = {'office': '广州市黄埔区科学大道112号绿地中央广场A1栋1204房'}
office = sys.argv[1]

if office in adress:
    pyperclip.copy(adress['office'])
else:
    print('Not correct input.')
