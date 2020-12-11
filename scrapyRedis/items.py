# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyRedisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UrlItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()


class PageItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()
    referer = scrapy.Field()
    template = scrapy.Field()


