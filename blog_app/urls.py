from django.urls import path, re_path, include
from . import views

app_name = 'blog_app'

urlpatterns = [
    # Path to Index page AKA post_list, a list of all blog posts
    re_path(r'^$', views.PostListView.as_view(),
            name='post_list'),

    # Path to About View. Link in Nav bar
    re_path(r'^about/$', views.AboutView.as_view(),
            name='about'),

    # Path to page that actually displays blog post of a given primary key
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(),
            name='post_detail'),

    # Path to display the "create a new blog post" page
    re_path(r'^post/new/$', views.CreatePostView.as_view(),
            name='post_new'),

    # Path to editing a post with a given primary key
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(),
            name='post_edit'),

    # Path to page that confirms delete
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(),
            name='post_remove'),

    # Path to view all unpublished posts
    re_path(r'^drafts/$', views.DraftListView.as_view(),
            name='drafts_list'),

    # Path to creating a comment
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post,
            name='add_comment_to_post'),

    # Path to approving a comment
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve,
            name='comment_approve'),

    # Path to removing a comment
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove,
            name='comment_remove'),

    # Path to publishing a post
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish,
            name='post_publish'),

]
