from urllib import parse

url = 'https://taian.esf.fang.com/loupan/2419164207.htm'
url = parse.urlparse(url)
print('%s://%s/' % (url.scheme, url.netloc))

