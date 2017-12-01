import scrapy 
import json
import requests
import time
#import decode
from PCHomeSearch.items import PchomesearchItem

class PCHomeSearch(scrapy.Spider):
	name = "PCHomeSearch"
	#scrapy crawl PCHomeSearch -a k=iphone -a p=2
	def __init__(self,k='',p='1',*args,**kwargs):
		super(PCHomeSearch,self).__init__(*args,**kwargs)
		self.k = k
		self.p = p
	def start_requests(self):
		urls = []
		for i in range(1,int(self.p)+1):
			str_page = ''+('%s'%i)
			tmp = 'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%s&page=%s&sort=rnk/dc'%(self.k,str_page)
			urls.append(tmp.strip())
		#urls = []
		#for i in range(1,6):
			#str_idx =''+('%s' % i)
			#urls.append('http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page='+str_idx'&sort=rnk/dc',)
			#'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=1&sort=rnk/dc',
		#urls = ['http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=1&sort=rnk/dc',
				#'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=2&sort=rnk/dc',
				#'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=3&sort=rnk/dc',
				#'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=4&sort=rnk/dc',
				#'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=5&sort=rnk/dc',]
				#'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=6&sort=rnk/dc']

		#urls = ['http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=1&sort=rnk/dc',]	
		for url in urls:
			print(url)
			time.sleep(1)
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		json_data = json.loads(response.body.decode('utf-8'))
		item = PchomesearchItem()
		for json_array in json_data["prods"]:
			item['title'] = json_array['name']
			item['link']  = "http://24h.pchome.com.tw/prod/"+json_array["Id"]
			item['desc']  = json_array['describe']
			item['price']  = json_array["price"]
			yield item
			#print(json_array["Id"])
			#print(json_array["name"])
			#print(json_array["price"])
			#print(json_array)
		#print(json_data)
		#json_data.close()
		#print(json_data["prods"][0]["Id"])
		#print(json_data["prods"][0]["cateld"])
		#print(json_data["prods"][0]["name"])
		#print(json_data["prods"][0]["describe"])
		#print(json_data["prods"][0]["price"])


		print('\n')
		self.log('HTML %s loaded ' % response.url)