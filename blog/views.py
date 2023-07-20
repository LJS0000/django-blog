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
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


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

    def get_initial(self):
        initial = super().get_initial()
        post = self.get_object()
        initial['title'] = post.title
        initial['content'] = post.content
        return initial

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
    template_name = 'blog/post_list.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'blog/post_list.html'
    fields = ['content']

    def get_initial(self):
        initial = super().get_initial()
        comment = self.get_object()
        initial['content'] = comment.content
        return initial

    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('blog:detail', kwargs={'pk': comment.post})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/post_detail.html'
    success_url = None


### Tag
class TagListView(ListView):
    model = Tag
    template_name = 'base.html'
    context_object_name = 'tags'

    def get_queryset(self):
        # 각 태그와 해당 태그의 블로그 글 개수를 가져오기 위해 annotate와 order_by 사용
        tags_cnt = Tag.objects.annotate(num_posts=Count('post')).order_by('-num_posts')[
            :10
        ]
        return tags_cnt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TagWriteView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'blog/post_detail.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/post_detail.html'
    success_url = None
