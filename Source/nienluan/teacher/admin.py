# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Teacher, Work_assignment

admin.site.register(Teacher)
admin.site.register(Work_assignment)

