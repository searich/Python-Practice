# x, y = 3, 4
# smaller = x if x < y else y
# print(smaller)

from lxml import html
import requests


page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)

buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')

print("buyers", buyers)
print("prices", prices)
