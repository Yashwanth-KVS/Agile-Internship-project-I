from django.urls import path, re_path
from .views import SignupView, LoginView, logout, dashboard, insights, desktop1_api
from django.views.generic import TemplateView

urlpatterns = [
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    # path('', dashboard, name='dashboard'),
    path('insights', insights, name='insights'),
    # re_path(r'^.*', serve_react_app, name='react_app'),
    path('', TemplateView.as_view(template_name='home/index.html')),
    # path('api/desktop1', desktop1_api, name='desktop1_api')
]
