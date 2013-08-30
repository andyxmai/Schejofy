from django.db import models

# Create your models here.

class User(models.Model):
	STUDENT_YEAR = (
		('Freshman', 	'Freshman'),
		('Sophomore', 'Sophomore'),
		('Junior', 		'Junior'),
		('Senior', 		'Senior'),
		('Graduate', 	'Graduate'),
	)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	year = models.CharField(max_length=10, choices=STUDENT_YEAR)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Course(models.Model):
	name = models.CharField(max_length=100)
	members = models.ManyToManyField(User, through='Membership')

	def __unicode__(self):
		return self.name
	
class Membership(models.Model):
	user   = models.ForeignKey(User)
	course = models.ForeignKey(Course)
	is_shopping = models.BooleanField()

	class Meta:
		unique_together = ["user", "course"]
    