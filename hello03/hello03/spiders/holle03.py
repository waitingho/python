
import scrapy

class PCHomeSpider(scrapy.Spider):
    name = "hello03"

    def start_requests(self):
        urls = [
            'http://24h.pchome.com.tw/index/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
    	top_sale_list = []

    	for i  in range(1,6):
    		str_idx   = ''+('%s'%i)
    		str_xpath = '//*[@id="hot_list"]/dl/dd[2]/ul/li['+str_idx+']/div/h5/a//text()'
    		titleList = response.xpath(str_xpath).extract()
    		strTitle  = ''.join(titleList)
    		str_xpath = '//*[@id="hot_list"]/dl/dd[2]/ul/li['+str_idx+']/div/h5/a//@href'
    		urlList   = response.xpath(str_xpath)[0].extract()
    		strUrl    = ''.join(urlList)
    		top_sale_list.append({'title':strTitle,'link':strUrl})
    	for item in top_sale_list:
    		
            print(item['title'])
    		print(item['link'])

    	print('\n')
    	#self.log('HTML %s loaded' % response.url)
