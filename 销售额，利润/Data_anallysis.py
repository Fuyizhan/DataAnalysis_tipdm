import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from urllib.request import urlretrieve
# before an image can be displayed, it has to be read into memory using the PIL module
from PIL import Image
import seaborn as sns
def task1_1():
    # 1.1 需要展示 2020 年年度销售额前 3 名的国家及其年增长率。
    # 按照地区，国家，服务分类，统计每年/每季度的销售额和利润 并计算各国、各服务分类销售额和利润同比增长率
    # 第一步需要得到excel的数据 转化为datafile 利用group add 进行统计计算

    # 读取excel数据
    df = pd.read_excel('D:\googledownload\\a\非洲通讯产品销售数据.xlsx')

    # 将df->dataframe 使其可以调用方法筛选
    df = pd.DataFrame(df)

    # 由于表格中没有年度和季度 根据已有的日期来创建

    # 日期规范化
    df['日期'] = pd.to_datetime(df['日期'])

    # 创建年度季度
    df['年度'] = df['日期'].dt.year
    df['季度'] = df['日期'].dt.quarter

    # 根据年度 地区 国家 服务分裂 统计 值 销售额和利润
    year_annual = pd.pivot_table(df, index=['年度', '国家', '地区', '服务分类'],
                                 values=['销售额', '利润'], aggfunc='sum').reset_index()  # 列索引
    # 同理 根据季度 地区 国家 服务分裂 统计 值 销售额和利润
    quarter_annual = pd.pivot_table(df, index=['季度', '国家', '地区', '服务分类'],
                                    values=['销售额', '利润'], aggfunc='sum').reset_index()
    # 奖处理好的数据保存为excel文件
    year_annual.to_excel('各年度销售额和利润.xlsx', index=False)
    quarter_annual.to_excel('各季度销售额和利润.xlsx', index=False)

    # 同比增长率 （当年-上年）/上年
    # 按各国每年的销售额和利润进行分组
    df1 = df.groupby(['年度', '国家']).agg({'销售额': 'sum', '利润': 'sum'}).reset_index()

    # 各国每年销售额同比
    df1['国家销售额每年同比'] = df1.groupby('国家')['销售额'].pct_change() * 100
    # 将最早姨一年的同比 NAN 改为 0 （因为最早一年无比它跟早的数据）
    df1.fillna(0, inplace=True)

    # 各国每年零利润同比 同理
    df1['国家利润每年同比'] = df1.groupby('国家')['利润'].pct_change() * 100
    df1.fillna(0, inplace=True)

    # 服务分类同理
    df2 = df.groupby(['年度', '服务分类']).agg({'销售额': 'sum', '利润': 'sum'}).reset_index()
    df2['服务分类销售额每年同比'] = df2.groupby('服务分类')['销售额'].pct_change() * 100
    df2['服务分类利润每年同比'] = df2.groupby('服务分类')['利润'].pct_change() * 100
    df2.fillna(0, inplace=True)

    # df1 df2 转化为excel表格
    df1.to_excel('各国同比增长率.xlsx', index=False)
    df2.to_excel('各服务分类同比增长率.xlsx', index=False)

    # 2020 年年度销售额前 3 名的国家及其年增长率
    df1_2020 = df1[df1['年度'] == 2020]
    df1_2020_sorted = df1_2020.sort_values('销售额', ascending=False)
    top_3 = df1_2020_sorted.head(3)[['国家', '国家销售额每年同比']]
    print(top_3)

def task1_2():
    # 统计各地区、国家有关服务分类销售额和利润数据。
    # 需要展示各地区有关服务分类利润数据

    # 读取excel数据
    df = pd.read_excel('D:\googledownload\\a\非洲通讯产品销售数据.xlsx')
    df1 = df.groupby(['地区', '服务分类']).agg({'销售额': 'sum', '利润': 'sum'}).reset_index()
    df2 = df.groupby(['国家', '服务分类']).agg({'销售额': 'sum', '利润': 'sum'}).reset_index()
    print(df1)


def task1_3():
    # 统计各个销售经理的成交合同数和成交率
    # 需要展示销售经理成交合同数前 3 名的数据

    # 提取该页数据
    df = pd.read_excel('D:\googledownload\\a\非洲通讯产品销售数据.xlsx', sheet_name=1)

    # 统计经理合同数和 成交率（平均值）
    df1 = df.groupby('销售经理').agg({'销售合同': 'sum', '成交率': 'mean'})

    # 成交率转为百分比形式
    df1["成交率"] = df1["成交率"].apply(lambda x: format(x, '.2%'))

    # 按合同数排序
    df1 = df1.sort_values('销售合同', ascending=False)
    print(df1.head(3))

"""
  绘制非洲各国产品的销售地图，并能够查看该国的销售额和利润。
  根据销售额的降序排列，绘制非洲各国产品销售额和利润数据的图表。
"""
def task2_1():
    # 读取excel数据 筛选所需数据
    df = pd.read_excel('D:\googledownload\\a\非洲通讯产品销售数据.xlsx')
    df1 = df.groupby(['国家']).agg({'销售额': 'sum', '利润': 'sum'}).reset_index()

    df1 = pd.DataFrame(df1)

    # 绘制地图
    fig = px.choropleth(df1,
                        locations='国家',
                        locationmode='country names',
                        color='销售额',
                        hover_data=['利润', '销售额'],
                        title='非洲各国产品销售地图',
                        color_continuous_scale='Blues')

    # 显示图形
    fig.show()


     # 按销售额降序排序
    df1_sorted = df1.sort_values('销售额', ascending=False)

    # 绘制柱状图
    plt.figure(figsize=(12, 6)) # 图形界面
    plt.bar(df1_sorted['国家'], df1_sorted['销售额'], label='销售额') # x, y, lable
    plt.bar(df1_sorted['国家'], df1_sorted['利润'], label='利润')
    plt.xlabel('国家')
    plt.ylabel('金额')
    plt.title('非洲各国产品销售额和利润')
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()

def task2_2():
    # 根据地区、国家等维度，绘制各服务分类的销售额和利润的年增
    # 长率及各季度同比增长率的图表。
    df = pd.read_excel('各年度销售额和利润.xlsx')

    df1 = pd.DataFrame(df)

    # 各国每年销售额同比
    df1['国家、地区销售额年增长率'] = df1.groupby(['国家', '地区'])['销售额'].pct_change() * 100
    # 将最早姨一年的同比 NAN 改为 0 （因为最早一年无比它跟早的数据）
    df1.fillna(0, inplace=True)

    # 各国每年利润同比
    df1['国家、地区利润年增长率'] = df1.groupby(['国家', '地区'])['利润'].pct_change() * 100
    # 将最早姨一年的同比 NAN 改为 0 （因为最早一年无比它跟早的数据）
    df1.fillna(0, inplace=True)

    sorted_list = ['年度', '地区', '国家', '服务分类', '国家、地区销售额年增长率', '国家、地区利润年增长率']

    df1 = df1[sorted_list]

    plt.figure(figsize=(30, 10))
    # df1的行数 即x轴表示每个国家的地区 len是求总体多少
    x = range(len(df1))
    # 设柱宽
    width = 0.35
   # spacing = 0.001
    plt.bar(x, df1['国家、地区销售额年增长率'], width, label='销售额年增长率')
    plt.bar(x, df1['国家、地区利润年增长率'], width, label='利润年增长率')

    plt.xticks(x, df1['服务分类'], rotation=90)

    plt.xlabel('服务分类')
    plt.ylabel('年增长率')
    plt.title('各服务分类的销售额和利润的年增长率')
    plt.legend()
    plt.tight_layout()
    plt.show()

def task2_4():
    # 绘制销售经理的销售合同数前 5 名排行榜。

    # 提取该页数据
    df = pd.read_excel('D:\googledownload\\a\非洲通讯产品销售数据.xlsx', sheet_name=1)

    # 统计经理合同数和
    df1 = df.groupby('销售经理').agg({'销售合同': 'sum'}).reset_index()

    df1 = df1.sort_values('销售合同', ascending=False)

    df1 = df1.head(5)
    plt.figure(figsize=(12, 6))
    x = range(len(df1['销售经理']))

    plt.bar(x, df1['销售合同'], color='blue')

    # 设置x轴刻度标签
    plt.xticks(x, df1['销售经理'], rotation=45)
    plt.xlabel('销售经理')
    plt.ylabel('销售合同数')
    plt.title('销售经理的销售合同数前5名排行榜')

    # 显示柱状图的数值标签
    for i, contract in enumerate(df1['销售合同']):
        plt.text(i, contract, str(contract), ha='center', va='bottom')

    # 显示图表
    plt.tight_layout()
    plt.show()

def task2_5():
    # 绘制销售额后 10 名的国家排行榜。

    df = pd.read_excel('D:\googledownload\\a\非洲通讯产品销售数据.xlsx')

    df1 = df.groupby('国家').agg({'销售额': 'sum'}).reset_index()

    df1 = df1.sort_values('销售额', ascending=False)

    df1 = df1.tail(10)

    plt.figure(figsize=(12, 6))
    x = range(len(df1['国家']))

    plt.bar(x, df1['销售额'])

    plt.xticks(x, df1['国家'], rotation=45)
    plt.xlabel = '国家'
    plt.ylabel = '销售额'
    plt.title('销售额后 10 名的国家排行榜')

    plt.tight_layout()
    plt.show()

'''
# plt.plot([0.895, 0.91, 0.96,1])
# plt.show()

flowers_df = sns.load_dataset('iris')
#print(flowers_df)
#print(flowers_df.species.unique())
# plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)

the hue parameter is used to color the data points based on a categorical variable
# sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, data=flowers_df)
# plt.show()

plt.title('Distribution of Sepal Width')
plt.hist(flowers_df.sepal_width, bins=5)
plt.show()
# specifying the boundaries of each bin
sns.histplot(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))
plt.show()
'''


# tips_df = sns.load_dataset('tips')
# # print(tips_df)
#
# # bill_avg_df = tips_df.groupby('day').agg({'total_bill': 'mean'})
# # plt.bar(bill_avg_df.index, bill_avg_df.total_bill)
# # plt.show()
#
# sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df)
# plt.show()


'''
df = sns.load_dataset('flights')
# plt.plot(df.passengers)
# plt.show()
df = pd.DataFrame(df)
df1 = pd.pivot_table(df, index="month", columns="year", values="passengers", aggfunc='sum')

# df1 = df.groupby(['month', 'year']).agg({'passengers': 'sum'})
# print(df1)
# print(df1.index)  # index depends on what within the groupby

plt.title("No. of Passengers")
sns.heatmap(df1)
plt.show()

sns.heatmap(df1, fmt='d', annot=True, cmap='Blues')
plt.show()
'''
'''
urlretrieve('https://i.imgur.com/SKPbq.jpg', 'chart.jpg')
img = Image.open('chart.jpg')

# an image loaded using PIL is simply a 3 dimensional numpy array

img_array = np.array(img)
img_array.shape
plt.imshow(img)

# turn off the axes
plt.axis('off')
# turn off the grid lines
plt.grid(False)
'''

'''
fig, axes = plt.subplots(2, 3, figsize=(12, 9))
plt.tight_layout(pad=2)

axes[0, 0].set_title('Yield of oranges')
axes[0, 0].set_xlabel('year')
axes[0, 0].set_ylabel('tons per hectare')

plt.show()
'''


