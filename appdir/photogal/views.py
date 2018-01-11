from django.shortcuts import render



def main(request):
    return render(request, 'photogal/main.html')

def register(request):
    return render(request, 'photogal/auth/register.html')

def login(request):
    return render(request, 'photogal/auth/login.html')