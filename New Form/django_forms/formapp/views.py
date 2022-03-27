from django.shortcuts import render
from django.http import HttpResponse
import time

from .forms import ContactForm , SubmitForm , Ajaxform
from .models import Contact

# Create your views here.
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('VALIDATION SUCCESS!')
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('MESSAGE: ' + form.cleaned_data['message'])
            return HttpResponse(f'Success on contact!<br>Enterd<br>Name:{form.cleaned_data["name"]}<br>Email:{form.cleaned_data["email"]}<br>Message:{form.cleaned_data["message"]} <br> Choise {form.cleaned_data["choise"]}')
    #  to save in db first need to create scheama in models and then save it in admin and then migrate
    
    return render(request, 'form.html', {'form': form})

def crispy_form(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            print('VALIDATION SUCCESS!')
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('MESSAGE: ' + form.cleaned_data['message'])
            print("saving form")
            form.save()  # save to database mentioned in models.py
            return HttpResponse(f'Successon  post_form!<br>Enterd<br>Name:{form.cleaned_data["name"]}<br>Email:{form.cleaned_data["email"]}<br>Message:{form.cleaned_data["message"]}')
    print("******************************** GET")
    form = SubmitForm()
    return render(request, 'form_crispy.html', {'form': form})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt        
def pro(request , data):
    data = data[6:]
    current_time = time.strftime("%H:%M:%S")
    # return HttpResponse(f'<h1>{current_time }</h1><p>Dats is : {data}</p>')
    if data == "rahul":
        return HttpResponse(f'true')
    else:
        return HttpResponse(f'false')
    


# def contact(request):
#     return HttpResponse('This website is working properly')