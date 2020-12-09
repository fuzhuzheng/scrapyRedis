from scrapy.http import Request
import scrapy
import re
from urllib import parse


class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'
    allowed_domains = ['www.hao123.com']

    def start_requests(self):
        url = 'http://www.hao123.com/'
        while True:
            yield Request(url, dont_filter=True)
            print(33333333)
            pass

    def parse(self, response):
        for a in self.get_a(response):
            # 跳过"javascript"类URL
            # if re.match('^javascript(.*)', url, re.I | re.S) is not None:
            #     continue
            #
            # url = parse.urljoin(response.url, url)
            print(a.attrib.get('href'))
            print(a.attrib.get('title'))
            print(a.root.get('text'))
            print('')
        pass

    def get_urls(self, response):
        return response.xpath("//a/@href").extract()

    def get_a(self, response):
        return response.xpath("//a")
