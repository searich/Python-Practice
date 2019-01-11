# colors = ['black', 'white']
# sizes = ["S", 'M', 'L']
# for tshirt in ([c, s] for c in colors for s in sizes):
#     print(tshirt)


# dial_code = [
#     (86, 'China'),
#     (91, 'India'),
#     (7, 'Russia'),
#     (81, 'Japa')
# ]
# 利用字典推导快速生成字典
# country_code = {country: code for code, country in dial_code}
# print(country_code)

color_code = [
    ('black', 'dog'),
    ('white', 'cat'),
    ('grey', 'mouse')
]
colorofanimal = {animal: color for color, animal in color_code}
print(colorofanimal)
