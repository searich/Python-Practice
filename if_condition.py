height = 1.75
weight = 80.5
bmi = weight/height**2
print(bmi)
if bmi < 18.5:
    print('过轻')
elif  25 > bmi >= 18.5:
    print('正常')
elif 28 > bmi >= 25:
    print('过重')
elif 32 > bmi >= 28:
    print('肥胖')
else:
    print('严重肥胖')