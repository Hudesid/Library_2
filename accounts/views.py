from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from . import forms

def sign_up_view(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            print(form.errors)

    ctx = {'form': forms.SignupForm}
    return render(request, 'sign_up.html', ctx)

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('library:list')
            else:
                return HttpResponse("""<h1 style="text-align: center">There is no such user in the database</h1>""")

    ctx = {'form': forms.LoginForm}
    return render(request, 'login.html', ctx)

