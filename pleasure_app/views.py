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

def update_scheduling(request):
	try:
		presentation = Presentation.objects.get(id=request.POST['pres_id'])
		presentation.educator1 = Educator.objects.filter(athena=request.POST['ed1']).first()
		presentation.educator2 = Educator.objects.filter(athena=request.POST['ed2']).first()
		presentation.supporter = Educator.objects.filter(athena=request.POST['sup']).first()
		presentation.save()
		response = {
			'status' : 1,
			'message' : 'Updated!'
		}
		return HttpResponse("Succesfully updated!");
	except Exception as e:
		return HttpResponse("Update failed! "+str(e));

def new_presentation(request):
	try:
		presentation = Presentation(
			location=request.POST['location'],
			subject=request.POST['module'],
			date=request.POST['date'],
	                #educator1 = Educator.objects.filter(athena=request.POST['ed1']).first(),
                	#educator2 = Educator.objects.filter(athena=request.POST['ed2']).first(),
                	#supporter = Educator.objects.filter(athena=request.POST['sup']).first(),
			notes=request.POST['notes']
		)
		presentation.save()
		return scheduling(request)
		#return HttpResponse("Succesfully created a new presentation!");
	except Exception as e:
		return HttpResponse("New presentation creation failed! "+str(e));

