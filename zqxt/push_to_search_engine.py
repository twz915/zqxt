# -*- coding: utf-8 -*-
# @Date    : 2015-04-09 13:24:50 - 2015-12-19 20:42:50
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
from __future__ import unicode_literals

import requests
import json


def pingbaidu(url):
    site_title = '自强学堂'  # 网站名称
    host_url = 'http://www.ziqiangxuetang.com'  # 网站网址，末尾不要加/
    # 更新的文章链接
    update_url = host_url+url if url.startswith('/') else url
    # 网站rss地址
    rss_url = 'http://www.ziqiangxuetang.com/latest_feed/'

    xml = '''
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
    <methodName>weblogUpdates.extendedPing</methodName>
    <params>
        <param>
            <value><string>%s</string></value>
        </param>
        <param>
            <value><string>%s</string></value>
        </param>
        <param>
            <value><string>%s</string></value>
        </param>
        <param>
            <value><string>%s</string></value>
        </param>
    </params>
</methodCall>''' % (site_title, host_url, update_url, rss_url)

    xml = xml.encode('utf-8')
    headers = {
        'Content-Type': 'text/xml',
        'User-Agent': 'request',
        'Content-Length': len(xml)
    }

    r = requests.post(
        'http://ping.baidu.com/ping/RPC2', data=xml, headers=headers)

    if '<int>0</int>' in r.content:
        return '【ping百度】成功推送到百度！'
    else:
        return '【ping百度】推送到百度失败！'


def submit_link(urls):
    # http://zhanzhang.baidu.com/linksubmit/index?site=http://www.ziqiangxuetang.com/
    if isinstance(urls, (list, tuple, set)):
        urls = '\n'.join(urls)
    headers = {
        'Content-Type': 'text/xml',
        'User-Agent': 'curl/7.12.1',
        'Host': 'data.zz.baidu.com ',
        'Content-Type': 'text/plain',
        'Content-Length': len(urls)
    }

    r = requests.post(
        'http://data.zz.baidu.com/urls?site=www.ziqiangxuetang.com'
        '&token=xxx', data=urls, headers=headers)

    result = json.loads(r.content)
    try:
        result = '【链接提交】成功{success}条, 剩余{remain}条！'.format(**result)
    except KeyError:
        pass
    return result


def submit_sitemap(xml):
    print(xml)
    headers = {
        'Content-Type': 'text/xml',
        'User-Agent': 'request',
        'Content-Length': len(xml)
    }

    r = requests.post(
        'http://ping.baidu.com/sitemap?site=www.ziqiangxuetang.com&'
        'resource_name=RDF_Other_OnlineDocument&access_token=xxx',
        data=xml, headers=headers)

    if '<int>200</int>' in r.content:
        return '【实时推送】成功推送到百度sitemap！'
    else:
        return '【实时推送】推送到百度sitemap失败！'


if __name__ == '__main__':
    print pingbaidu('http://www.ziqiangxuetang.com/django/django-models.html')
