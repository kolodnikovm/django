from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegisterForm

def main(request):
    return render(request, 'flickstagram/main.html')

def login(request):
    return render(request, 'flickstagram/auth/login.html')

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('success_reg')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
        context = {'form': form}
    return render(request, 'flickstagram/auth/register.html', context)

def success_reg(request):
    return HttpResponse('GJ')
