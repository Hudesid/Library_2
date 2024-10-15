from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign/up/', views.sign_up_view, name='sign_up'),
    path('login/', views.login_view, name='login'),
]