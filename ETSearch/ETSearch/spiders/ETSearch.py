import scrapy
import time

from ETSearch.items import EtsearchItem

class ETSearch(scrapy.Spider):
	name = "ETSearch"

	#scrapy crawl ETSearch -a k=蔣萬安 -a p=2

	def __init__(self,k='',p='1',*args,**kwargs):
		super(ETSearch, self).__init__(*args, **kwargs)
		self.k = k
		self.p = p

	def start_requests(self):

		urls = []
		for i in range(1,int(self.p)+1):
			str_page = ''+('%s' % i)
			tmp = 'https://www.ettoday.net/news_search/doSearch.php?keywords=%s&page=%s' % (self.k,str_page)
			urls.append(tmp.strip())

		for url in urls:
			print(url)
			time.sleep(1)
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		item = EtsearchItem()
		str_xpath = '//*[@id="result-list"]/div'
		count = len(response.xpath(str_xpath))
		for i in range(1,count+1):
			str_idx   = ''+('%s' % i)
			str_xpath = '//*[@id="result-list"]/div['+str_idx+']/div[2]/h2/a//text()'
			titleList = response.xpath(str_xpath).extract()
			strTitle  = ''.join(titleList)
			str_xpath = '//*[@id="result-list"]/div['+str_idx+']/div[2]/h2/a//@href'
			urlList   = response.xpath(str_xpath)[0].extract()
			strUrl    = ''.join(urlList)
			#//*[@id="result-list"]/div[2]/div[2]/p
			str_xpath = '//*[@id="result-list"]/div['+str_idx+']/div[2]/p//text()'
			bodyList  = response.xpath(str_xpath).extract()
			strBody   = ''.join(bodyList)

			item['title'] = strTitle
			item['link']  = strUrl
			item['body']  = strBody 
			yield item

		self.Log('HTML %s loaded' % response.url)




