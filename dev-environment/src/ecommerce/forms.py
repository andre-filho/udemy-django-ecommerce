from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
  fullName = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "your fullname"
      })
    )
  email = forms.EmailField(widget=forms.EmailInput(attrs={
      "class": "form-control",
      "placeholder": "your email goes here"
    })
  )
  content = forms.CharField(widget=forms.Textarea(attrs={
      "class": "form-control",
      "placeholder": "your content goes here"
    })
  )

  def clean_email(self):
    email = self.cleaned_data.get("email")
    if not "gmail.com" in email:
      raise forms.ValidationError("Email is invalid")
    return email

class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={
      "class": 'form-control',
      "placeholder": "Username"
    })
  )
  password = forms.CharField(widget=forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Password"
    })
  )

class RegisterForm(forms.Form):
  
  username = forms.CharField(widget=forms.TextInput(attrs={
      "class": 'form-control',
      "placeholder": "Username"
    })
  )
  
  email = forms.CharField(widget=forms.EmailInput(attrs={
      "class": "form-control",
      "placeholder": "Your email"
    })
  )
  
  password = forms.CharField(widget=forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Password"
    })
  )
  
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Password confirmation"
    })
  )

  def clean_username(self):
    username = self.cleaned_data.get('username')
    checker  = User.objects.filter(username=username)
    if checker.exists():
      raise forms.ValidationError("Username is already taken")
    return username

  def clean_email(self):
    email = self.cleaned_data.get('email')
    qs    = User.objects.filter(email=email)
    if qs.exists():
      raise forms.ValidationError("email is taken")
    return email

  def clean(self):
    data      = self.cleaned_data
    password  = self.cleaned_data.get("password")
    password2 = self.cleaned_data.get("confirm_password")
    if password2 != password:
      raise forms.ValidationError("passwords must match")
    return data

