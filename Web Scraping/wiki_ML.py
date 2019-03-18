import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup = bs4.BeautifulSoup(res.text, 'lxml')
for i in soup.select('.toctext'):
    print(i.text)


