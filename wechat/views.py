import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from xml.etree import ElementTree as ET
import hashlib

from wechat.joke import getjoke
from wechat.reply import replyText


class WeChat(View):
    # 这里我当时写成了防止跨站请求伪造，其实不是这样的，恰恰相反。因为django默认是开启了csrf防护中间件的
    # 所以这里使用@csrf_exempt是单独为这个函数去掉这个防护功能。
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(WeChat, self).dispatch(*args, **kwargs)

    def get(self, request):
        # 下面这四个参数是在接入时，微信的服务器发送过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        # 这个token是我们自己来定义的，并且这个要填写在开发文档中的Token的位置
        token = 'cjkDoWhatILove'

        # 把token，timestamp, nonce放在一个序列中，并且按字符排序
        hashlist = [token, timestamp, nonce]
        hashlist.sort()

        # 将上面的序列合成一个字符串
        hashstr = ''.join([s for s in hashlist])

        hashstr = hashstr.encode('utf-8')

        # 通过python标准库中的sha1加密算法，处理上面的字符串，形成新的字符串。
        hashstr = hashlib.sha1(hashstr).hexdigest()

        # 把我们生成的字符串和微信服务器发送过来的字符串比较，
        # 如果相同，就把服务器发过来的echostr字符串返回去
        if hashstr == signature:
            return HttpResponse(echostr)

    def post(self, request):
        # 通过xml.etree.ElementTree.fromstring将接收到数据字符串转成xml
        str_xml = ET.fromstring(request.body)

        # 从xml中读取我们需要的数据。注意这里使用了from接收的to，使用to接收了from，
        # 这是因为一会我们还要用这些数据来返回消息，这样一会使用看起来更符合逻辑关系
        fromUser = str_xml.find('ToUserName').text
        toUser = str_xml.find('FromUserName').text
        msgType = str_xml.findtext("MsgType")

        if msgType == 'event':
            event = str_xml.findtext("Event")
            if event == 'subscribe':
                content = '''啦啦啦～谢谢你来关注我！我能做什么：\n
                回复段子：我给你讲个段子！'''

                r = replyText(fromUser, toUser, content)
        elif msgType == 'text':
            content = str_xml.find('Content').text
            if content == '段子':
                jokes = getjoke()
                index = random.randint(0, len(jokes) - 1)
                replyContent = jokes[index]
                r = replyText(fromUser, toUser, replyContent)

            else:
                replycontent = '其他功能正在努力开发中'

                r = replyText(fromUser, toUser, replycontent)
        else:
            return ''

        return HttpResponse(r)
