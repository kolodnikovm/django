from django.shortcuts import render

from .models import Category, Picture, Tag

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