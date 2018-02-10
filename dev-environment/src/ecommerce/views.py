from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title": "home home_page",
        "content": "welcome to the home page"
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        "title": "about_page",
        "content": "welcome to the about page"

    }
    return render(request, 'about_page.html', context)

def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  context = {
      "title": "contact_page",
      "content": "welcome to the contact page",
      "form": contact_form
  }

  if contact_form.is_valid():
    print(contact_form.cleaned_data)

  # if request.method == 'POST':
  #     print(request.POST)
  #     print(request.POST.get('fullName'))
  #     print(request.POST.get('email'))
  #     print(request.POST.get('content'))

  return render(request, 'contact/view.html', context)

def login_page(request):
  form_class = LoginForm(request.POST or None)
  content = {
    "form": form_class
  }

  print("User logged in: ")
  print(request.user.is_authenticated)   # false
  
  if form_class.is_valid():
    # print(form_class.cleaned_data)
    username = form_class.cleaned_data.get("username")
    password = form_class.cleaned_data.get("password")
    user = authenticate(request, username=username, password=password)

    print("User logged in: ")
    print(request.user.is_authenticated)   # false

    if user is not None:
      login(request, user)

      print("User logged in: ")
      print(request.user.is_authenticated)  # true
      
      #redirect to a success page
      # content['form'] = LoginForm()
      redirect("/login")
    else:
      # return a invalid login error message
      print('error')

  return render(request, "auth/login.html", content)

def register_page(request):
  form = LoginForm(request.POST or None)
  if form.is_valid():
    print(form.cleaned_data)
  return render(request, "auth/register.html", {})

# def home_page_old(request):
#     html_ = """
#         <!doctype html>
#         <html lang="en">
#           <head>
#             <!-- Required meta tags -->
#             <meta charset="utf-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#
#             <!-- Bootstrap CSS -->
#             <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#
#             <title>Hello, world!</title>
#           </head>
#           <body>
#             <div class='text-center'>
#                 <h1>Hello, world!</h1>
#             </div>
#             <!-- Optional JavaScript -->
#             <!-- jQuery first, then Popper.js, then Bootstrap JS -->
#             <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#             <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
#             <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#           </body>
#         </html>
#     """
#     return HttpResponse(html_)
