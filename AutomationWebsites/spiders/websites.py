#ICSCERT ALERT SPIDER

import scrapy
from AutomationWebsites.item import WebItem 
class WebScraper (scrapy.Spider):
    name = "webscraper"
    allowed_domain = ["yokogawa.com"]
    start_urls = ["https://www.yokogawa.com/library/resources/white-papers/yokogawa-security-advisory-report-list/"]

    #parsing
    def parse(self,response):
        for sel in response.xpath("//tr/td"):
         item = WebItem()
         item ["alert"] = sel.xpath("///text()").extract()
         item ["vendor"] = sel.xpath("//[@class]/a/text()").extract()       
         yield item

