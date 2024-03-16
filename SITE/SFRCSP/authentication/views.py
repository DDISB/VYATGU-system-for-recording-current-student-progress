from django.contrib.auth import authenticate, login

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginUserForm

# Create your views here.

def login_user(request):
  if (request.method == "POST"):
    form = LoginUserForm(request.POST)
    if (form.is_valid()):
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'], password=cd['password'])
      if (user and user.is_active):
        login(request, user)
        return HttpResponseRedirect(reverse("mainPage"))
  else:
    form = LoginUserForm()
  list = {'title': 'Вход на сайт', 'form': form}
  return render(request, 'authentication/login.html', list)

def logout_user(request):
  return HttpResponse("logout")