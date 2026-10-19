from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.showPatients, name='patients'),
    path('risk/', views.showRisk, name='risk'),
    path('risk/riskdetail/<int:id>/', views.showRiskDetail, name='riskdetail'),
    path('treatment/', views.showTreatment, name='treatment'),
    path('treatment/treatmentdetail/<int:id>/', views.showTreatmentDetail, name='treatmentdetail'),

]