import requests
import json


# 待预测数据
# text = ["黄片下载,黄片下载,打击黄牛党", "偷拍亚洲另类无码专区AV_恸哭の女教师大桥未久加勒比_唐三 胡列娜 用力 啊 乳",
#         "欧美日韩专区无码人妻在线,国产电影一卡二卡三卡四卡,亚洲深深色噜噜狠狠爱网站,中国农村妇女下身毛茸茸"]
#
# # 设置运行配置
#
# # 指定预测方法为porn_detection_lstm并发送post请求，content-type类型应指定json方式
# # HOST_IP为服务器IP
# url = "http://172.18.1.2:8866/predict/porn_detection_lstm"
#
# headers = {"Content-Type": "application/json"}
# # 对应本地预测porn_detection_lstm.detection(texts=text, batch_size=1, use_gpu=True)
# data = {"texts": text, "batch_size": 1, "use_gpu": True}
# results = requests.post(url=url, headers=headers, data=json.dumps(data))
#
# # 打印预测结果
# print(json.dumps(results.json(), indent=4, ensure_ascii=False))


def check_porn(text=''):
    texts = []
    length = len(text)

    start = 0
    stup_len = 8

    while start < length:
        texts.append(text[start:start+stup_len])
        start += int(stup_len / 2)

    url = "http://172.18.1.2:8866/predict/porn_detection_lstm"

    headers = {"Content-Type": "application/json"}

    # 对应本地预测porn_detection_lstm.detection(texts=text, batch_size=1, use_gpu=True)
    data = {"texts": texts, "batch_size": 1, "use_gpu": True}

    response = requests.post(url=url, headers=headers, data=json.dumps(data)).json()

    if response['status'] == '000':
        for result in response['results']:
            if result['porn_detection_label'] == 1:
                return 1

    return 0
    print(json.dumps(response, indent=4, ensure_ascii=False))
    # return response['results'][0]['porn_detection_label'] if response['status'] == '000' else 'err'


check_porn('香港经典三级影片 - 韩国、日本、国产三级电影 - 三级片大全 - 三级MP4网_日本wvvw在线中文字幕,日本wvvw高清中文字幕,日本wvvw中文字幕在线观看_中文字幕av高清片_中文字幕第一页_中文字幕乱近親相姦')

