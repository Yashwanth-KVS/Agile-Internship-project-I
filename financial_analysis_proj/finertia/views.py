from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'registration/signup.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    auth_logout(request)
    return render(request,'registration/login.html')


def insights(request):
    return render(request,'dashboard.html')


def desktop1_api(request):
    data = {
        "ourServices": "Our Services",
        "products": [
            {"name": "Product"},
            {"name": "Manage your Finances"},
            {"name": "Savings Schemes"},
            {"name": "Financial Insights"}
        ],
        "navItems": ["Home", "Product", "Banking", "Login"],
        "footerText": "Follow us to know more",
        "contactUs": "Contact Us",
        "description": "Financial wellness is a way of effectively managing your finances. Not knowing how to deal with your finances can lead to major stress, anxiety or depression. Finance plays a substantial role in your daily wellness and well-being."
    }
    return JsonResponse(data)