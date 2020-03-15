import xlrd
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10), dpi=80)
plt.title('评论数量散点分布图', color='r', fontweight=800, size=50)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
datas = xlrd.open_workbook('1.xls')
table = datas.sheets()[0]
score_cols = table.col_values(3)  # 获取评分
avg_cols = table.col_values(5)  # 获取平均消费
comment_cols = table.col_values(6)  # 获取评论数量
print(comment_cols)
comment_x = [i for i in range(0, 18000, 100)]
comment_num = [i-i for i in range(0, 18000, 100)]
for i in comment_cols:
    comment_num[int(i/100)] += 1
x = range(len(comment_x))
for i, j in zip(x[1:], comment_num[1:]):
    if j!=0:
        plt.scatter(i, j, c='r', s=3)
plt.xticks(x[1::19], comment_x[1::19], size=20, color='r')   # x坐标
plt.grid(axis="y")  #生成网格
plt.show()