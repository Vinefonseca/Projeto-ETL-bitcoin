import requests as r

url = 'https://jsonplaceholder.typicode.com/posts/1'
params = {"postID:1"}
response = r.get(url, params=params)

comentarios = response.json()

print(comentarios)

