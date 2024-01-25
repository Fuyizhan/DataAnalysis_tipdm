import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def task3_1():
    # 根据消费情况，分别为累计消费前 10 的顾客画像。

    # 读取数据
    df = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 提取所需数据
    df_new = df[['顾客编号', '销售金额']]

    # 计算每位顾客消费额
    df_new = df_new.groupby('顾客编号').agg({'销售金额': 'sum'}).reset_index()

    # 降序
    df_new.sort_values(by=['销售金额'], ascending=False, inplace=True)

    # 得到前十id 并提取他们的消费信息
    top10_customer_id = df_new.index[0: 10]
    top10_customer = []
    for id in top10_customer_id:
        top10_customer.append(df[df['顾客编号'] == id])

    print(top10_customer)

def task3_2():
    # 分析各大类商品的销售情况，总结其销售规律。

    '''
    利用折线图显示， 可以清楚看出各个商品的走势
    确定参考因素  销售情况 即 每天的销售数量
    '''

    # 读取数据
    df = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 提取所需行
    df_new = df[['大类名称', '销售日期', '销售数量']]

    # 统计每日数量
    grouped_df = df_new.groupby(['大类名称', '销售日期']).agg({'销售数量': 'sum'}).reset_index()

    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(16, 8))

    sns.lineplot(x='销售日期', y='销售数量', hue='大类名称', data=grouped_df)

    plt.xlabel('销售日期')
    plt.ylabel('销售数量')
    plt.xticks(rotation=90)
    plt.show()

def task3_3():
    # 分析促销对商品销售的影响，为超市制定销售策略提供建议。

    '''
    对比促销和不促销对 销售量和销售金额 的影响
    对比同一类产品在促销和不促销时对 销售量和销售金额 的影响
    对比不同的时间段 促销和不促销对  销售量和销售金额  的影响
    '''

    # 读取数据
    df = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 提取所需数据
    df1 = df[['是否促销', '销售数量', '销售金额']]

    # 分组求和
    grouped_df1 = df1.groupby('是否促销').agg({'销售数量': 'sum', '销售金额': 'sum'}).reset_index()

    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 生成比较图
    plt.figure(figsize=(10, 6))
    sns.barplot(x='是否促销', y='销售数量', data=grouped_df1)
    plt.title('销售数量 ： 促销 VS 不促销')
    plt.xlabel('促销情况')
    plt.ylabel('销售数量')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='是否促销', y='销售金额', data=grouped_df1)
    plt.title('销售金额 ： 促销 VS 不促销')
    plt.xlabel('促销情况')
    plt.ylabel('销售额')
    plt.show()

    '''对比可得 不促销的销售额和销售量都远远大于促销的'''

    # 提取所需数据
    df2 = df[['是否促销', '销售数量', '销售金额', '大类名称']]

    # 分组求和
    grouped_df2 = df2.groupby(['是否促销', '大类名称']).agg({'销售数量': 'sum', '销售金额': 'sum'}).reset_index()

    # 生成比较图
    plt.figure(figsize=(16, 8))
    sns.barplot(x='大类名称', y='销售数量', hue='是否促销', data=grouped_df2)
    plt.title('各大类销售数量 ： 促销 VS 不促销')
    plt.xlabel('大类名称')
    plt.ylabel('销售数量')
    plt.show()

    # 生成比较图
    plt.figure(figsize=(16, 8))
    sns.barplot(x='大类名称', y='销售金额', hue='是否促销', data=grouped_df2)
    plt.title('各大类销售金额 ： 促销 VS 不促销')
    plt.xlabel('大类名称')
    plt.ylabel('销售金额')
    plt.show()

    '''
    对比可得 各类产品不促销的销售额和销售量都远远大于促销的， 
    只有日配的促销量是高于不促销的
    '''

    # 根据日期生成月列
    df['销售日期'] = pd.to_datetime(df['销售日期'])
    df['月份'] = df['销售日期'].dt.month

    # 提取所需数据
    df3 = df[['是否促销', '销售数量', '销售金额', '月份']]

    # 分组求和
    grouped_df3 = df3.groupby(['是否促销', '月份']).agg({'销售数量': 'sum', '销售金额': 'sum'}).reset_index()

    # 生成比较图
    plt.figure(figsize=(16, 8))
    sns.barplot(x='月份', y='销售数量', hue='是否促销', data=grouped_df3)
    plt.title('各月销售数量 ： 促销 VS 不促销')
    plt.xlabel('月份')
    plt.ylabel('销售数量')
    plt.show()

    plt.figure(figsize=(16, 8))
    sns.barplot(x='月份', y='销售金额', hue='是否促销', data=grouped_df3)
    plt.title('各月销售金额 ： 促销 VS 不促销')
    plt.xlabel('月份')
    plt.ylabel('销售金额')
    plt.show()

    '''
    二月的销售促销的销售量和销售金额最客观
    '''

if __name__ == '__main__':
    task3_1()
    task3_2()
    task3_3()
