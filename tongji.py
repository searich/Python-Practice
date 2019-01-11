open_file = open('tongji.txt', 'r', encoding='utf-8')
read = open_file.readlines()
open_file.close()
new_file = open('sumtongji.txt', 'w', encoding='utf-8')

for line in read:
    dividword = line.split()
    if len(dividword) != 0:
        # print(dividword)
        # print(len(dividword))
        sum = 0
        for score in dividword[1:-1]:
            sum = sum + int(score)
            # print(sum)
        result = dividword[0] + str(sum) + '\n'
        print(type(result))
        print(result)
        new_file.write(result)

new_file.close()
