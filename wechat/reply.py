import time
from django.template import Context
from django.template import loader


def replyText(fromUser, toUser, content):
    # 这里获取当前时间的秒数，time.time()取得的数字是浮点数，所以有了下面的操作
    nowtime = str(int(time.time()))

    # 加载text.xml模板t = loader.get_template('wechat/text.xml')
    t = loader.get_template('wechat/text.xml')

    # 将我们的数据组成Context用来render模板
    c = Context({'toUser': toUser, 'fromUser': fromUser,
                 'nowtime': nowtime, 'content': content})
    return t.render(c)