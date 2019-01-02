import requests, bs4


url = 'https://www.amazon.com/gp/aq-feedback/lazyLoad/handler/af-link-handler.html?pl=%7B%22adPlacementMetaData%22%3A%7B%22adElementId%22%3A%22pdagDesktopSparkle%22%2C%22pageType%22%3A%22Search%22%2C%22slotName%22%3A%22auto-sparkle-hsa-tetris%22%2C%22pageUrl%22%3A%22%22%2C%22searchTerms%22%3A%22bWFjYm9vayBwcm8%3D%22%7D%2C%22adCreativeMetaData%22%3A%7B%22adNetwork%22%3A%22aax%22%2C%22adProgramId%22%3A1010%2C%22adImpressionId%22%3A%22%22%2C%22adCreativeId%22%3A%221813706480501%22%2C%22adId%22%3A%228929865290901%22%7D%7D'

res = requests.get(url)
res_text = 

print(type(res.text))
