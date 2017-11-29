import scrapy
G
class HelloSpider(scrapy.Spider):
    name = "Test"

    def start_requests(self):
        urls = [
            'http://24h.pchome.com.tw/index/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a
        for i in range(5):
            title = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li['+str(i+1)+']/div/h5/a//text()').extract()
            title = ''.join(title)
            print(title)
            link = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li['+str(i+1)+']/div/h5/a//@href').extract()
            link = ''.join(link)
            link = 'http:'+link
            print(link)
            price = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li['+str(i+1)+']/div/h6/strong/a//text()').extract()
            price = ''.join(price)
            print(price)



print('test')
