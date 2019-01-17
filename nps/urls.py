from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^submit/$', views.submit_answer, name='submit_answer'),
	url(r'^thanks/$', views.thanks, name='thanks')
]