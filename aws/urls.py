from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', SignUp),
    path('resend-code/', ResendConfirmCode),
    path('confirm-signup/', ConfirmSignUp),
    path('token/', GetToken),
    path('sign-in/', SignIn),


]
