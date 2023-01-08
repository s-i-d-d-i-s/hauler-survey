from email.policy import default
from django.db import models

# Create your models here.
class Survey(models.Model):
	surveyID = models.CharField(max_length=255,default='')
	sessionID = models.CharField(max_length=255,default='')
	customerID = models.CharField(max_length=255,default='')
	vendorName = models.CharField(max_length=255,default='')
	vendorImage = models.CharField(max_length=255,default='')
	finished = models.BooleanField(default=False)
	
	def __str__(self):
		return f"ID: {self.surveyID}"


class SurveyResponse(models.Model):
	surveyID = models.CharField(max_length=255,default='')
	sessionID = models.CharField(max_length=255,default='')
	customerID = models.CharField(max_length=255,default='')
	didBuy = models.IntegerField(default=-1)
	sellerExp = models.IntegerField(default=-1)
	prodQual = models.IntegerField(default=-1)
	anyMsg = models.TextField(default="")
	
	def __str__(self):
		return f"ID: {self.surveyID}"
