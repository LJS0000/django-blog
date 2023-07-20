from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회, 태그 목록 조회
    path("", views.IndexView.as_view(), name='list'),
    # 글 상세 조회, 글 태그 조회, 댓글 조회
    path("detail/<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    # 글 작성
    path("write/", views.PostWriteView.as_view(), name='write'),
    # 글 수정
    path("detail/<int:pk>/edit/", views.PostUpdateView.as_view(), name='edit'),
    # 글 삭제
    path("detail/<int:pk>/delete/", views.PostDeleteView.as_view(), name='delete'),
    # 댓글 작성
    path(
        "detail/<int:pk>/comment/write/",
        views.CommentWriteView.as_view(),
        name='cm-write',
    ),
    # 댓글 수정
    path(
        "detail/<int:pk>/comment/edit/",
        views.CommentUpdateView.as_view(),
        name='cm-edit',
    ),
    # 댓글 삭제
    path(
        "detail/comment/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name='cm-delete',
    ),
    # 태그 작성
    path(
        "detail/<int:pk>/tag/write/",
        views.TagWriteView.as_view(),
        name='tag-write',
    ),
    # 태그 삭제
    path(
        "detail/tag/<int:pk>/delete/",
        views.TagDeleteView.as_view(),
        name='tag-delete',
    ),
    # 태그 검색
    # 일반 검색
]
