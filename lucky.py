#! python3
# lucky.py - Opens several google search results.


import requests, sys, webbrowser, bs4


print('googling...') # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# TODO: open a web browser tab for each result
link_elements = soup.select('.r a')
num_open = min(5, len(link_elements))
for i in range(num_open):
    webbrowser.open('https://google.com' + link_elements[i].get('href'))
