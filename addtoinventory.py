def displayInventory(inventory: dict):
    # print(inventory)
    print('Below is the inventory:')
    num_inv = 0
    for k, v in sorted(inventory.items()):
        print(f'{v} {k}')
        num_inv += v


def addToInventory(inventory: dict, addedItems: list):
    print(inventory)
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)

    print('The inventory has been updated!')
    displayInventory(inventory)


# 调用函数
inv = {'dragon': 1, 'dragger': 2, 'arrow': 2, 'gold coin': 42, 'torch': 6, 'rope': 1}
dragonLoot = ['gold coin', 'dragger', 'ruby']
addToInventory(inv, dragonLoot)
