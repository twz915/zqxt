#coding:utf-8
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from tiy.models import Instance
from urllib import unquote

class Test_TIY_Views(TestCase):
    def test_tiy_home_page(self):
        name = 'tryhtml_intro'
        code = '<html><body><h1>Title</h1><p>paragraph</p></body></html>'

        Instance.objects.create(name=name,code=code)
        r = self.client.get(reverse('tiy',args=(name,)))

        self.assertContains(r, name)

    def test_tiy_post(self):
        #用户提交的内容可以是任意内容，在此模拟
        import random
        code = range(random.choice(range(1,100)), random.choice(range(100,200)))
        random.shuffle(code)
        code = ','.join(map(str, code))

        r = self.client.post(reverse('demo'),{'code':code})
        self.assertEqual(r['X-XSS-Protection'], '0')
        self.assertContains(r, code)

    def test_show_php(self):
        pass

    def test_show_asp(self):
        pass

    def test_show_file(self):
        pass

    def test_tiy_superuser_saveit(self):
        pass

    def test_ajax_database(self):
        r = self.client.get(reverse('ajax-database'),{'q':'APPLE'})
        self.assertContains(r,'table')

    def test_try_color(self):
        r = self.client.get(reverse('try-color'))
        self.assertContains(r, '颜色测试')

    def test_ajax_suggest_no_such_name(self):
        r = self.client.get(reverse('ajax-suggest'), {'q': 'No such name'})
        self.assertContains(r,"Couldn't find!")

    def test_ajax_suggest_normal_name(self):
        r = self.client.get(reverse('ajax-suggest'),{'q':'W'})
        self.assertContains(r,"WeizhongTu")

    def test_demo_get(self):
        r = self.client.get(reverse('demo-get'))
        self.assertContains(r, '服务器当前时间')
    
    def test_demo_get_via_post(self):
        r = self.client.post(reverse('demo-get'))
        self.assertContains(r, '您请求的方法不是GET方法！', status_code=404)

    def test_demo_get2(self):
        r = self.client.get(reverse('demo-get2'), {'fname':'涂','lname':'伟忠'})
        self.assertContains(r, '涂')
        self.assertContains(r, '伟忠')
    
    def test_demo_get2_via_post(self):
        r = self.client.post(reverse('demo-get2'))
        self.assertContains(r, '您请求的方法不是GET方法！', status_code=404)

    def test_ajax_get(self):
        r = self.client.get(reverse('jquery-ajax-get'))
        self.assertContains(r, '这是来自外部PHP文件的一些文本。')
    
    def test_ajax_get_via_post(self):
        r = self.client.post(reverse('jquery-ajax-get'))
        self.assertContains(r, '您请求的方法不是GET方法！', status_code=404)

    def test_ajax_post(self):
        r = self.client.post(reverse('jquery-ajax-post'), {'name':'涂伟忠', 'city': '天津'})
        self.assertContains(r, '涂伟忠')
        self.assertContains(r, '天津')

    def test_ajax_post_via_get(self):
        r = self.client.get(reverse('jquery-ajax-post'), {'name':'涂伟忠', 'city': '天津'})
        self.assertContains(r, '您请求的方法不是POST方法！', status_code=404)

    def test_ajax_post2(self):
        r = self.client.post(reverse('jquery-ajax-post2'), {'fname':'涂','lname':'伟忠'})
        self.assertContains(r, '涂')
        self.assertContains(r, '伟忠')

    def test_ajax_post2_via_get(self):
        r = self.client.get(reverse('jquery-ajax-post2'), {'fname':'涂','lname':'伟忠'})
        self.assertContains(r, '您请求的方法不是POST方法！', status_code=404)

class Test_TIY_models(TestCase):
    pass

