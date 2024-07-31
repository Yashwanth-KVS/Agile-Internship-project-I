from django.urls import path
from .views import SignupView, LoginView, logout, home, dashboard, analytics, insights, payments

app_name = 'finertia'

urlpatterns = [
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
     path('analytics', analytics, name='analytics'),
    path('insights', insights, name='insights'),
    path('payments', payments, name='payments'),

]
