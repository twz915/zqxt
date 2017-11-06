# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pyquery import PyQuery as pq


class SearchTutorial(object):
    def __init__(self, keyword):
        self.wp = pq(
            url='http://so.ziqiangxuetang.com/cse/search'
            '?s=73600958046581005&q=%s' % keyword, encoding='utf-8')
        print self.wp
        self.results = self.wp('#results .result h3 a')
        if self.results == []:
            self.result_string = (
                '抱歉，没有找到与【%s】相关的结果。请更换其它搜索词再次尝试 '
                '或者 访问<a href="http://www.ziqiangxuetang.com">自强学堂</a>'
                % keyword)
        else:
            result_string_list = []
            for index, r in enumerate(self.results, 1):
                r = pq(r)
                title = r.text().replace(' - 自强学堂', '')
                url = r.attr('href').split('?bd')[0]
                result_string_list.append(
                    '[{0}]. <a href="{2}">{1}</a>'.format(index, title, url))

            self.result_string = "搜索结果如下：\n" + '\n'.join(result_string_list)


def main():
    s = SearchTutorial('Django')
    print s.result_string


if __name__ == '__main__':
    main()
