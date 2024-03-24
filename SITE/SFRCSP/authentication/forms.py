from django import forms

class LoginUserForm(forms.Form):
  username = forms.CharField(label="Логин", 
    widget=forms.TextInput(attrs={'type': 'login', 
      'class': 'form-control', 
      'id': 'floatingInput', 
      'placeholder': 'login'}))
  password = forms.CharField(label="Пароль", 
    widget=forms.PasswordInput(attrs={'type': 'password', 
      'class': 'form-control', 
      'id': 'floatingPassword',
      'placeholder': 'password'}))
  