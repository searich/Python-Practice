import webbrowser

keyword = input('enter keyword: ')
keyword = keyword.encode('utf-8')
print(keyword)
webbrowser.open(
    'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' +
    keyword +
    '&rsv_pq=ee30bb2a0001024c&rsv_t=851dypc5FARe043M%2ByALWHA0ci5hK23zZWSObRGJqOq9DdesZFWM6sKk0P0&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=4027&rsv_sug4=4656'
)
