# accept_headers = [
#     # '*/*',  # Принятие любого контента
#     'text/html',  # Принятие только HTML-контента
#     # 'application/json',  # Принятие только JSON-контента
#     'text/html,application/json',  # Принятие как HTML, так и JSON
#     # 'application/json,text/html',  # Принятие JSON с предпочтением HTML
#     # 'application/json,text/html;charset=utf-8',  # Принятие JSON с предпочтением HTML и UTF-8
#     'text/html,application/json',  # Принятие HTML с предпочтением JSON
#     # 'image/*'  # Принятие изображений
# ]


# import requests
# url = 'http://worldagnetwork.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# result = requests.get(url, headers=headers)
# print(result.content.decode())

# a_list = [url_origin + x.find('a').get('href') for x in ul_block] 