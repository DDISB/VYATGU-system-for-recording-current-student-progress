from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
# from django.urls import reverse

from .forms import LoginUserForm

# Create your views here.

def login_user(request):
  if (request.user.is_authenticated):
    return redirect('Journal', permanent=True)

  if (request.method == "POST"):
    form = LoginUserForm(request.POST)
    if (form.is_valid()):
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'], password=cd['password'])
      if (user and user.is_active):
        login(request, user)
        return redirect('Journal', permanent=True)
  else:
    form = LoginUserForm()
  list = {'title': 'Вход на сайт', 'form': form}
  return render(request, 'authentication/login.html', list)

def logout_user(request):
  if (request.user.is_authenticated):
    logout(request)
  return redirect('authentication:login', permanent=True)