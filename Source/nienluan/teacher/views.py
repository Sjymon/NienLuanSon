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
from models import Teacher
from . import forms
from forms import TeacherForm

class ListTeacher(ListView):
	model = Teacher
	template_name = 'apps/teacher/list.html'
	def get_context_data(self, **kwargs):
		context = super(ListTeacher, self).get_context_data(**kwargs)
		context['student_list'] = Teacher.objects.all()
		return context

class AddTeacher(CreateView):
	model = Teacher
	form_class = TeacherForm
	template_name = 'apps/teacher/add.html'


class DetailTeacher(DetailView):
	model = Teacher
	template_name = 'apps/teacher/detail.html'

class EditTeacher(UpdateView):
	model = Teacher
	form_class = TeacherForm
	template_name = 'apps/teacher/edit.html'

class DeleteTeacher(DeleteView):
	model = Teacher
	template_name = 'apps/teacher/delete.html'
	success_url = reverse_lazy('teacher:list')
