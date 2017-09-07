from django.conf.urls import url 

from .views import ListTeacher, AddTeacher, DetailTeacher, EditTeacher, DeleteTeacher

urlpatterns = [
    url(r'^list/$', ListTeacher.as_view(), name='list'),
    url(r'^add/$', AddTeacher.as_view(), name='add'),
    url(r'^detail/(?P<slug>.*)/$', DetailTeacher.as_view(), name='detail'), 
    url(r'^edit/(?P<slug>.*)/$', EditTeacher.as_view(), name='edit'),
    url(r'^delete/(?P<slug>.*)/$', DeleteTeacher.as_view(), name='delete'), 
]