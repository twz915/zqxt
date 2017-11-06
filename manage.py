#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BAE: export PYTHONPATH=$PYTHONPATH:/home/bae/app/deps
'''
wget -b --mirror -p --convert-links -P ./ http://www.w3schools.com/

创建数据库 `zqxt` 步骤
mysql -u root -p
DROP DATABASE zqxt;

CREATE DATABASE `zqxt` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use zqxt;
GRANT ALL PRIVILEGES ON zqxt.* TO "tu"@"localhost" IDENTIFIED BY "199110050";
source /Users/tu/Downloads/zqnew.sql;
FLUSH PRIVILEGES;
EXIT;
'''

import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zqxt.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
