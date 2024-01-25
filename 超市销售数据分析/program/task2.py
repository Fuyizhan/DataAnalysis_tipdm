import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task2_1():
    # 绘制生鲜类商品和一般商品每天销售金额的折线图，并分析比较
    # 两类产品的销售状况。

    '''
    先得到 每天不同类别的销售额 数据
    再根据数据生成折线图
    '''

    # 读取数据
    df = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 得到每天不同类别的销售额
    grouped_df = df.groupby(['销售日期', '商品类型']).agg({'销售金额': 'sum'}).reset_index()

    # 删去 联营商品 类型
    grouped_df_filtered = grouped_df[grouped_df['商品类型'] != '联营商品']

    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 生成图
    plt.figure(figsize=(18, 10))
    sns.lineplot(x='销售日期', y='销售金额', hue='商品类型', marker='o', data=grouped_df_filtered)
    plt.xticks(rotation=90)
    plt.xlabel('日期')
    plt.ylabel('销售额')
    plt.title('商品每天销售金额的折线图')
    plt.legend()
    plt.show()

def task2_2():
    #  按月绘制各大类商品销售金额的占比饼图，并分析其销售状况。

    '''
    先得到每月各大类商品的销售额
    再绘图
    '''

    # 读取数据
    df = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 根据日期生成月列
    df['销售日期'] = pd.to_datetime(df['销售日期'])
    df['月份'] = df['销售日期'].dt.month

    # 提取所需数据
    grouped_df = df.groupby(['月份', '大类名称']).agg({'销售金额': 'sum'}).reset_index()

    # 把 月份 设为 列， 即可通过 月份 得到 本月的销售额
    pivot_df = grouped_df.pivot(index='大类名称', values='销售金额', columns='月份')

    # 把 NAN 设为 0
    pivot_df = pivot_df.fillna(0)

    # 因为有四个月， 所以生成四个子图
    fig, axs = plt.subplots(2, 2, figsize=(16, 10))

    # 先把子图 二维 展平为 一维
    axs = axs.flatten()

    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 循环生成子图 使用enumerate在传value 的同时传 index
    for i, month in enumerate(pivot_df.columns):
        axs[i].pie(pivot_df[month], labels=pivot_df.index, autopct='%1.1f%%', startangle=90)
        axs[i].set_title(f"{month}月销售金额")

    # 在子图之外添加通用图例
    plt.legend(pivot_df.index, title='大类名称', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()

def task2_3():
    # 绘制促销商品和非促销商品销售金额的周环比增长率柱状图

    '''
    以 是否促销为区别 计算每日销售额
    再计算每周销售额
    '''

    # 读取数据
    data_csv = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 提取所需列
    data_csv = data_csv[['销售日期', '销售金额', '是否促销']]

    # 是否促销分组
    data_csv_promotion_yes = data_csv[data_csv['是否促销'] == '是']
    data_csv_promotion_no = data_csv[data_csv['是否促销'] == '否']

    # 每天销售总额
    data_csv_promotion_yes = data_csv_promotion_yes.groupby('销售日期').agg({'销售金额': 'sum'})
    data_csv_promotion_no = data_csv_promotion_no.groupby('销售日期').agg({'销售金额': 'sum'})

    # 生成周列
    data_csv_promotion_yes['周数'] = week(data_csv_promotion_yes)
    data_csv_promotion_no['周数'] = week(data_csv_promotion_no)

    # 每周销售额
    data_csv_promotion_yes = data_csv_promotion_yes.groupby('周数').agg({'销售金额': 'sum'})
    data_csv_promotion_no = data_csv_promotion_no.groupby('周数').agg({'销售金额': 'sum'})

    # 周环比增长率
    promotion_yes_rate = round(data_csv_promotion_yes['销售金额'].pct_change(), 4)
    promotion_no_rate = round(data_csv_promotion_no['销售金额'].pct_change(), 4)
    # 第一年 nan 设为 0
    promotion_yes_rate = promotion_yes_rate.fillna(0)
    promotion_no_rate = promotion_no_rate.fillna(0)

    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # 设置整体图框大小
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))

    # 绘制第一个子图
    axs[0].bar(promotion_yes_rate.index,
            promotion_yes_rate,
            label='促销商品',
            color='red')

    axs[0].set_xlabel('周数')
    axs[0].set_ylabel('增长率')
    axs[0].set_title('销售金额的周环比增长率柱状图')
    axs[0].legend()
    # 设置x轴的密度间隔为1
    axs[0].set_xticks(range(min(promotion_yes_rate.index), max(promotion_yes_rate.index)+1, 1))


    # 绘制第二个子图
    axs[1].bar(promotion_no_rate.index,
               promotion_no_rate,
               label='非促销商品',
               color='blue')

    axs[1].set_xlabel('周数')
    axs[1].set_ylabel('增长率')
    axs[1].set_title('销售金额的周环比增长率柱状图')
    axs[1].legend()
    # 设置x轴的密度间隔为1
    axs[1].set_xticks(range(min(promotion_no_rate.index), max(promotion_no_rate.index) + 1, 1))

    plt.show()


def week(DataFrame):
    # 确定周数
    whole_week = 0
    # 定义一个周数组，在补充完后可以直接添加到df的column上
    week = []
    # 不是整周的情况下
    if ( (len(DataFrame) % 7) != 0):
        whole_week_minus_1 = len(DataFrame) // 7
        for i in range(1, whole_week_minus_1 + 1):
            for __ in range(7):
               week.append(i)

        for __ in range((len(DataFrame) % 7)):
            week.append(whole_week_minus_1 + 1)
    # 整周的情况下
    else:
        whole_week = len(DataFrame) / 7
        for i in range(1, whole_week + 1):
            for __ in range(7):
               week.append(i)

    return week

if __name__ == '__main__':
    task2_1()
    task2_2()
    task2_3()