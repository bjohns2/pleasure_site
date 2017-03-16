from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Educator(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	training_class = models.CharField(max_length=10)
	graduation_year = models.IntegerField(default=0)
	athena = models.CharField(max_length=20)
	active = models.BooleanField(default=True)

	trained_communication = models.ForeignKey(
		'Training',
		related_name='com_training',
		blank = True,
		null = True,
		limit_choices_to={'module':'COM'},
	)
	trained_values = models.ForeignKey(
                'Training',
        	related_name='val_training', 
		blank = True,
                null = True,
                limit_choices_to={'module':'VAL'},
        )
	trained_identity = models.ForeignKey(
                'Training',
		related_name='id_training',
                blank = True,
                null = True,
                limit_choices_to={'module':'ID'},
        )
	trained_love = models.ForeignKey(
                'Training',
		related_name='lov_training',
                blank = True,
        	null = True,
                limit_choices_to={'module':'LOV'},
        )
	trained_culture = models.ForeignKey(
                'Training',
		related_name='cul_training',
                blank = True,
                null = True,
                limit_choices_to={'module':'CUL'},
        )

	def __str__(self):
		return "Educator " + str(self.first_name) + ' '  + str(self.last_name)

class Training(models.Model):
	MODULE_CHOICE_ENUM = (
		('COM','Communication'),
		('VAL','Values'),
		('ID','Identity'),
		('LOV','Love'),
		('CUL','Culture'),
	)
	module = models.CharField(max_length=3,choices=MODULE_CHOICE_ENUM)
	date = models.DateField()
	notes = models.TextField()

	def __str__(self):
		return "Training: " + str(self.module) + " on " + str(self.date) 

class Presentation(models.Model):
	# TODO: DRY        
	MODULE_CHOICE_ENUM = (
                ('COM','Communication'),
                ('VAL','Values'),
                ('ID','Identity'),
                ('LOV','Love'),
                ('CUL','Culture'),
        )
	location = models.CharField(max_length=200,null=True,blank=True)
	subject = models.CharField(max_length=3,choices=MODULE_CHOICE_ENUM)
	date = models.DateTimeField()
	educator1 = models.ForeignKey(
		'Educator',
		related_name='educator1',
		blank=True,
		null=True,
		# TODO: limit choices so that eds not trained can't sign up
		#limit_choices_to	
	)
	educator2 = models.ForeignKey(
                'Educator',
                related_name='educator2',
                blank=True,
                null=True,
        )
        supporter = models.ForeignKey(
                'Educator',
                related_name='supporter',
                blank=True,
                null=True,
        )
	notes = models.TextField(null=True,blank=True)	
	attendees = models.IntegerField(default=-1)

	def __str__(self):
		return "Presentation at " + str(self.location) + " on " + str(self.subject) + ", " + str(self.date)

class Meeting(models.Model):
	date = models.DateTimeField()
	attendees = models.ManyToManyField(Educator)

	def __str__(self):
		return "Meeting at " + str(self.date) + " with " + str(self.attendees.count()) + " educators"

class Event(models.Model):
	date = models.DateTimeField()
	attendees = models.ManyToManyField(Educator,blank=True)
	location = models.CharField(max_length=200,null=True,blank=True)
	title = models.CharField(max_length=200,null=True,blank=True)
	notes = models.TextField(null=True,blank=True)

	def __str__(self):
		return "Event "+ str(self.title) + " at " + str(self.location) + ", " + str(self.date)
	

