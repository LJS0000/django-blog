from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm


User = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'signin-email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signin-password'})
    )

    class Meta:
        model = User
        fields = ['email', 'password']


class CustomUserChangeForm(UserChangeForm):
    password = None  # 비밀번호 필드 제거

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
