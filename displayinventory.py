def displayInventory(inventory: dict):
    print(inventory)
    num_inv = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        num_inv += v


inv = {'dragon': 1, 'dragger': 2, 'arrow': 2, 'gold coin': 42, 'torch': 6, 'rope': 1}
displayInventory(inv)
