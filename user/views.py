from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomUserChangeForm,
)
from django.urls import reverse_lazy


### User
class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/user_signup.html'
    success_url = reverse_lazy('user:signin')


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'user/user_signin.html'
    success_url = '/'


class UserLogoutView(LogoutView):
    next_page = '/'


### Profile
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/profile_detail.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'user/profile_edit.html'
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        if form.cleaned_data.get('password'):
            update_session_auth_hash(self.request, self.object)
        return response
