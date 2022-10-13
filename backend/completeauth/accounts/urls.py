
from django.urls import path

from accounts.viewss import social 
from .views import SocialLogin,Home

app_name = 'users'

urlpatterns = [
    path('authentication-test/', social.authentication_test),
    path('social/',SocialLogin.as_view()),
    path('home/',Home.as_view(),name="home")
]