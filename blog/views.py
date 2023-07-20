from django.db.models import Count
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Comment, Tag


### Post
class IndexView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    # 포스트를 최신순으로 가져옴
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

    # 최신 태그 10개를 가져옴
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mytags = Tag.objects.all()
        tags = Tag.objects.order_by('-id')[:7]
        context['mytags'] = mytags
        context['tags'] = tags
        return context


# 태그에 해당하는 리스트 조회
class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(tags__name=tag_name).order_by('-created_at')

    # 최신 태그 10개를 가져옴
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.order_by('-id')[:10]
        context['tags'] = tags
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mytags = Tag.objects.filter(post__id=self.kwargs['pk'])
        context['mytags'] = mytags
        return context


class PostWriteView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_write.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:list')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy('blog:detail', kwargs={'pk': post.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    success_url = '/'


### Comment
class CommentWriteView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog/post_detail.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'blog/post_detail.html'
    fields = ['content']

    def get_initial(self):
        initial = super().get_initial()
        comment = self.get_object()
        initial['content'] = comment.content
        return initial

    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('blog:detail', kwargs={'pk': comment.post_id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/post_detail.html'


### Tag
class TagWriteView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'blog/post_detail.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'blog/post_detail.html'
    success_url = None
