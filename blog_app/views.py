from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from .forms import PostForm, CommentForm
# Create your views here.


class AboutView(TemplateView):
    """
    Creates the about page view
    """
    template_name = 'about.html'


class PostListView(ListView):
    """
    Creates the post list view which doubles as the home page.
    A list of all Published blog posts
    """
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    """
    Renders a detailed view of a selected blog post
    """
    model = Post
    comment = Comment


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    Create a new blog post using the Post Form
    """
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    model = Post
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    Edit An instance of the Post class
    """
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    model = Post
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete An instance of the Post class
    """
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog_app:post_list')


class DraftListView(LoginRequiredMixin, ListView):
    """
    View all unpublished Posts
    """
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-create_date')


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_app:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog_app/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog_app:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog_app:post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog_app:post_detail', pk=pk)
