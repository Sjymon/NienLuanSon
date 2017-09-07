# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.base import TemplateView

from . import models
from models import Student
from . import forms
from forms import StudentForm

class ListStudent(ListView):
	model = Student
	template_name = 'apps/student/list.html'
	def get_context_data(self, **kwargs):
		context = super(ListStudent, self).get_context_data(**kwargs)
		context['student_list'] = Student.objects.all()
		return context

class AddStudent(CreateView):
	model = Student
	form_class = StudentForm
	template_name = 'apps/student/add.html'


class DetailStudent(DetailView):
	model = Student
	template_name = 'apps/student/detail.html'

class EditStudent(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'apps/student/edit.html'

class DeleteStudent(DeleteView):
	model = Student
	template_name = 'apps/student/delete.html'
	success_url = reverse_lazy('student:list')
