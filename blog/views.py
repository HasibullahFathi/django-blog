from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    # model = Post # it shows all the records of Post model but we cant not filter them with this statement
    queryset = Post.objects.filter(status=0) # filter is posible because of Post.objects instead of all() we can use e.g filter(author=4)
    template_name = "post_list.html"  # now django pretends that our template name is post_list.html but if we have another name then we need this line of code