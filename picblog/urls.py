from django.urls import path
#from . import views
from . views import HomeView, PostDetailView, CreatePostView, DeletePostView, CreateCommentView

urlpatterns = [
    #path('',views.home, name="home")
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',PostDetailView.as_view(),name="post_detail"),
    path('create_post/', CreatePostView.as_view(),name="create_post"),
    path('article/<int:pk>/delete_post',DeletePostView.as_view(), name="delete_post"),
    path('article/<int:pk>/comment', CreateCommentView.as_view(),name="add_comment"),
]