import requests as r

url = 'https://jsonplaceholder.typicode.com/posts/1'

resposta = r.get(url)

print(resposta)

