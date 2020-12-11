from scrapy.http import Request
import scrapy
from scrapyRedis.items import UrlItem, PageItem
from scrapy_redis.spiders import RedisSpider
import re
from urllib import parse


class mySpiderSpider(RedisSpider):
    name = 'mySpider'

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=False)

    def parse(self, response, **kwargs):
        # 提取页面内容
        yield PageItem(
            url=response.url,
            title=self.get_title(response),
            keywords=self.get_keywords(response),
            description=self.get_description(response),
            body=self.get_body(response),
            referer=self.get_referer(response),
            template=''
        )

        # 提取页面A标签链接
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

    def get_a(self, response):
        return response.xpath("//a")

    def get_referer(self, response):
        referer = response.request.headers.get('referer')
        return referer.decode('UTF-8') if referer else ''

    def get_title(self, response):
        """获取标题信息"""
        return response.xpath("//title/text()").get()

    def get_keywords(self, response):
        """信息获取关键字信息"""
        return response.xpath("//meta[@name='keywords']/@content").get()

    def get_description(self, response):
        """获取描述信息"""
        return response.xpath("//meta[@name='dription']/@content").get()

    def get_body(self, response):
        """获取描述信息"""
        return response.xpath("//body").get()
