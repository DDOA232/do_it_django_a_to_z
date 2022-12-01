# from django.shortcuts import render
from django.views.generic import ListView, DetailView ## 여러 포스트 목록 페이지를 만들기 위해 ListView 가져오기
from .models import Post, Category


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
