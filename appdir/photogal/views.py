from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Category, Picture, Tag
from .forms import UploadPictureForm
from .forms import RegisterForm

def main(request):
    categories = Category.objects.order_by('category_name')


    context = {'categories' : categories}
    return render(request, 'photogal/main.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')
    else:
        form = RegisterForm()

        context = {'form': form}
        return render(request, 'registration/register.html', context)

def photos(request):
    pics = Picture.objects.all()

    context = {'pics':pics}
    return render(request, 'photogal/photos.html', context)

def category_view(request, category_name):
    category_pics = Picture.objects.filter(category__category_name__exact=str(category_name))
    for pic in category_pics:
        pic.pic_tags = pic.tags.all()

    context = {
        'category_pics': category_pics, 'category_name': str(category_name),
        }
    return render(request, 'photogal/category_photos.html', context)

def tag_view(request, tag_name):
    tag_pics = Picture.objects.filter(tags__tag_name__iexact=str(tag_name))

    context = {'tag_pics':tag_pics, 'tag_name': str(tag_name)}
    return render(request, 'photogal/tag_photos.html', context)

def upload_view(request):
    if request.method == 'POST':
        form = UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UploadPictureForm()

        context = {'form': form}
        return render(request, 'photogal/upload_photo.html', context)

from django.contrib.auth import logout
