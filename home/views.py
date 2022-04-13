from django.shortcuts import render
from .models import Person
from django.contrib import messages
from datetime import datetime




def add_form(request):
    if request.method == 'POST':
        if request.POST.get('sender') and request.POST.get('receiver') and request.POST.get('email') and request.POST.get('bday'):
            sender = request.POST['sender']
            receiver = request.POST['receiver']
            email = request.POST['email']
            bday = request.POST['bday']
            year_now = int(datetime.now().strftime("%Y"))-1
            person = Person(
                sender=sender,
                receiver=receiver,
                email=email,
                bday=bday,
                year=year_now
            )
            person.save()
            messages.success(
                    request, "We have successfully added the data on our server.")
            return render(request, "form.html")
        else:
            error = {
                "error": 'One or more fields is missing.'
            }
            return render(request, "form.html", error)
    return render(request, "form.html")