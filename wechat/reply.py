from django.template import Context
from django.template import loader


def replyText(fromUser, toUser, nowtime, content):

    # 加载text.xml模板t = loader.get_template('wechat/text.xml')
    t = loader.get_template('wechat/text.xml')

    # 将我们的数据组成Context用来render模板
    c = Context({'toUser': toUser, 'fromUser': fromUser,
                 'nowtime': nowtime, 'content': content})
    return t.render(c)