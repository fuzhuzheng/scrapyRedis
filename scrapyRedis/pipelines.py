# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy_redis.pipelines import RedisPipeline


class ScrapyRedisPipeline(RedisPipeline):

    def _process_item(self, item, spider):
        print(item)
        pass
    # def process_item(self, item, spider):
    #
    #
    #     return item
