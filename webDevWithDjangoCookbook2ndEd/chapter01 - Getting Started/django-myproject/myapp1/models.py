# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .app_settings import STATUS_CHOICES

class NewsArticles(models.Model):
    status = models.CharField(_("Status"),
            max_length=20, choices=STATUS_CHOICES
    )