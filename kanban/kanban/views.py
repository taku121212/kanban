from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url # resolve_urlを追加
from django.views.generic import DetailView, UpdateView # UpdateViewを追加
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OnlyYouMixin 

from .forms import UserForm
def index(request):
    return render(request, "kanban/index.html")

@login_required
def home(request):
    return render(request, "kanban/home.html")


def zi(request):
    return render(request, "kanban/zi.html")


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

class UserDetailView(LoginRequiredMixin, DetailView): # この行を編集
    model = User
    template_name = "kanban/users/detail.html"
    
class UserUpdateView(OnlyYouMixin, UpdateView): # この行を編集
    model = User
    template_name = "kanban/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('kanban:users_detail', pk=self.kwargs['pk'])