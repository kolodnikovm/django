from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import RegisterForm, UploadPictureForm
from .helpers import group_required
from .models import Category, Picture


class Main(ListView):
    model = Category
    template_name = 'photogal/main.html'
    context_object_name = 'all_categories'


class Register(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class PicturesByCategory(ListView):
    template_name = 'photogal/category_photos.html'
    context_object_name = 'pictures'

    def get_queryset(self):
        return Picture.objects. \
            filter(category__name__iexact=self.kwargs['category_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs['category_name']
        return context


class PicturesByTag(ListView):
    template_name = 'photogal/tag_photos.html'
    context_object_name = 'pictures'

    def get_queryset(self):
        return Picture.objects. \
            filter(tags__name__iexact=self.kwargs['tag_name'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name']
        return context


class UploadView(FormView):
    template_name = 'photogal/upload_photo.html'
    form_class = UploadPictureForm
    success_url = '/'

    def get_initial(self):
        initial = super(UploadView, self).get_initial()
        initial['user'] = self.request.user.id
        return initial

    def form_valid(self, form):
        return super().form_valid(form)


# @group_required('regular')
# def upload_view(request):
#     if request.method == 'POST':
#         form = UploadPictureForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     else:
#         form = UploadPictureForm(initial={"user": request.user.id})

#         context = {'form': form}
#         return render(request, 'photogal/upload_photo.html', context)


class PictureDetail(DetailView):
    model = Picture
    template_name = 'photogal/photo_info.html'
    pk_url_kwarg = 'picture_id'
