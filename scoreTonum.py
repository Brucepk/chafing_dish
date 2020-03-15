import xlrd
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10), dpi=80)
datas = xlrd.open_workbook('1.xls')
table = datas.sheets()[0]
'''print(table.nrows)           
print(table.ncols)         
print(table.row_values(0))    
print(table.cell(0,0).value)'''
score_cols = table.col_values(3)  # 获取评分
avg_cols = table.col_values(5)  # 获取平均消费
comment_cols = table.col_values(6)  # 获取评论数量
t = 2.9
scores = []
nums = []
while t <= 4.9:
    t += 0.1
    score = round(t, 2)
    scores.append(score)
    nums.append(score_cols.count(score))
print(nums)
price = [i-j-1 for j, i in enumerate(range(1, 22))]
for i, j in zip(score_cols, avg_cols):
    if j != 0:
        price[scores.index(i)] += j
price_avg = [round(i/j, 2) for i, j in zip(price, nums)]
print(price_avg)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
x = range(len(scores))
'''plt.title('火锅店星级评价整体情况', color='r', fontweight=800, size=50)
plt.bar(x, nums, label='该评分火锅店数量', width=0.5, color='r')
for a, b in zip(x, nums):
    plt.text(a, b+2, b, ha='center', va='bottom', fontsize=15)'''
plt.title('不同评分的平均人均消费', color='r', fontweight=800, size=50)
plt.bar(x, price_avg, label='不同评分的平均价格', width=0.4, color='y')
for a, b in zip(x, price_avg):
    plt.text(a, b+2, b, ha='center', va='bottom', fontsize=15)
plt.xticks(x, scores, size=20)   # x坐标'''
plt.grid(axis="y")  #生成网格
plt.show()