from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Educator

# Create your views here.
def index(request):
	educator_list = Educator.objects.all()
	template = loader.get_template('pleasure_app/index.html')
	context = {
		'educator_list':educator_list,
	}
	return HttpResponse(template.render(context, request))


