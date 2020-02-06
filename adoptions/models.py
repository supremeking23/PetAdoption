from django.db import models
#from django.utils.html import mark_safe

# Create your models here.

class Pet(models.Model):
	SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]

	#for image
	image = models.ImageField(upload_to='images/')

	pet_name = models.CharField(max_length=100)
	submitter = models.CharField(max_length=100)
	species = models.CharField(max_length=30)
	breed = models.CharField(max_length=30, blank = True)

	description = models.TextField()
	sex = models.CharField(choices=SEX_CHOICES, max_length = 1, blank = True)

	submission_date = models.DateTimeField()
	age = models.IntegerField(null=True)
	vaccinations = models.ManyToManyField('Vaccine', blank = True)
	#question = models.ForeignKey(Question, on_delete=models.CASCADE

	def __str__(self):
		return self.pet_name

	#def image_tag(self):
		#return mark_safe('<img src="%s" width="150" height="150" />' % (self.image))

	#image_tag.short_description = 'Image'
	

class Vaccine(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name
