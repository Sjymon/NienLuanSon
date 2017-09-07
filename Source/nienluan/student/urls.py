from django.conf.urls import url 

from .views import ListStudent, AddStudent, DetailStudent, EditStudent, DeleteStudent

urlpatterns = [
    url(r'^list/$', ListStudent.as_view(), name='list'),
    url(r'^add/$', AddStudent.as_view(), name='add'),
    url(r'^detail/(?P<slug>.*)/$', DetailStudent.as_view(), name='detail'), 
    url(r'^edit/(?P<slug>.*)/$', EditStudent.as_view(), name='edit'),
    url(r'^delete/(?P<slug>.*)/$', DeleteStudent.as_view(), name='delete'), 
]