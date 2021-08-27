from django.views.generic import ListView, DetailView, CreateView
from . models import Post
from . forms import PostForm

#def home(request):
#    return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name= 'home.html'
    ordering=['-id']

class PostDetailView(DetailView):
    model=Post
    template_name='post.html'

class CreatePostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='create.html'
    
