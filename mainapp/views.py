from django.shortcuts import render,redirect,reverse
from mainapp.models import Skill, idos, About, Contact
from django.contrib import messages
from datetime import datetime
import os
from django.core.mail import send_mail 

# Create your views here.
def genrateData():
    skilldic = {}
    for i in Skill.objects.values():
        skilldic[i["skill"]] = i["level"]
    context = {"skillist": skilldic, "idos": idos.objects.all(
    ), "about": About.objects.values()}
    return context

def Index(request):
    context=genrateData()
    return render(request, "index.html", context=context)

def contactCreate(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        desc = request.POST.get("desc")
        data = Contact(name=name, email=mail, desc=desc, date=datetime.now())
        data.save() 
        try:
            sendContact(name,mail,desc)
            return True
        except Exception as e:
            print(e)
            return False

def Submit(request):
    response=contactCreate(request)
    if response==True:
        messages.success(request,"Contact Request Sended")
    elif response==False:
        messages.error(request,"An error occured. Please Try again")
    return redirect(reverse('index'))
    
def sendContact(name,email,desc):
    mail_subject=f"Contact Request from {name}"
    message=f"""
    Email : {email}\n
    {name} said\n
    {desc}
    """
    send_mail(mail_subject, message, os.environ.get('mail'), ["codewithalvin@gmail.com"],fail_silently=False)
