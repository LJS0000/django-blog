from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Post, Comment, Tag, PostTag


### Post
class IndexView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostWriteView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_write.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
        return reverse('blog:detail', kwargs={'pk': post.pk})


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
        return reverse('blog:detail', kwargs={'pk': comment.post})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/post_detail.html'


### Tag
class TagWriteView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'blog/post_write.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/post_edit.html'
