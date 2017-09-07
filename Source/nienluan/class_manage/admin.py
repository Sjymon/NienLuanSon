# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Term_year, Class

admin.site.register(Term_year)
admin.site.register(Class)
