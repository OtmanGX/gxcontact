from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

from authenticate.views import LoginFormView, LogoutFormView
from . import views

urlpatterns = [
    path('login/', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutFormView.as_view(), name="logout"),
    path('register/', views.SignUpView.as_view(), name="register"),
    # path('register/', views.register_user, name="register"),
    # path('edit/profile', views.edit_profile, name="edit_profile"),
    # path('edit/password', views.change_password, name="password"),
]
