from django.shortcuts import render, redirect
from django.views.generic import ListView

def HomePageView(request):

	return redirect('/sp/')