from django.urls import path
from .views import SignupView, LoginView, logout, dashboard

urlpatterns = [
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('', dashboard, name='dashboard'),
]
