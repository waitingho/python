
import scrapy

class PCHomeSpider(scrapy.Spider):
    name = "hello02"

    def start_requests(self):
        urls = [
            'http://24h.pchome.com.tw/index/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a
        #for i in range(5):
        titleList = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a//text()').extract()
        strTitle  = ''.join(titleList)
                    #'//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a//text'
        #str_xpath = '//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a//text()'
        #titleList = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a//text()').extract()
        #strTitle = ''.join(titleList)

        #str_xpath = '//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a//@href'
        #urlList = response.xpath(str_xpath)[0].extract()
        #strUrl = ''.join(urlList)

        urlList   = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a//@href')[0].extract()
        strUrl = ''.join(urlList)
        print('\n')
        print(strTitle)
        print(strUrl+'\n')

        self.log('HTML %s loaded' % response.url)
            #print(title)
            #link = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li[1]/div/h5/a//@href').extract()
            #link = ''.join(link)
            #link = 'http:'+link
            #print(link)
            #price = response.xpath('//*[@id="hot_list"]/dl/dd[2]/ul/li['+str(i+1)+']/div/h6/strong/a//text()').extract()
            #price = ''.join(price)
            #print(price)
