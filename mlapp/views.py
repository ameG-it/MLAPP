from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

def index(request):
  return render(request,'mlapp/index.html')

def input_form(request):
  form = InputForm()
  return render(request,'mlapp/input_form.html',{'form':form})
# Create your views here.
