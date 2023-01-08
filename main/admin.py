from django.contrib import admin

from main.models import Survey, SurveyResponse

# Register your models here.
admin.site.register(Survey)
admin.site.register(SurveyResponse)