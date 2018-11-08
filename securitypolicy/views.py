from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from rest_framework import generics

from .models import Rule, Section


# @login_required
def homepage(request):
    context = {
        'title': 'Security Policy',
        # 'sections' : Section.objects.all(),
        # 'rules': Rule.objects.all(),
    }
    return render(request, 'securitypolicy/homepage.html', context)
	# return HttpResponse('<h1>Security Policy Home</h1>')

class SectionListView(ListView):
	model = Section
	template_name = "securitypolicy/homepage.html"
	context_object_name = 'sections'

class SectionDetailView(ListView):

    def get(self, request, pk):
        context = {
            'title': 'Security Policy',
            'sections' : Section.objects.all(),
            'rules': Rule.objects.filter(section_id=pk),
        }
        return render(request, 'securitypolicy/section_detail.html', context)