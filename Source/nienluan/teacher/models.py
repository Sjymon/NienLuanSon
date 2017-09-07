# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from class_manage.models import Class
from student.models import People

class ID_Teacher(People):
	teacher_id 	= models.CharField(max_length=10, blank=True)

class Teacher(ID_Teacher):
	note 	= models.TextField(blank=True)
	active 	= models.BooleanField(default=True)
	slug 	= models.SlugField(unique=True, blank=True)

	def _get_unique_slug(self):
		slug = slugify("teacher-"+self.first_name+self.last_name)
		unique_slug = slug
		num = 0
		while Teacher.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	def get_absolute_url(self):
		return reverse('teacher:detail', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('teacher:edit', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('teacher:delete', kwargs={'slug': self.slug})

class Work_assignment(models.Model):
	class_name 	= models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_teacher_plus')
	teacher 	= models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_plus')

	def __unicode__(self):
		return unicode(self.class_name)

@receiver(pre_save, sender=Teacher, dispatch_uid="create_student_slug")
def create_student_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = instance._get_unique_slug()

@receiver(post_save, sender=Teacher, dispatch_uid="create_teacher_id")
def create_teacher_id(sender, instance, created, **kwargs):
	tea_id = '%s%04d' % ('T', instance.id)
	instance.id_teacher.teacher_id = tea_id
	instance.id_teacher.save()