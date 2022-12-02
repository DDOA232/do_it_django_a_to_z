# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView ## 여러 포스트 목록 페이지를 만들기 위해 ListView 가져오기
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category
from django.shortcuts import render, redirect

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

# 여러 포스트 목록 페이지를 만들때 사용할 수 있는 기능
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['카테고리모음'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context



   
   

   # ListView를 활용한 방법에서 PostList 불러오는 방법 1
   #  template_name = 'blog/index.html'




#def index(request):
#    posts = Post.objects.all().order_by('-pk')

#    return render(
#        request,
#        'blog/index.html',
#        {
#            'posts' : posts,
#        }
#    )

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['카테고리모음'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)

#    return render(
#        request,
#
#        'blog/single_post_page.html',
#        {
#            'post' : post,
#        }
#    )

# Create your views here.

def category_page(request, slug):
    category = Category.objects.get(slug =slug)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : Post.objects.filter(category=category),
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )