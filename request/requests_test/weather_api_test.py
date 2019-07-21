#Python接口测试——基于天气API

import requests
from urllib import  parse

data={'city':'上海'}
city=parse.urlencode(data).encode('utf-8')
url='https://www.sojson.com/open/api/weather/json.shtml'

"""
原链接为 https://www.sojson.com/open/api/weather/json.shtml？city=上海
新链接为 http://t.weather.sojson.com/api/weather/city/101030100  最后是天津市的cityId
所以原代码已经无法运行，请参考https://www.sojson.com/api/weather.html网页注明
"""

r=requests.get(url,params=city)
print(r.text)
response_data=r.json()

print(response_data['date'])
print(response_data['message'])
print(response_data['status'])
print(response_data['city'])

print(response_data['data']['forecast'][0]['date'])
print(response_data['data']['forecast'][0]['type'])
print(response_data['data']['forecast'][0]['high'])
print(response_data['data']['forecast'][0]['low'])