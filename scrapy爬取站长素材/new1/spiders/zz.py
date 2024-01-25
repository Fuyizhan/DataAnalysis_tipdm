import scrapy
from scrapy爬取站长素材.items import New1Item



class ZzSpider(scrapy.Spider):

    name = 'zz'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['https://sc.chinaz.com/tag_tupian/ShangXin.html']


    def parse(self, response):
        # 将获取到的网页内容保存到chinaz.html文件内
        with open("chinaz.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        # 建立实体列表
        items = []
        # 获取解析内容(返回的是一个列表)
        content = response.xpath("/html/body/div[2]/div[4]/div/img")
        # 遍历返回的内容
        for each in content:
            # 创建MyspiderItem()【scrapy框架内实体框架(定义获取内容的文件类型)】对象
            item = New1Item()
            # 图片名称  【extract()方法获取属性内容】
            name = each.xpath("@alt")[0].extract()
            # 图片下载地址
            url = 'https:' + each.xpath("@data-original")[0].extract()
            item['name'] = name
            item['url'] = url
            # 将定义好的实体添加到实体列表中
            items.append(item)
        print(items)
        return items
