from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from MedEase.models import Doctor
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method=="POST":
        cardimg = request.FILES.get('image')  # 'image' corresponds to the input field name
        new_doctor = Doctor(
            cardname= request.POST.get('docname') + " " +request.POST.get('doclname'),
            cardimg=cardimg,  # Replace with actual image path
            cardprofession=request.POST.get('expertise'),
            infoimg=cardimg,  # Replace with actual image path
            infoname=request.POST.get('docname'),
            infoprofession=request.POST.get('education'),
            infolocation=request.POST.get('location'),
            infomail=request.POST.get('email'),
            infophone=request.POST.get('phone'),
            doctype=request.POST.get('doctype'),
        )

        username = request.POST.get('docname')
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            messages.info(request,'email exists..!')
            return redirect('doctorprofile')

        elif User.objects.filter(username=username).exists():
            messages.info(request,'username exists..!')
            return redirect('doctorprofile')

        else:
            user = User.objects.create_user(username=username, email=email, password='1234')
            user.save()
            new_doctor.save()
            userDoc = auth.authenticate(username=username, password='1234')
            auth.login(request, userDoc)
            return redirect('/index')
    else:
        return render(request, 'index.html')

def healthstatus(request):
    return render(request, 'healthstatus.html')

def doctorprofile(request):
    return render(request, 'doctorprofile.html')


def viewDoctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'viewDoctor.html',{'doctors' : doctors})


def cardiologists(request):
    doctors = Doctor.objects.all()
    Cardios = []
    for doc in doctors :
        if doc.doctype=='Cardiologist':
            Cardios.append(doc)
    return render(request, 'viewDoctor.html',{'doctors' : Cardios})
def orthopaedicians(request):
    doctors = Doctor.objects.all()
    orthos = []
    for doc in doctors :
        if doc.doctype=='Orthopedician':
            orthos.append(doc)
    return render(request, 'viewDoctor.html',{'doctors' : orthos})
def neurologists(request):
    doctors = Doctor.objects.all()
    neuros = []
    for doc in doctors :
        if doc.doctype=='Neurologist':
            neuros.append(doc)
    return render(request, 'viewDoctor.html',{'doctors' : neuros})
def ents(request):
    doctors = Doctor.objects.all()
    ent = []
    for doc in doctors :
        if doc.doctype=='ENT_Doctor':
            ent.append(doc)
    return render(request, 'viewDoctor.html',{'doctors' : ent})

def pediatricians(request):
    doctors = Doctor.objects.all()
    pedis = []
    for doc in doctors :
        if doc.doctype=='Pediatrician':
            pedis.append(doc)
    return render(request, 'viewDoctor.html',{'doctors' : pedis})
def dentists(request):
    doctors = Doctor.objects.all()
    dents = []
    for doc in doctors :
        if doc.doctype=='Dentist':
            dents.append(doc)
    return render(request, 'viewDoctor.html',{'doctors' : dents})

def appointment(request):
    doctorname = request.GET.get('doc')
    return render(request, 'appointment.html', {'docname' : doctorname})

def landingpage(request):
    return render(request, 'landingpage.html')