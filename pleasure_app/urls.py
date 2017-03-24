from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index',views.index,name='index'),
	url(r'^scheduling', views.scheduling, name='scheduling'),
	url(r'^update_scheduling', views.update_scheduling, name='update_scheduling'),
	url(r'^new_presentation',views.new_presentation,name='new_presentation'),
	url(r'^attendance',views.attendance,name='attendance'),
	url(r'^update_attendance',views.update_attendance,name='update_attendance'),
	url(r'^training',views.training,name='training'),
	url(r'^add_ed_to_training',views.add_ed_to_training,name='add_ed_to_training'),
	url(r'^remove_ed_from_training',views.remove_ed_from_training,name='remove_ed_from_training'),
	url(r'^history',views.history,name='history'),
	url(r'^resources',views.resources,name='resources'),
        #url('^register/', CreateView.as_view(
        #    template_name='pleasure_app/register.html',
        #    form_class=UserCreationForm,
        #    success_url='/'
        #)),
        #url('^accounts/', include('django.contrib.auth.urls')),
]




