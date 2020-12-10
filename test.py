from redis import StrictRedis

redis = StrictRedis(host="172.18.0.2",
                    port=6379,
                    password='83VvZw$*@#NE',
                    db=2,
                    socket_timeout=10,
                    socket_connect_timeout=2,
                    decode_responses=True)

redis.lpush("mySpider:start_urls", "https://www.hao123.com")
# t = True
# while t:
#     try:
#         (a, b) = redis.blpop("mySpider:items", timeout=10)
#         print(a)
#         print(b)
#     except:
#         t = False
#
# param = redis.llen("87zn:items")
#
# print(param)
#
keys = redis.keys("*")

print(keys)
