from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from datetime import datetime, timedelta


from .models import Educator
from .models import Presentation
from .models import Meeting
from .models import Training
from .models import Event

# Create your views here.
def index(request):
	educator_list = Educator.objects.filter(active=True).order_by('first_name')
	last_week_presentations = Presentation.objects.filter(date__gte=datetime.now()-timedelta(days=7)).filter(date__lte=datetime.now()).order_by('date')
	next_week_presentations = Presentation.objects.filter(date__lte=datetime.now()+timedelta(days=7)).filter(date__gte=datetime.now()).order_by('date')
	last_week_trainings = Training.objects.filter(date__gte=datetime.now()-timedelta(days=7)).filter(date__lte=datetime.now()).order_by('date')
	next_week_trainings = Training.objects.filter(date__lte=datetime.now()+timedelta(days=7)).filter(date__gte=datetime.now()).order_by('date')
	template = loader.get_template('pleasure_app/index.html')
	context = {
		'educator_list':educator_list,
		'next_week_presentations':next_week_presentations,
		'last_week_presentations':last_week_presentations,
		'last_week_trainings':last_week_trainings,
		'next_week_trainings':next_week_trainings,
	}
	return HttpResponse(template.render(context, request))

def scheduling(request):
	educator_list = Educator.objects.filter(active=True).order_by('first_name')
	presentation_list = Presentation.objects.all().order_by('date')
	template = loader.get_template('pleasure_app/scheduling.html')
	context = {
		'educator_list':educator_list,
		'presentation_list':presentation_list,
	}
	return HttpResponse(template.render(context, request))

def update_scheduling(request):
	try:
		presentation = Presentation.objects.get(id=request.POST['pres_id'])
		newed1 = Educator.objects.filter(athena=request.POST['ed1']).first()
		newed2 = Educator.objects.filter(athena=request.POST['ed2']).first()
		newsupp = Educator.objects.filter(athena=request.POST['sup']).first()
		if presentation.educator1 != newed1 and presentation.educator1 != None and newed1 != None:
			return HttpResponse("Overwrite error!")
		elif presentation.educator2 != newed2 and presentation.educator2 != None and newed2 != None:
			return HttpResponse("Overwrite error!")
		elif presentation.supporter != newsupp and presentation.supporter != None and newsupp != None:
			return HttpResponse("Overwrite error!")
		else:
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

def attendance(request):
	educator_list = Educator.objects.filter(active=True).order_by('first_name')
	meeting_list = Meeting.objects.all().order_by('date')
	template = loader.get_template('pleasure_app/attendance.html')
	context = {
		'educator_list':educator_list,
		'meeting_list':meeting_list,
	}
	return HttpResponse(template.render(context, request))

def update_attendance(request):
        try:
		dt = request.POST['datetime']
		datetime = dt[6:10]+'-'+dt[0:2]+'-'+dt[3:5]+' 00:00'
		meeting = Meeting(date=datetime)
		meeting.save()
		attendance_list = request.POST.getlist('attendance[]')
		for ed in attendance_list:
			educator = Educator.objects.filter(athena=ed).first()
			meeting.attendees.add(educator)
                meeting.save()
                #return scheduling(request)
                return HttpResponse("Success! Created new presentation.");
        except Exception as e:
                return HttpResponse("New presentation creation failed! "+str(e));

def training(request):
        educator_list = Educator.objects.filter(active=True).order_by('first_name')
        future_training_list = Training.objects.all().filter(date__gte=timezone.now()).order_by('date')
        past_training_list = Training.objects.all().filter(date__lt=timezone.now()).order_by('date')
	template = loader.get_template('pleasure_app/training.html')
        context = {
                'educator_list':educator_list,
                'future_training_list':future_training_list,
		'past_training_list':past_training_list,
        }
        return HttpResponse(template.render(context, request))

def add_ed_to_training(request):
        try:
         	ed = Educator.objects.filter(athena=request.POST['educator']).first()       
		training = Training.objects.filter(id=request.POST['training_id']).first()
		if training.module == "CUL":
			ed.trained_culture = training
		elif training.module == "VAL":
			ed.trained_values = training
		elif training.module == "ID":
			ed.trained_identity = training
		elif training.module == "LOV":
			ed.trained_love = training
		elif training.module == "COM":
			ed.trained_communication = training
		ed.save()
                return HttpResponse("Success! Added ed to training.");
        except Exception as e:
                return HttpResponse("Error!"+str(e));

def remove_ed_from_training(request):
        try:
                ed = Educator.objects.filter(athena=request.POST['educator']).first()
                training = Training.objects.filter(id=request.POST['training_id']).first()
                if training.module == "CUL":
                        ed.trained_culture = None
                elif training.module == "VAL":
                        ed.trained_values = None
                elif training.module == "ID":
                        ed.trained_identity = None
                elif training.module == "LOV":
                        ed.trained_love = None
                elif training.module == "COM":
                        ed.trained_communication = None
                ed.save()
                return HttpResponse("Success! Removed ed from training.");
        except Exception as e:
                return HttpResponse("Error!"+str(e));

def history(request):
        educator_list = Educator.objects.filter(active=True).order_by('first_name')
        presentation_list = Presentation.objects.filter(date__lte=datetime.now()).order_by('-date')
        training_list = Training.objects.all().filter(date__lte=datetime.now()).order_by('-date')
	template = loader.get_template('pleasure_app/history.html')
        event_list = Event.objects.all().filter(date__lte=datetime.now()).order_by('-date')
	context = {
                'educator_list':educator_list,
                'presentation_list':presentation_list,
        	'training_list':training_list,
		'event_list':event_list,
	}
        return HttpResponse(template.render(context, request))

