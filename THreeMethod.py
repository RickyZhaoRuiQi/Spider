
import urllib.request
from http import cookiejar

url = 'https://www.baidu.com'

print('方法一')
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('方法二')
request = urllib.request.Request(url)
request.add_header('User-Agent','Mozilla/5.0')
response2 = urllib.request.urlopen(url)
print(response2.getcode())
print(len(response2.read()))

print('方法三')
cj = cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())