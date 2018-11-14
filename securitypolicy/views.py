from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

from rest_framework import generics
from rest_framework import viewsets
from .serializers import SectionSerializer, RuleSerializer

from .models import Rule, Section, SubSection, Policy


# @login_required
def homepage(request):
    context = {
        'title': 'Security Policy',
        # 'sections' : Section.objects.all(),
        # 'rules': Rule.objects.all(),
    }
    return render(request, 'securitypolicy/homepage.html', context)


class PolicyListView(ListView):
    model = Policy
    template_name = "securitypolicy/homepage.html"
    context_object_name = 'policies'


class SectionListView(ListView):
    def get(self, request, pk):
        context = {
            'title': 'Security Policy - Policy Detail',
            'sections': Section.objects.filter(policy_id=pk, )
        }
        return render(request, 'securitypolicy/policy.html', context)


class SectionListViewAPI(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class RuleListViewAPI(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


class SubSectionListView(ListView):
    def get(self, request, pk, pks):
        context = {
            'title': 'Security Policy - Section Detail',
            'rules': Rule.objects.filter(section_id=pks, ),
            'policy': Policy.objects.filter(id=pk, ),
            'subsections': SubSection.objects.filter(section_id=pks, )
        }
        return render(request, 'securitypolicy/section_detail.html', context)


class RuleListView(ListView):
    def get(self, request, pk, pks, pkss):
        context = {
            'title': 'Security Policy',
            'policy': Policy.objects.filter(id=pk),
            'sections': Section.objects.filter(policy_id=pk, id=pks),
            'subsections': SubSection.objects.filter(section_id=pks),
            'rules': Rule.objects.filter(subsection_id=pkss)
        }
        return render(request, 'securitypolicy/subsection_detail.html', context)

class RuleDetailView(DetailView):
    model = Rule


class RuleCreateView(LoginRequiredMixin, CreateView):
    model = Rule
    fields = ['title', 'content', 'section']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# <app>/<model>_<view_type>.html


class RuleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Rule
    fields = ['title', 'content', 'section']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# <app>/<model>_<view_type>.html

    def test_func(self):
        rule = self.get_object()
        if self.request.user == rule.author:
            return True
        return False


class RuleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rule
    success_url = '/'

    def test_func(self):
        rule = self.get_object()
        if self.request.user == rule.author:
            return True
        return False


def about(request):
    return render(request, 'securitypolicy/about.html', {'title': 'About'})
# return HttpResponse('<h1>Security Policy About</h1>')


class RuleSearch(ListView):
    def get(self, request):
        context = {
            'title': 'Security Policy',
            'sections': Section.objects.all(),
            'rules': Rule.objects.filter(title__contains=request.GET.get("q")),
        }
        return render(request, 'securitypolicy/rule_search.html', context)