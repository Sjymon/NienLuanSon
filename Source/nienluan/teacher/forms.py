from django import forms

from .models import Teacher

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = [
			'teacher_id',
			'first_name',
			'last_name',
			'birthday',
			'nation',
			'email',
			'phone',
			'address_city',
		]