# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
from wechat_sdk.context.framework.django import DatabaseContextStore
from zqxt.zhanneisearch import SearchTutorial
import json
import requests

WECHAT_TOKEN = 'zqxt'
AppID = 'xxx'
AppSecret = 'xxx'
TuringURL = 'http://www.tuling123.com/openapi/api?key=xxx&userid=xxx&info='


# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)

@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")


    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')

    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()
    # 利用本次请求中的用户OpenID来初始化上下文对话
    context = DatabaseContextStore(openid=message.source)

    # 关注事件
    if message.type == 'event' or True:
        response = wechat_instance.response_text(
            content = (
                '感谢您的关注！\n回复【功能】两个字查看支持的功能，还可以回复任意内容开始聊天'
                '\n【<a href="http://www.ziqiangxuetang.com">自强学堂手机版</a>】'
                ))
    if isinstance(message, TextMessage):
        step = context.get('step', 1)  # 当前对话次数，如果没有则返回 1
        #last_text = context.get('last_text')  # 上次对话内容

        # 当前会话内容
        content = message.content.strip()
        if content == '功能':
            reply_text = (
                    '目前支持的功能：\n1. 关键词后面加上【教程】两个字可以搜索教程，'
                    '比如回复 "Django 后台教程"\n'
                    '2. 回复任意词语，查天气，陪聊天，讲故事，无所不能！\n'
                    '还有更多功能正在开发中哦 ^_^\n'
                    '【<a href="http://www.ziqiangxuetang.com">自强学堂手机版</a>】'
                )
        elif content.endswith('教程'):
            s = SearchTutorial(content.rsplit('教程', 1)[0])
            reply_text = s.result_string
        else:
            r = requests.get(TuringURL+content)
            result = json.loads(r.content)
            reply_text = result.get('text', '').replace('图灵', '小强'
                ).replace('<br>', '') + result.get('url', '')

            if step == 1:
                reply_text += ('\nTIPS: 回复【功能】两个字查看支持的功能!'
                    ' <a href="http://www.ziqiangxuetang.com">自强学堂</a>')

        # 将新的数据存入上下文对话中
        context['step'] = step + 1
        context['last_text'] = content
        context.save()  # 非常重要！请勿忘记！临时数据保存入数据库！

        response = wechat_instance.response_text(content=reply_text)

    return HttpResponse(response, content_type="application/xml")
