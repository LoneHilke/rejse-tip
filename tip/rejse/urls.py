from django.urls import  path
from . import views

URLPatterns = [
    # blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.views.blogs_comments, name="blogs comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete__blog_post, name="delete_blog_post"),
    path("search/", views.search, name="search"),

    # profile
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),

    # user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]