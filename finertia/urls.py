from django.urls import path
from .views import SignupView, LoginView, logout, home, userpage, analytics, insights, payments

urlpatterns = [
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('', home, name='home'),
    path('user', userpage, name='userpage'),
     path('analytics', analytics, name='analytics'),
    path('insights', insights, name='insights'),
    path('payments', payments, name='payments'),

]
