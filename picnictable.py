def printPicnic(itemsdict: dict, leftWidth: int, rightWidth: int):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsdict.items():
        print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth))
        # print(f'''{{k}.ljust({leftWidth}, '-')}  {str({v}).rjust({rightWidth})}''')


picnicitems = {'sandwich': 4, 'apple': 13, 'cup': 8, 'mouse': 1000}
printPicnic(picnicitems, 10, 8)
