import scrapy 
import json
#import decode
from PCHomeSearch.items import PchomesearchItem

class PCHomeSearch(scrapy.Spider):
	name = "PCHomeSearch02"

	def start_requests(self):

		urls = []
		for i in range(1,6):
			str_idx =''+('%s' % i)
			urls.append('http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page='+str_idx'&sort=rnk/dc')
			#'http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=1&sort=rnk/dc',
		
		for url in urls:
			print(url)
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