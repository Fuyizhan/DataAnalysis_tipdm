import pandas as pd

def task1_1():
    # 对数据作必要的预处理，在报告中列出处理步骤，将处理后的结果保存为“task1_1.csv”

    '''
    预处理： 去重复 填空值 日期规范化  删除异常值
    '''

    # 读取数据
    data_csv = pd.read_csv(r"D:\googledownload\附件.csv", encoding='gbk')  # r 是防止反斜杠转义的 gbk--简体中文

    # 打印各列名称
    print(data_csv.columns.values)

    # 得到数据量的行列大小
    rows, columns = data_csv.shape
    print("原始数据量：")
    print(f"行数: {rows}, 列数: {columns}")

    # 数据去重
    data_csv.drop_duplicates(inplace=True)
    print("数据去重后:")
    print("行数:" + str(len(data_csv)))

    # 去空值
    # 计算每列的空值个数
    print(data_csv.isnull().sum())
    # how='any' which means if there has any row that contains at least
    # one missing value will be removed.
    # how='all' which means only if all values in the row are missing,then removed
    data_csv = data_csv.dropna(how='any')
    print("数据去空后:")
    print("行数:" + str(len(data_csv)))

    # 日期合法化
    data_csv['销售日期'] = pd.to_datetime(data_csv['销售日期'], format='%Y%m%d', errors='coerce')
    # errors='coerce' means that any values that can't be converted to numeric will be replaced with NaN (Not a Number).
    # 即 任何不能转化成数字的都被NaN值代替
    data_csv = data_csv.dropna(how='any')
    print("日期去空后:")
    print("行数:" + str(len(data_csv)))

    # 销售日期中包含销售月份，所以删除销售月份
    data_csv.drop('销售月份', axis=1, inplace=True)
    # 删除销售数量和销售金额小于0的异常值
    print('删除异常值之前：', data_csv.shape)
    data_csv = data_csv[(data_csv['销售数量'] > 0) & (data_csv['销售金额'] > 0)]
    print('删除异常值之后:', data_csv.shape)

    # 将data存储为task1_1.csv
    data_csv.to_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', index=False, encoding='gbk')

def task1_2():
    # 统计每个大类商品的销售金额，将结果保存为“task1_2.csv”

    '''
    以大类名称为组区别，进行销售金额的求和
    '''

    # 读取预处理后的数据
    data_csv = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 分组求和
    data_main_category = data_csv.groupby(['大类名称']).agg({'销售金额': 'sum'}).reset_index()
    data_main_category.rename(columns={'销售金额': '销售金额总和'}, inplace=True)

    # 将data存储为task1_2.csv
    data_main_category.to_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_2.csv', index=False, encoding='gbk')

def task1_3():
    # 统计每个中类商品的促销销售金额和非促销销售金额，将结果保存为“task1_3.csv
    '''
    先以是否促销为区别 获取每个商品的销售情况
    再以中类名称为组区别，进行销售金额的求和
    '''

    # 读取数据
    data_csv = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 促销
    data_csv_yes = data_csv[data_csv['是否促销'] == '是'].groupby('中类名称').agg({'销售金额': 'sum'})
    data_csv_yes.rename(columns={'销售金额': '促销销售金额总和'}, inplace=True)

    # 不促销
    data_csv_no = data_csv[data_csv['是否促销'] == '否'].groupby('中类名称').agg({'销售金额': 'sum'})
    data_csv_no.rename(columns={'销售金额': '非促销销售金额总和'}, inplace=True)

    # 将两表合并
    data_merge = pd.merge(data_csv_yes, data_csv_no, how='left', left_on='中类名称', right_on='中类名称')
    # how='left' 即 左连接 -- 左表的所有行数据都会显示在融合表中，如果右表的列数据与走表的不一致，则在融合表中显示为NaN值

    # 将data存储为task1_3.csv
    data_merge.to_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_3.csv', index=False, encoding='gbk')

def task1_4():
    # 统计生鲜类产品和一般产品的每周销售金额，将结果保存为“task1_4.csv”

    '''
    通过日期生成周数列，
    以产品类型和日期为区别组,先计算每天同类产品的销售额
    以产品类型和周数为区别组，再计算每周销售额
    '''

    # 读取数据
    data_csv = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 提取所需列
    data_csv = data_csv[['销售日期', '商品类型', '销售金额']]

    # 得到生鲜类
    data_csv_fresh = data_csv[data_csv['商品类型'] == '生鲜']

    # 先计算每天同类产品的销售额，再统计每周
    data_csv_fresh = data_csv_fresh.groupby('销售日期').agg({'销售金额': 'sum'})

    # 给 df 加上周列表
    weeks = week(data_csv_fresh)
    data_csv_fresh['周数'] = weeks

    # 统计每周销售金额
    data_csv_fresh = data_csv_fresh.groupby('周数').agg({'销售金额': 'sum'})
    # 列重命名
    data_csv_fresh.rename(columns={'销售金额': '生鲜类产品周销售金额'}, inplace=True)
    # 得到一般类
    data_csv_common = data_csv[data_csv['商品类型'] == '一般商品']

    # 先计算每天同类产品的销售额，再统计每周
    data_csv_common = data_csv_common.groupby('销售日期').agg({'销售金额': 'sum'})

    # 给 df 加上周列表
    weeks = week(data_csv_common)
    data_csv_common['周数'] = weeks

    # 统计每周销售金额
    data_csv_common = data_csv_common.groupby('周数').agg({'销售金额': 'sum'})
    # 列重命名
    data_csv_common.rename(columns={'销售金额': '一般产品周销售金额'}, inplace=True)

    # 合并两表
    data_merge = pd.merge(data_csv_fresh, data_csv_common, how='left', left_on='周数', right_on='周数')

    # 将data存储为task1_4.csv
    data_merge.to_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_4.csv', index=False, encoding='gbk')

def week(DataFrame):
    # 确定周数
    whole_week = 0
    # 定义一个周数组，在补充完后可以直接添加到df的column上
    week = []
    # 不是整周的情况下
    if ( (len(DataFrame) % 7) != 0):
        whole_week_minus_1 = len(DataFrame) // 7  # 因为不是整周，整除后是少一周的  如:15天3周 15 / 7 = 2
        # 添加到周列表
        for i in range(1, whole_week_minus_1 + 1):
            # 整周七天，添加七次
            for __ in range(7):
               week.append(i)
        # 添加非整周的天数
        for __ in range((len(DataFrame) % 7)):
            week.append(whole_week_minus_1 + 1)

    # 整周的情况下
    else:
        whole_week = len(DataFrame) / 7
        for i in range(1, whole_week + 1):
            for __ in range(7):
               week.append(i)

    return week

def task1_5():
    # 统计每位顾客每月的消费额及消费天数，将结果保存为“task1_5.csv”，并在报告中列出用户编号为 0-10 的结果。

    """
    抽取所需列  即 顾客编号  日期  销售金额
    以顾客和月份  统计消费额
    以顾客和月份 统计天数
    """

    # 读取数据
    data_csv = pd.read_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_1.csv', encoding='gbk')

    # 提取所需列
    data_csv = data_csv[['顾客编号', '销售日期', '销售金额']]

    # 生成月列
    data_csv['销售日期'] = pd.to_datetime(data_csv['销售日期'])
    data_csv['月份'] = data_csv['销售日期'].dt.month

    # 每位顾客每月的消费额
    data_consumer_month = data_csv.groupby(['顾客编号', '月份']).agg({'销售金额': 'sum'}).reset_index()
    data_consumer_month.rename(columns={'销售金额': '消费额'}, inplace=True)

    # size 根据 groupby 来统计出现的次数   name='次数'是 以size统计的数据生成的新列
    data_csv_times = data_csv.groupby(['顾客编号', '月份']).size().reset_index(name='次数')

    # 融合两表
    data_csv_merge = pd.merge(data_consumer_month, data_csv_times, how='left', left_on=['顾客编号', '月份'], right_on=['顾客编号', '月份'])

    # 将data存储为task1_5.csv
    data_csv_merge.to_csv(r'C:\PycharmProjects\project1\超市销售数据分析\result\task1_5.csv', index=False, encoding='gbk')

if __name__ == '__main__':
    task1_1()
    task1_2()
    task1_3()
    task1_4()
    task1_5()


