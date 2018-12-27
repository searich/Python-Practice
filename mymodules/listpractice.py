def joinListContent(somelist: list) -> str:
    print(' '.join(somelist[:-1]) + ' and ' + somelist[-1])


alist = ['I', 'love', 'cat', 'dog']
joinListContent(alist)
