# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

choices_term = (
	(1, 1),
	(2, 2),
	(3, 3),
)

class Term_year(models.Model):
	term 	= models.IntegerField(default=1, choices=choices_term)
	year 	= models.CharField(max_length=9, unique=True)

	def __unicode__(self):
		return str(self.term) + " - " + self.year

class Class(models.Model):
	class_name		= models.CharField(max_length=20, unique=True)
	term_year 		= models.ForeignKey(Term_year, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.class_name