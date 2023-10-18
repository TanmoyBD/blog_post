from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
#     blogs
    path("", views.blogs, name="blogs"),
    #path("blog_comments/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path('delete_blog_post/<int:blog_id>/', views.Delete_Blog_Post, name='delete_blog_post'),
    path('delete_from_fv/<int:blog_id>/', views.delete_from_fv, name='delete_from_fv'),
    path('save-favorite/<int:blog_id>/', views.save_favorite, name='save_favorite'),
    path('cat_wise_blog/<slug:slug>/', views.blogs, name='cat_wise_blog'),  # Hiting here
    path('favorite/', views.favorite_blogs, name='favorite_blogs'),
    path('blog_details/<int:blog_id>/',views.blog_details,name='blog_details'),
    path("search/", views.search, name="search"),
    path("delete/<int:blog_id>/", views.Delete_Blog_Post, name="delete"),
    path("edit/<int:blog_id>/", views.edit_blog, name="edit_blog"),

    
#     profile
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    
#    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]