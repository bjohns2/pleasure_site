from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index',views.index,name='index'),
	url(r'^scheduling', views.scheduling, name='scheduling'),
	url(r'^update_scheduling', views.update_scheduling, name='update_scheduling'),
	url(r'^new_presentation',views.new_presentation,name='new_presentation'),
]

