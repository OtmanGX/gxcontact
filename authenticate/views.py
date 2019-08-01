from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = "You were successfully logged in"

class LogoutFormView(SuccessMessageMixin, LogoutView):
    success_message = "You were successfully logged out"
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().get(self, request, *args, **kwargs)


class SignUpView(CreateView):
    template_name = "register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("home")



def edit_profile(request) :
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, ('The data have been updated !'))

    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})


def change_password(request) :
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('The data have been updated !'))

    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'password.html', {'form': form})