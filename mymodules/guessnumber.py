def collatz(num):
    if num % 2 == 0:
        return num / 2
    elif num % 2 == 1:
        return 3 * num + 1

# To get 1


try:
    num_input = int(input('Enter number: '))
    num = collatz(num_input)
    while num > 1:
        print(int(num))
        num = collatz(num)
        if num == 1:
            print(int(num))
            break
except ValueError:
    print('integret number only!')
