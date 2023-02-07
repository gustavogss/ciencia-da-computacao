import requests
from parsel import Selector 

res = requests.get('http://books.toscrape.com/')
# print(res.status_code)
selector = Selector(text=res.text)

# pega todas as imagens da página
print(selector.css('img.thumbnail').getall()) 

# pega a primeiro elemento img da página
print(selector.css('img.thumbnail').get()) 

#pega o elemento img de indice 0, a primeira imagem 
# (img é o elemento da página, e thumbnail é a classe do elemento)
print(selector.css('img.thumbnail').getall()[0]) 

#para iterar entre todos os elementos img
for thumbnail in selector.css('img.thumbnail').getall():
    print(thumbnail)


