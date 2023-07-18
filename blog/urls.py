from django.urls import path
from . import views

urlpatterns = [
    # 글 목록 조회
    path("", views.PostListView.as_view(), name='list'),
    # 글 상세 조회
    path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    # 글 작성
    path("write/", views.PostWriteView.as_view(), name='write'),
    # 글 수정
    path("detail/<int:pk>/edit/", views.PostUpdateView.as_view(), name='edit'),
    # 글 삭제
    path("detail/<int:pk>/delete/", views.PostDeleteView.as_view(), name='delete'),
]
