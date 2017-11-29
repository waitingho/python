import scrapy
import time

from Mobile01.items import Mobile01Item
 
class Mobile01(scrapy.Spider):
    name = "Mobile01"
    #scrapy crawl Mobile01 -a c=16 -a p=1
    def __init__(self, c='16', p='1', *args, **kwargs):
        super(Mobile01, self).__init__(*args, **kwargs)
        self.c = c
        self.p = p
        
    def start_requests(self):
        urls = []
        c = self.c
        for i in range(1,int(self.p)+1):
            str_idx = ''+('%s' % i)
            tmp = 'https://www.mobile01.com/forumtopic.php?c=%s&p=%s' % (c,str_idx) 
            urls.append(tmp.strip())

        for url in urls:
            print (url)
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        item = Mobile01Item()
        #//*[@id="maincontent"]/div[6]/table/tbody/tr[1]
        str_xpath = '//*[@id="maincontent"]/div[6]/table/tbody/tr'
        count = len(response.xpath(str_xpath))
        for i in range(1,count+1):
            str_idx = ''+('%s' % i)
            str_xpath = '//*[@id="maincontent"]/div[6]/table/tbody/tr['+str_idx+']/td[1]/span/a//text()'
            titleList = response.xpath(str_xpath).extract()
            strTitle = ''.join(titleList)
            str_xpath = '//*[@id="maincontent"]/div[6]/table/tbody/tr['+str_idx+']/td[1]/span/a//@href'
            urlList = response.xpath(str_xpath)[0].extract()
            strUrl = ''.join(urlList)
            strUrl = 'https://www.mobile01.com/'+strUrl
            item['title'] = strTitle
            item['link'] = strUrl
            yield item
        
        self.log('HTML %s loaded' % response.url)
