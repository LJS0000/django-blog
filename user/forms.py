from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signup-password1'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signup-password2'})
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data['email']
        username = email.split('@')[0]  # 이메일 앞부분을 username에 저장
        user.username = username
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'signin-email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signin-password'})
    )

    class Meta:
        model = User
        fields = ['email', 'password']


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['username', 'email', 'profile_img']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
