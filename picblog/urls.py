from django.urls import path
#from . import views
from . views import HomeView, PostDetailView, CreatePostView

urlpatterns = [
    #path('',views.home, name="home")
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',PostDetailView.as_view(),name="post"),
    path('create_post/', CreatePostView.as_view(),name="create"),
]