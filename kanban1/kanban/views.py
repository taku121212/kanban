from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # 追加
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy # 追加
from django.views.generic import DetailView, UpdateView, CreateView # 追加

from .forms import UserForm, ListForm # 追加
from . models import List # 追加


def index(request):
    return render(request, "kanban/index.html")


@login_required # 追加
def home(request):
    return render(request, "kanban/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
    return render(request, 'kanban/signup.html', context)

