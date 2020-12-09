import scrapy


class Myspider1Spider(scrapy.Spider):
    name = 'mySpider1'
    allowed_domains = ['www.hao123.com']
    start_urls = ['http://www.hao123.com/']

    def parse(self, response):
        pass
