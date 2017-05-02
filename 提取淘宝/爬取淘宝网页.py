import requests
import re

#获取页面函数、
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print("")
#对获取页面进行解析
def parsePage(ilt,html):
	try:
		#在爬取下来的网页中进行查找价格
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		#在爬取下来的网页中查找物品
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price=eval(plt[i].split(':')[1])
			title=eval(tlt[i].split(':')[1])
			ilt.append([price,title])
	except:
		print("")
#进行打印
def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号", "价格", "商品名称"))
	count = 0
	for g in ilt:
		count = count + 1
		print(tplt.format(count, g[0], g[1]))

def main():
	goods='书包'
	depth=2
	start_url='https://s.taobao.com/search?q='+goods
	infoList=[]
	for i in range(depth):
		try:
			#str函数的作用是将其中的内容转换为字符串
			url=start_url+'&s='+str(44*i)
			html=getHTMLText(url)
			parsePage(infoList , html)
		except:
			continue
	printGoodsList(infoList)

main()
