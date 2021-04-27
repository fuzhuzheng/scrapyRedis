# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy_redis.pipelines import RedisPipeline
import json


class ScrapyRedisPipeline(RedisPipeline):

    def process_item(self, item, spider):
        data = {
            'url': item['url'],
            'title': item['title'],
            'keywords': item['keywords'],
            'description': item['description'],
        }
        spider.server.lpush('dddddddddddd', json.dumps(data))
        return item
