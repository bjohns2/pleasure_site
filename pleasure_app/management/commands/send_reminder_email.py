from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
from django.core.mail import send_mail

from pleasure_app.models import Educator
from pleasure_app.models import Presentation
from pleasure_app.models import Meeting
from pleasure_app.models import Training
from pleasure_app.models import Event

class Command(BaseCommand):
    help = 'Send an email'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)
    #
    #def handle(self, *args, **options):
    #    for poll_id in options['poll_id']:
    #        try:
    #            poll = Poll.objects.get(pk=poll_id)
    #        except Poll.DoesNotExist:
    #            raise CommandError('Poll "%s" does not exist' % poll_id)
    #
    #        poll.opened = False
    #        poll.save()
    #

    def handle(self,*args, **options):
	next_week_presentations = Presentation.objects\
		.filter(date__lte=datetime.now().date()+timedelta(days=8))\
		.filter(date__gte=datetime.now().date()+timedelta(days=7))\
		.order_by('date')
	for p in next_week_presentations:
		ed1 = p.educator1
		ed2 = p.educator2
		sup = p.supporter
		if ed1 != None and ed2 != None and sup != None:
			message = 'Upcoming Event:\n'+str(p)+'\n\n'+ed1.first_name\
				+', please email out to '+p.location+' about the module and reserve a space if necessary. '\
				+ '\n'+ed2.first_name+', please bring the presentation supplies (the script and any other materials needed).'\
				+'\n'+sup.first_name+', please coordinate food for the event with Vienna.'
			recipients_list = ['pleasure-exec@mit.edu',ed1.athena+'@mit.edu',ed2.athena+'@mit.edu',sup.athena+'@mit.edu']
			title = '[Pleasure Reminders] You have an event coming up in 1 week!'
		else:
			message = 'Dear Exec, \nOne or more of the presenter slots for an upcoming event is empty, so I didn\'t send'+ \
                                  ' a reminder email. Please get people signed up for this event and then remind them to pub, bring'+ \
                                  ' materials, and coordinate food. Thanks! \n Event: '+str(p)+'\n <3 Pleasure Reminder Bot'
		        recipients_list = ['pleasure-exec@mit.edu']
			title = '[Pleasure Reminders] Missing presenters for upcoming event!'
		send_mail(
			title,
			message,
                        'noreply@pleasure.mit.edu',
                        recipients_list,
                        fail_silently=False,
                )
	self.stdout.write(self.style.SUCCESS('Successfully emailed someone'))
