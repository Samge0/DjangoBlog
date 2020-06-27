#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: create_testdata.py
@time: 2017/3/11 上午1:58
"""

from django.core.management.base import BaseCommand
from blog.models import Article, Tag, Category
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
import datetime


class Command(BaseCommand):
    help = 'create test datas'

    def handle(self, *args, **options):
        user = get_user_model().objects.get_or_create(
            email='test@test.com', username='测试用户', password='test!q@w#eTYU')[0]

        pcategory = Category.objects.get_or_create(
            name='编程', parent_category=None)[0]

        category = Category.objects.get_or_create(
            name='python', parent_category=pcategory)[0]

        category.save()
        basetag = Tag()
        basetag.name = "标签"
        basetag.save()
        for i in range(1, 20):
            article = Article.objects.get_or_create(
                category=category,
                title='Python3基础知识 ' + str(i),
                body= "线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。" + str(i),
                author=user)[0]
            tag = Tag()
            tag.name = "python" + str(i)
            tag.save()
            article.tags.add(tag)
            article.tags.add(basetag)
            article.save()

        from DjangoBlog.utils import cache
        cache.clear()
        self.stdout.write(self.style.SUCCESS('created test datas \n'))
