import requests
import json
import matplotlib
import matplotlib.pyplot as plt
import xlwt
import xlrd

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Referer': 'https://bj.meituan.com/s/%E7%81%AB%E9%94%85/'
}
cookie = {
    'Cookie': '' #填自己的cookie
}
session = requests.session()
urlfirst = 'https://bj.meituan.com/ptapi/recommends?limit=10'
response = session.get(url=urlfirst, headers=header, cookies=cookie)
items = json.loads(response.text)
for i in items:
    #print(i)
    itemId = i['itemId']
    name = i['title']
    score = i['score']
    lowPrice = i['lowPrice']
    avgPrice = i['avgPrice']
scores = []
avgPrices = []
workbook = xlwt.Workbook(encoding='utf-8')   # 创建一个workbook 设置编码
worksheet = workbook.add_sheet('My Worksheet')    # 创建一个worksheet
for i in range(1, 67):
    data = {
        'uuid': '', #填自己的uuid
        'userid': -1,
        'limit': 32,
        'offset': 32*i,
        'cateId': -1,
        'q': '%E7%81%AB%E9%94%85'
    }
    url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1?'
    response = session.get(url, params=data, headers=header, cookies=cookie)
    result = json.loads(response.text)
    items = result['data']['searchResult']
    wb = xlrd.open_workbook('1.xls')  # 打开表格
    tabsheet = wb.sheets()[0]  # 取1.xls表格内第一个表
    k = tabsheet.nrows  # 判断该表已有多少行内容
    for t, item in enumerate(items):
        worksheet.write(k + t, 0, k + t)
        worksheet.write(k + t, 1, item['id'])
        worksheet.write(k + t, 2, item['title'])
        worksheet.write(k + t, 3, item['avgscore'])
        worksheet.write(k + t, 4, item['lowestprice'])
        worksheet.write(k + t, 5, item['avgprice'])
        worksheet.write(k + t, 6, item['comments'])
        worksheet.write(k + t, 6, item['historyCouponCount'])

    workbook.save('1.xls')
