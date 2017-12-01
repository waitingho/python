import scrapy


from hello05.items import Hello05Item

class PCHomeSpider(scrapy.Spider):
    name = "hello05"

    def start_requests(self):
        urls = [
            'http://24h.pchome.com.tw/index/',
          ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        item = Hello05Item()

        for i  in range(1,6):
            str_idx   = ''+('%s'%i)
            str_xpath = '//*[@id="hot_list"]/dl/dd[2]/ul/li['+str_idx+']/div/h5/a//text()'
            titleList = response.xpath(str_xpath).extract()
            strTitle  = ''.join(titleList)
            str_xpath = '//*[@id="hot_list"]/dl/dd[2]/ul/li['+str_idx+']/div/h5/a//@href'
            urlList   = response.xpath(str_xpath)[0].extract()
            strUrl    = ''.join(urlList)

            str_xpath = '//*[@id="hot_list"]/dl/dd[2]/ul/li['+str_idx+']/div/h6/strong/a//text()'
            priceList = response.xpath(str_xpath).extract()
            strPrice = ''.join(priceList)

            item['title'] = strTitle
            item['link']  = strUrl
            item['price'] = strPrice
            yield item