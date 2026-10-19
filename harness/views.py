from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Patient
from .services import DeepSeekService

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def showPatients(request):
    mydata = Patient.objects.all()
    template = loader.get_template('patients.html')
    context = {
        'mypatients' : mydata,
    }
    return HttpResponse(template.render(context, request))

def showRisk(request):
    mydata = Patient.objects.all()
    template = loader.get_template('risk.html')
    context = {
        'mypatients' : mydata,
    }
    return HttpResponse(template.render(context, request))

def showTreatment(request):
    mydata = Patient.objects.all()
    template = loader.get_template('treatment.html')
    context = {
        'mypatients' : mydata,
    }
    return HttpResponse(template.render(context, request))

def showRiskDetail(request, id):
    mydata = Patient.objects.get(id=id)
    llm_service = DeepSeekService()
    proposed_risk = llm_service.getRisk(mydata)
    template = loader.get_template('riskdetail.html')
    context = {
        'mypatients' : mydata,
        'patient_risk' : proposed_risk,
    }
    return HttpResponse(template.render(context, request))

def showTreatmentDetail(request, id):
    mydata = Patient.objects.get(id=id)
    llm_service = DeepSeekService()
    proposed_treatment = llm_service.getTreatment(mydata)
    template = loader.get_template('treatmentdetail.html')
    context = {
        'mypatients' : mydata,
        'patient_treatment' : proposed_treatment,
    }
    return HttpResponse(template.render(context, request))
