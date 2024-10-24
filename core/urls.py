from django.urls import path
from .views import register, user_login, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
