from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm

def index(request):
  return render(request,'mlapp/index.html')

def input_form(request):
  if request.method == 'POST': # Formの入力があった時、
    form = InputForm(data=request.POST)
    if form.is_valid(): # Formの記載の検証を行い、
      form.save() # 問題なければ、入力データを保存
      return redirect('index') # 保存後遷移するページの指定
    else:
      return render(request, 'mlapp/input_form.html', {'form':form})
  else:
    form = InputForm()
    return render(request, 'mlapp/input_form.html', {'form':form})
