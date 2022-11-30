from django.shortcuts import render
from django.views.generic import ListView ## 여러 포스트 목록 페이지를 만들기 위해 ListView 가져오기
from .models import Post


# 여러 포스트 목록 페이지를 만들때 사용할 수 있는 기능
class PostList(ListView):
    model = Post
    ordering = '-pk'
   
   

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

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,

        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )

# Create your views here.
