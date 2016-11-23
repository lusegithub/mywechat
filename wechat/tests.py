from django.test import TestCase

# Create your tests here.
from wechat.weather import getWeather

if __name__ == '__main__':
    content = '天+广州'
    if content[0:2] == '天气':
        s = getWeather(content[3:])
        print(s)