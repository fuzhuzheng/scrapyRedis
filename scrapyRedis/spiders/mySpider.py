from scrapy.http import Request
import scrapy
from scrapyRedis.items import UrlItem
from scrapy_redis.spiders import RedisSpider
import re
from urllib import parse


class mySpiderSpider(RedisSpider):
    name = 'mySpider'

    def parse(self, response):

        code = response.encoding

        for a in self.get_a(response):
            urls = {}

            url = a.xpath('@href').get()
            title = a.xpath('@title').get()
            text = a.xpath('./text()').get()

            # 跳过"javascript"类URL
            if url is None or re.match('(^javascript|^#)(.*)', url, re.I | re.S) is not None or url in urls:
                continue

            urls.setdefault(url, True)

            url = parse.urljoin(response.url, url)

            yield UrlItem(
                url=url,
                title=title,
                text=text
            )

            # print(3)
            # print(a.get())
        pass

    def get_urls(self, response):
        return response.xpath("//a/@href").extract()

    def get_a(self, response):
        return response.xpath("//a")
