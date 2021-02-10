from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from . models import Post, Comment
from . forms import PostForm, CommentForm
from django.urls import reverse_lazy

#def home(request):
#    return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name= 'home.html'

class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class CreatePostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='create_post.html'
    
class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')

class CreateCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='add_comment.html'
    def form_valid(self, form):
        form.instance.post_id= self.kwargs['pk']
        return super().form_valid(form)
    
    success_url=reverse_lazy('home')