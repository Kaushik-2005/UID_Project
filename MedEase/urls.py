from django.urls import path

from UID_Project import settings

from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('doctorprofile/', views.doctorprofile, name = "doctorprofile"),
    path('index', views.index, name = 'index'),
    path('', views.landingpage, name = 'landingpage'),
    path('viewDoctor/', views.viewDoctor, name = 'viewDoctor'),
    path('cardiologists/', views.cardiologists, name = 'cardiologists'),
    path('orthopaedicians/', views.orthopaedicians, name = 'orthopaedicians'),
    path('neurologists/', views.neurologists, name = 'neurologists'),
    path('dentists/', views.dentists, name = 'dentists'),
    path('ents/', views.ents, name = 'ents'),
    path('pediatricians/', views.pediatricians, name = 'pediatricians'),
    path('appointment/', views.appointment, name='appointment'),
    path('healthstatus/', views.healthstatus, name= 'healthstatus')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)