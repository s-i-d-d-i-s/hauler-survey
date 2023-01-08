 
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from main.models import Survey, SurveyResponse
import json

# Create your views here.
def homepage(request):
    return render(request,'main/homepage.html')

@login_required
def dashboard(request):
    responses = SurveyResponse.objects.all()
    return render(request,'main/dashboard.html',{'responses':responses})


def generate_survey_id(N):
    import string
    import random
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

allowed_client_id = ['sd9sdgj120sf12']

@csrf_exempt
def create_survey_form(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        sessionID = request_data['sessionID']
        customerID = request_data['customerID']
        vendorName = request_data['vendorName']
        clientID = request_data['clientID']
        vendorImage = request_data['vendorImage']
        if clientID not in allowed_client_id:
            return HttpResponse('Invalid Client ID')
        while True:
            surveyID = generate_survey_id(5)
            survey = Survey.objects.filter(surveyID=surveyID).all()
            if len(survey) == 0:
                Survey(surveyID=surveyID,
                        sessionID=sessionID,
                        customerID=customerID,
                        vendorName=vendorName,
                        vendorImage=vendorImage).save()
                break
        return HttpResponse(surveyID)
    return HttpResponse("Only POST Request Allowed")


def fill_survey(request,surveyID):
    survey = Survey.objects.filter(surveyID=surveyID).all()
    if len(survey) == 0:
        return HttpResponse("Invalid Survey ID")
    survey = survey.first()
    data = {
        'surveyID': survey.surveyID,
        'sessionID': survey.sessionID,
        'customerID' : survey.customerID,
        'vendorName' : survey.vendorName,
        'vendorImage' : survey.vendorImage,
        'finished': survey.finished
    }
    if request.method == 'POST':
        print(request.POST)
        request_data = request.POST
        didBuy = request_data['didBuy']
        if didBuy == 'yes':
            didBuy = True
        else:
            didBuy = False
        sellerExp = int(request_data['sellerExp'])
        prodExp = int(request_data['prodExp'])
        suggestion = request_data['suggestion']
        exp = SurveyResponse(surveyID = data['surveyID'],
                            sessionID=data['sessionID'],
                            customerID=data['customerID'],
                            didBuy=didBuy,
                            sellerExp=sellerExp,
                            prodQual=prodExp,
                            anyMsg = suggestion)
        exp.save()
        survey.finished=True
        survey.save()
        return redirect('homepage')
    return render(request,'main/surveyForm.html',{'data':data})
