from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 회원가입
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    # 회원가입
    path('signin/', views.UserLoginView.as_view(), name='signin'),
    # 로그아웃
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    # 프로필 조회
    path('profile/', views.UserDetailView.as_view(), name='profile'),
    # 프로필 수정
    path('profile/edit/', views.UserLogoutView.as_view(), name='pf-edit'),
]
