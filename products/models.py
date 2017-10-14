# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    score = models.IntegerField()
    p_name = models.CharField(max_length=500, default='')
    product_name = models.CharField(max_length=500, default='')

    def __unicode__(self):
        return self.p_name
