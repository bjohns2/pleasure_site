from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Educator
from .models import Presentation

# Create your views here.
def index(request):
	educator_list = Educator.objects.all()
	template = loader.get_template('pleasure_app/index.html')
	context = {
		'educator_list':educator_list,
	}
	return HttpResponse(template.render(context, request))

def scheduling(request):
	educator_list = Educator.objects.all()
	presentation_list = Presentation.objects.all()
	template = loader.get_template('pleasure_app/scheduling.html')
	context = {
		'educator_list':educator_list,
		'presentation_list':presentation_list,
	}
	return HttpResponse(template.render(context, request))
	


