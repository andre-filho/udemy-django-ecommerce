from django import forms

class ContactForm(forms.Form):
  fullName = forms.CharField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "your fullname"
      })
    )
  email = forms.EmailField(
    widget=forms.EmailInput(attrs={
      "class": "form-control",
      "placeholder": "your email goes here"
    })
  )
  content = forms.CharField(
    widget=forms.Textarea(attrs={
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
  username = forms.CharField(
    widget=forms.TextInput(attrs={
      "class": 'form-control',
      "placeholder": "Username"
    })
  )
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Password"
    })
  )
