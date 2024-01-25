from lxml import etree
import requests

# # xpath 解析文件
# tree = etree.parse('demo.html')
#
# # 查看ul li
# li_list = tree.xpath('//body/ul/li')
# print(li_list)
#
# li_list2 = tree.xpath('//ul/li[@id]/text()')
# print(li_list2)
#
# li_list3 = tree.xpath('//ul/li[@id="1"]/text()')
# print(li_list3)

"""获取百度网址的百度一下"""

# 得到百度网页内容
url = 'https://www.baidu.com/'
headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
request = requests.get(url=url, headers=headers)
content = request.text

# 解析html文档 —> 解析树对象
tree = etree.HTML(content)
# xpath 解析树中的匹配对象
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)


""" Xpath helper"""
# //div[@class="name"]/a[@title]
'''
额尔古纳河右岸（茅盾文学奖获奖作品全集28）
我与地坛（纪念版）
活着（余华代表作，精装，易烊千玺推荐阅读）
苏东坡传（林语堂纪念典藏精装版）
胜者心法：资治通鉴成事之道（冯唐从管理讲透古今胜者之道！随书附赠冯唐书法书签）
生死疲劳（不看不知道，莫言真幽默！全新版本！）
病隙碎笔 2021纪念版（史铁生充满灵性光辉的生命笔记，启迪无数读者的长篇哲思散文经典）
人生海海（麦家经典代表作，莫言、罗翔盛赞，入选《人民日报》书单，发行量超300万，创文学新奇迹）
故宫博物院 孩子一定要去的博物馆 图说天下精装版
一句顶一万句（一本让“中国脱口秀扛把子”李诞连声叫绝的茅奖好书，当当专享印签本）
摄影轻松入门一本就够（全彩）
窄门（诺贝尔文学奖经典 读完《窄门》便读懂了纪德的一生 法文直译全新版 “你希望很快忘记吗？—我希望永远...
被讨厌的勇气：“自我启发之父”阿德勒的哲学课 岸见一郎
长安的荔枝
也是冬天，也是春天：升级彩插版（收录迟子建最新散文力作及其经典散文名篇）
知行合一王阳明（百万读者的心学入门书！深入解读知行合一及其创始人王阳明的通俗全传！樊登读书、书单来了...
蛤蟆先生去看心理医生（热销300万册！英国经典心理咨询入门书，知名心理学家李松蔚强烈推荐）
带壳的牡蛎是大人的心脏（当当专享签章版+作者亲绘贴纸。火爆全网现象级漫画，汪苏泷、沈月、容祖儿、阮筠庭...
作家榜名著：月亮与六便士（全新未删节插图珍藏版！毛姆写给年轻人的梦想之书！满地都是六便士，他却抬头看...
知行合一王阳明大全集（套装共3册）（全面解读知行合一理念的经典全集）
'''