from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

from django.shortcuts import redirect
# Create your views here.

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')

    else:
        f = CustomUserCreationForm()

    return render(request, 'home/register.html', {'form': f})


class SignUpView(CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    success_url='/smart/notes'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'

class HomeView(TemplateView):
    template_name='home/welcome.html'

