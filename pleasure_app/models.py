from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Educator(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	training_class = models.CharField(max_length=10)
	graduation_year = models.IntegerField(default=0)

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
	subject = models.CharField(max_length=200)
	date = models.DateField()
	educators = models.ManyToManyField(Educator)
	notes = models.TextField()	

	def __str__(self):
		return "Presentation: " + str(self.subject) + " on " + str(self.date)



