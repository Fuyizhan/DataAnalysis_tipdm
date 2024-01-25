import urllib.request
import urllib.parse

# 定制请求头
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request
# 获取响应数据
def get_content(request):
    responde = urllib.request.urlopen(request)
    content = responde.read().decode('utf-8')
    return content
# 下载数据
def down_load(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input("请输入开始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)

    print('爬取完毕')
