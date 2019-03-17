from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'base.html'

class SchoolListView(ListView):
    model = models.School
    template_name = 'schools-list.html'

class SchoolDetailView(DetailView):
    # rename the context object
    context_object_name = 'school_details'
    model = models.School
    template_name = 'schools-details.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("schools_list")
