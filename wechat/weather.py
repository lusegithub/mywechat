import json
import requests


def getWeather(city):
    try:
        url = 'http://apis.baidu.com/heweather/weather/free?city=%s' % city
        headers = {'apikey': 'a79124c4594c2e5a0799a39ea8f64c87'}
        # r = requests.get(url, headers=headers).text.encode('latin-1').decode('unicode_escape')
        r = requests.get(url, headers=headers).text
        jsonData = json.loads(r)
        weather = [jsonData['HeWeather data service 3.0'][0]['basic']['city'],
                   jsonData['HeWeather data service 3.0'][0]['now']['cond']['txt'],
                   jsonData['HeWeather data service 3.0'][0]['now']['tmp'],
                   jsonData['HeWeather data service 3.0'][0]['now']['fl'],
                   jsonData['HeWeather data service 3.0'][0]['now']['wind']['dir'],
                   jsonData['HeWeather data service 3.0'][0]['now']['wind']['sc'],
                   jsonData['HeWeather data service 3.0'][0]['suggestion']['drsg']['txt']]
        weather = '''%s，%s，气温%s℃，体感温度%s℃，%s%s级，%s''' % (weather[0], weather[1], weather[2], weather[3], weather[4]
                                                        , weather[5], weather[6])
        return weather
    except:
        return '不好意思,请查看你的城市是否输入正确'
