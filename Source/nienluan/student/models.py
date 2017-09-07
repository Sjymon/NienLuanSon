# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models, IntegrityError, transaction
from django.template.defaultfilters import slugify
from django.urls import reverse

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from class_manage.models import Class

class Contacts(models.Model):
	email		= models.CharField(unique=True, blank=True, max_length=255)
	phone 		= models.CharField(blank=True, max_length=15)

	class Meta:
		abstract = True

class Address(models.Model):
	address_no 		= models.CharField(blank=True, max_length=255)
	address_street 	= models.CharField(blank=True, max_length=255)
	address_ward 	= models.CharField(blank=True, max_length=255)
	address_district= models.CharField(blank=True, max_length=255)
	address_city 	= models.CharField(blank=True, max_length=255)

	class Meta:
		abstract = True 

class People(Contacts, Address):
	first_name 	= models.CharField(max_length=50)
	last_name 	= models.CharField(max_length=50)
	sex 		= models.IntegerField(default=0)
	birthday 	= models.DateField(blank=True)
	birtplace 	= models.CharField(blank=True, max_length=100)
	nation 		= models.CharField(max_length=100)

class ID_Student(People):
	student_id 	= models.CharField(blank=True, max_length=10)

class Student(ID_Student):
	note		= models.TextField(blank=True)
	name_class 	= models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_plus')
	active 		= models.BooleanField(default=True)
	slug 		= models.SlugField(unique=True, blank=True)

	# def student_id(self):
	# 	now = datetime.datetime.now()
	# 	year = str(now.year)
	# 	year = year[2:]
	# 	std_id = '%s%s%05d' % ('B', year, self.id)
	# 	return std_id

	def _get_unique_slug(self):
		slug = slugify(self.first_name+self.last_name)
		unique_slug = slug
		num = 0
		while Student.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug,num)
			num += 1
		return unique_slug

	# def save(self, *args, **kwargs):
	# 	if not self.slug:
	# 		self.slug = self._get_unique_slug()
	# 	# self = super(f).save(*args, **kwargs)
	# 	# self.student_id:
	# 	# self.student_id = Student.id
	# 	# self.save()
	# 	# res = super(Student, self).save(*args, **kwargs)
	# 	# print self.id

	# 	# self.student_id = "CaI"
	# 	# while True:
	# 	# 	try: 
	# 	# 		savepoint = transaction.savepoint()
	# 	# 		res = super(Student, self).save(*args, **kwargs)

	# 	# 		transaction.savepoint_commit(savepoint)
	# 	# 		# now = datetime.datetime.now()
	# 	# 		# year = str(now.year)
	# 	# 		# year = year[2:]
	# 	# 		# std_id = '%s%s%05d' % ('B', year, self.id)
	# 	# 		# self.student_id = std_id

	# 	# 		# print self.student_id

	# 	# 		# if (self.student_id ):
	# 	# 		return res
	# 	# 	except IntegrityError:
	# 	# 		transaction.savepoint_rollback(savepoint)
	# 	# 		now = datetime.datetime.now()
	# 	# 		year = str(now.year)
	# 	# 		year = year[2:]
	# 	# 		# print self.id
	# 	# 		std_id = '%s%s%05d' % ('B', year, self.id)
	# 	# 		self.student_id = std_id
	# 	# return super(Student, self).save(*args, **kwargs)
	# 	return super(Student, self).save(self, *args, **kwargs)

	# def save(self, *args, **kwargs):
	# 	self.slug = slug = slugify(self.first_name+self.last_name)
	# 	i = 0
	# 	while True:
	# 		try:
	# 			savepoint = transaction.savepoint()
	# 			res = super(Student, self).save(*args, **kwargs)
	# 			transaction.savepoint_commit(savepoint)
	# 			return res
	# 		except IntegrityError:
	# 			transaction.savepoint_rollback(savepoint)
	# 			i += 1
	# 			self.slug = '%s_%d' % (slug, i)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	def get_absolute_url(self):
		return reverse('student:detail', kwargs={'slug': self.slug})
		
	def get_update_url(self):
		return reverse('student:edit', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('student:delete', kwargs={'slug': self.slug})


@receiver(pre_save, sender=Student, dispatch_uid="create_student_slug")
def create_student_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = instance._get_unique_slug()

@receiver(post_save, sender=Student, dispatch_uid="create_student_id")
def create_student_id(sender, instance, created, **kwargs):
	now = datetime.datetime.now()
	year = str(now.year)
	year = year[2:]
	std_id = '%s%s%05d' % ('B', year, instance.id)
	instance.id_student.student_id = std_id
	# ID_Student.student_id = std_id
	instance.id_student.save()
	# ID_Student.save()
	# instance.note = "Cai j cung duowc"
	# ipn_obj = sender
	# print ipn_obj
	# instance.student.save()
	# instance.save(update_fields=['student_id'])
	# instance.update()
	# instance.objects.filter(student_id=std_id).update()
	# print('Saved: {}'.format(kwargs['instance'].__dict__))
	# instance.save()
	# instance.student.save()
	# instance.student.save()
	# return instance.student_id
