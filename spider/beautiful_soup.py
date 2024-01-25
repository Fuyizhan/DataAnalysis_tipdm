from bs4 import BeautifulSoup
soup = BeautifulSoup(open('testbs4.html', encoding='utf-8'), 'lxml')
print(soup.a)
print(soup.a.attrs)
print(soup.find('a'))
print(soup.find('a', title="a2"))
print(soup.find('a', class_="a1"))
print(soup.find_all('a'))
print(soup.find_all(['a', 'span']))
print(soup.find_all('li', limit=2))
print(soup.select('a'))
print(soup.select('.a1'))
print(soup.select('#l1'))
print(soup.select('li[id]'))
print(soup.select('li[id="l2"]'))
print(soup.select('div li'))
print(soup.select('div > ul > li'))
print(soup.select('a,li'))
obj = soup.select('#d1')[0]
print(obj.string)
print(obj.get_text())
obj = soup.select('#p1')[0]
print(obj.name)
print(obj.attrs)
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])