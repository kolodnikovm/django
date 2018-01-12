from django.shortcuts import render

from .models import Category, Picture

def main(request):
    categories = Category.objects.order_by('category_name')


    context = {'categories' : categories}
    return render(request, 'photogal/main.html', context)

def register(request):
    return render(request, 'photogal/auth/register.html')

def login(request):
    return render(request, 'photogal/auth/login.html')

def photos(request):
    pics = Picture.objects.all()

    context = {'pics':pics}
    return render(request, 'photogal/photos.html', context)

def category(request, category_name):
    selected_category = Category.objects.get(category_name=category_name)
    category_pics = Picture.objects.filter(category=selected_category)

    context = {'category_pics': category_pics, 'category': selected_category}
    return render(request, 'photogal/category_photos.html', context)