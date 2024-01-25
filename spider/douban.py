# get 请求
# 获取豆瓣第一页的数据
import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

# 请求对象
request = urllib.request.Request(url=url, headers=headers)

# 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 数据下载到本地
with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

