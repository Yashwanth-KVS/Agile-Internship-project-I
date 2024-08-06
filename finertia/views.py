from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FinancialForm
from .MLmodel import classify_financial_status_and_suggest_plan
import pandas as pd

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


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import UserData, AllTransactions
import random
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce
import json
from django.core.serializers.json import DjangoJSONEncoder
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    mobile_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "mobile_number", "password1", "password2")


class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            login(request, user)
            return redirect('finertia:login')
        else:
            print("Form is not valid")
            print(form.errors)
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
                print("Logged in successfully")
                login(request, user)
                return redirect('finertia:dashboard')
            else:
                # Add an error if authentication fails
                form.add_error(None, "Invalid username or password")
        else:
            # Handle form errors (e.g., empty fields)
            form.add_error(None, "Please correct the errors below.")
        print("Login failed")
        return render(request, 'registration/login.html', {'form': form, })


def home(request):
    return render(request, 'home.html')


# @login_required
# def dashboard(request):
#     user_data = UserData.objects.get(user=request.user)
#     user_transactions = user_data.transactions.all()
#     context = {
#         'transactions': user_transactions,
#         'username': request.user.username  # Add this line
#     }
#     return render(request, 'dashboard.html', context)

@login_required
def dashboard(request):
    user_data = UserData.objects.get(user=request.user)
    user_transactions = user_data.transactions.all()

    # Calculate spending by category
    # category_spending = user_transactions.filter(income_expense='Expense').values('category').annotate(
    #     total=Coalesce(Sum('amount', output_field=DecimalField()), 0)
    # ).order_by('-total')

    # Calculate spending by category
    category_spending = user_transactions.filter(income_expense='Expense').values('category').annotate(
        total=Coalesce(Sum('amount', output_field=DecimalField()), 0, output_field=DecimalField())
    ).order_by('-total')

    # Prepare data for the chart
    categories = [item['category'] for item in category_spending]
    amounts = [float(item['total']) for item in category_spending]

    context = {
        'transactions': user_transactions,
        'username': request.user.username,
        'categories_json': json.dumps(categories, cls=DjangoJSONEncoder),
        'amounts_json': json.dumps(amounts, cls=DjangoJSONEncoder),
    }
    return render(request, 'dashboard.html', context)


@login_required
def analytics(request):
    return render(request, 'analytics.html')


@login_required
def insights(request):
    return render(request, 'ini-test.html')


@login_required
def payments(request):
    return render(request, 'payments.html')


@login_required
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


@login_required
def financial_form_view(request):
    if request.method == 'POST':
        form = FinancialForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            stability, loan_eligibility, suggested_loan_amount, plan_text = classify_financial_status_and_suggest_plan(
                form_data)
            return render(request, 'result.html', {
                'stability': stability,
                'loan_eligibility': loan_eligibility,
                'suggested_loan_amount': suggested_loan_amount,
                'plan_text': plan_text
            })
    else:
        form = FinancialForm()
    return render(request, 'analytics.html', {'form': form})
