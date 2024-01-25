import urllib.request
from lxml import etree

def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/fengjing.html'
    else:
        url = 'https://sc.chinaz.com/tupian/fengjing_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    responde = urllib.request.urlopen(request)
    content = responde.read().decode('utf-8')
    return content

def down_load(page, content):
    tree = etree.HTML(content)

    name_list = tree.xpath('/html/body/div[3]/div[2]/div/img/@alt')

    src_list = tree.xpath('/html/body/div[3]/div[2]/div/img/@data-original')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]

        url = 'https:' + src

        # 下载图片并保存
        # urllib.request.urlretrieve('图片地址','文件保存的名字')
        urllib.request.urlretrieve(url=url, filename='./img/' + name + '.jpg')
    print("第"+str(page)+"页下载完毕")


if __name__ == '__main__':
    start_page = int(input("请输入开始页码"))
    end_page = int(input("请输入结束页码"))
    for page in range(start_page, end_page):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)