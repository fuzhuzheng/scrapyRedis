import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from redis import StrictRedis
#
redis = StrictRedis(host="172.18.0.2",
                    port=6379,
                    password='83VvZw$*@#NE',
                    db=2,
                    socket_timeout=10,
                    socket_connect_timeout=2,
                    # decode_responses=True
                    )

redis.sadd("mySpider:start_urls", "https://www.hao123.com/")
# redis.sadd("mySpider:start_urls", "https://www.aimitop.com/")

# t = True
# while t:
#     try:
#         (a, b) = redis.blpop("mySpider:items", timeout=10)
#         print(a)
#         print(b)
#     except:
#         t = False
#
# param = redis.spop("mySpider:start_urls")
#
# print(param)
# param = redis.type("mySpider:requests")

# print(param)


# params = redis.smembers("mySpider:start_urls")
# for param in params:
#     # redis.spop("mySpider:start_urls")
#     print(param)

# params = redis.smembers("mySpider:dupefilter")
# for param in range(10000):
#     redis.spop("mySpider:dupefilter")
# print(param)

# params = redis.scard("mySpider:dupefilter")
# params = redis.delete("mySpider:dupefilter")
# params = redis.delete("mySpider:requests")
#
#     # redis.lpop("mySpider:requests")
# print(len(params))
# print(params)

# import json, time
#
# i = 0
# while i < 100:
#     # time.sleep(2)
#     _, data = redis.brpop('dddddddddddd', 3600*36000)
#     data = json.loads(data)
#     print(data)
#
#     i += 1

import json
# data = redis.get(':1:spider_init_settings')
# # data = bytes(data).decode(encoding='utf-8')
# print(data.decode('utf-8'))
#
# keys = redis.keys("*")
#
# print(keys)


