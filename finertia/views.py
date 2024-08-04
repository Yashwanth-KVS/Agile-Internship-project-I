
from django.contrib.auth import  authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# class SignupView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'registration/signup.html', {'form': form})
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('finertia:dashboard')
#         return render(request, 'registration/signup.html', {'form': form})

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import UserData, AllTransactions
import random
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce
import json
from django.core.serializers.json import DjangoJSONEncoder


class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Create UserData instance
            user_data = UserData.objects.create(user=user)

            # Get 15 random transactions
            all_transactions = list(AllTransactions.objects.all())
            random_transactions = random.sample(all_transactions, 15)

            # Add transactions to user_data
            user_data.transactions.add(*random_transactions)
            print('here')
            return redirect('finertia:dashboard')

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
                return redirect('finertia:dashboard')
        return render(request, 'registration/login.html', {'form': form})


def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    user_data = UserData.objects.get(user=request.user)
    user_transactions = user_data.transactions.all()
    context = {
        'transactions': user_transactions,
        'username': request.user.username  # Add this line
    }
    return render(request, 'dashboard.html', context)





def analytics(request):
    return render(request, 'analytics.html')


def insights(request):
    return render(request, 'ini-test.html')


def payments(request):
    return render(request, 'payments.html')


def logout(request):
    if request.method == 'GET':
        auth_logout(request)
        return render(request, 'registration/login.html')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('finertia:dashboard')
        return render(request, 'registration/login.html', {'form': form})
