# -*- coding: utf-8 -*-
from os.path import dirname, abspath
import os
import re
from datetime import datetime
from fabric.api import *

'''
常用命令:
lcd(dir): 进入本机某目录
local(cmd): 本机上执行命令
cd(dir): 进入服务器某目录
run(cmd):服务器上执行命令
'''
# 服务器列表
#env.hosts = ['user@server1','user2@server2']


BASE_DIR = dirname(abspath(__file__))


def compress():
    datetime_json_name = datetime.now().strftime('%Y%m%d_%H%M%S.json')
    reg = re.compile(r'''COMPRESS_OFFLINE_MANIFEST ?= ?(?:'|").+?(?:'|")''')

    with lcd(BASE_DIR):
        with open(os.path.join(BASE_DIR, 'zqxt', 'settings.py'), 'r+') as f:
            content = f.read()
            content = reg.sub(
                r'COMPRESS_OFFLINE_MANIFEST = "%s"' % datetime_json_name,
                content)
            f.seek(0)
            f.truncate()
            f.write(content)

        local('python manage.py compress --force')


def push_only():
    with lcd(BASE_DIR):
        local('git push')


def push():
    compress()
    with lcd(BASE_DIR):
        local('git add -A')
        local('git status')
        local('git commit -m "%s"' % raw_input('input commit reason:'))
        local('git push')
