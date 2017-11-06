# -*- coding:utf-8 -*-
# WeizhongTu 2014.05.31
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Tutorial,Column

class TutorialsViews(TestCase):
    def setUp(self):
        # create columns: 
        # `test_column_1` to `test_column_100`
        ColumnList = [ Column(name='test_column_%s'%i, slug='test_column_%s'%i) for i in range(1,101)]
        Column.objects.bulk_create(ColumnList)

        # create tutorials for test_column_1
        c = Column.objects.get(slug='test_column_1')
        Tutorial.objects.create(column=c, title='test tutorial 1', slug='test_index.html')
        Tutorial.objects.create(column=c, title='test tutorial 2', slug='test_2.html')
        Tutorial.objects.create(column=c, title='test tutorial 3', slug='test_3.html')

    def test_index(self):
        r = self.client.get(reverse('index'))
        self.assertTrue('latest_tutorials' in r.context)
        self.assertContains(r, '自强学堂')

    def test_column_redirect_to_first_tutorial(self):
        # test a column has tutorials, will redirect permant
        response = self.client.get(reverse('column', args=('test_column_1',)))
        self.assertRedirects(response, 
            reverse('tutorial-detail', args=('test_column_1', 'test_index.html')),
            status_code=301, target_status_code=200)

    def test_tutorial_basic_url(self):
        import random
        c,t = random.sample(xrange(1000),2)
        self.assertEqual(reverse('tutorial-detail', args=('c%d' % c, 't%d.html' % t,)), '/c%d/t%d.html' % (c, t))
    
    def test_column_and_tutorial_detail(self):
        # when no tutorials in column, return 404, or else return 200
        response = self.client.get(reverse('tutorial-detail',
            args=('test_column_1', 'test_index.html',)))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('tutorial' in response.context)
        #self.assertEqual(response.context['tutorial'].content, u'教程正在编写中……')

    def test_error_tutorial(self):
        # when visit tutorial if give an error column, will redirect to right column
        # no test_index.html in test_column_12, but have one in test_column_1
        response = self.client.get(reverse('tutorial-detail',
            args=('test_column_12', 'test_index.html',)))
        self.assertRedirects(response,
            reverse('tutorial-detail',args=('test_column_1', 'test_index.html')),
            status_code=301, target_status_code=200)

    def test_column_no_tutorial(self):
        # test a column no tutorials
        response = self.client.get(reverse('column', args=('test_column_100',)))
        self.assertEqual(response.status_code,404)

    def test_submit_error_tutorial(self):
        pass

class TutorialsModels(TestCase):
    pass


