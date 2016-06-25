from django.conf.urls import patterns,include,url
from appprod.views import *
urlpatterns=[url(r'^$', listarprestadores, name='prestadores'),

]