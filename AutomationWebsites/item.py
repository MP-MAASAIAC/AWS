#ICSCERT ITEM FILE

import scrapy
from scrapy.item import Item,Field
class WebItem(scrapy.Item):
    alert = scrapy.Field()
    vendor = scrapy.Field()
    pass