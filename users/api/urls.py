from django.urls import path
from users.api import views

app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create-user'),
    path('token/', views.CreateAuthTokenView.as_view(), name='create-token')
]