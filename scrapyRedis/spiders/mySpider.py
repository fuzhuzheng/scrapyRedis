from scrapy.http import Request, HtmlResponse
import scrapy
from scrapyRedis.items import UrlItem, SitesItem
from scrapy_redis.spiders import RedisSpider
import re
from urllib import parse


# import urlparse


class mySpiderSpider(RedisSpider):
    name = 'mySpider'

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=False)

    def check_contain_chinese(self, check_str):
        if not check_str:
            return True

        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def parse(self, response, **kwargs):
        title = self.get_title(response)

        if not self.check_contain_chinese(title):
            return None

        # 提取页面内容
        yield SitesItem(
            url=response.url,
            title=title,
            keywords=self.get_keywords(response),
            description=self.get_description(response),
        )

        urls = []
        netlocs = []
        # 提取页面A标签链接
        for a in self.get_a(response):

            url = a.xpath('@href').get()

            # 跳过"javascript"类URL
            if url is None or re.match('(^javascript|^#)(.*)', url, re.I | re.S) is not None:
                continue

            url = parse.urljoin(response.url, url)
            url = parse.urlparse(url)

            if url.netloc in netlocs or url.scheme not in ['http', 'https']:
                continue
            netlocs.append(url.netloc)

            url = '%s://%s/' % (url.scheme, url.netloc.strip())
            urls.append(url)

        for url in urls:
            yield self.make_requests_from_url(url)

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
