import requests
import json
import lxml.html
from lxml import etree

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# text = json.loads(r.content)
#
# print(type(text))
#
# for t in text:
#     print(t[:50], '\n')

# r = requests.get('https://api.github.com')
# d = json.loads(r.content)
#
# print(type(d))
# print(d['authorizations_url'])
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# text = json.loads(r.content)
#
# print(text[0])
# html = requests.get('https://www.python.org/').content
#
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath('/html/head/title/text()') # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.
#
# print(title)

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл? в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a') # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    t = li.find('time')
    print(t.get('datetime'), a.text)  # из этого тега забираем текст — это и будет нашим названием