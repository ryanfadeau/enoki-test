from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name="calendar"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('create-user/', views.create_user_view.as_view(), name="create-user")
]