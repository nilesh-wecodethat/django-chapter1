from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from blog.models import Post
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger


def create_post(request): 
    user = User.objects.get(username="admin") #The get() method allows you to retrieve a single object from the database.
    post = Post(title='Another post',   # create post object
               slug='another-post',
               body='Post body.',
               author=user)
    post.save()

def update_post(request) : 
    post = Post.objects.get(slug = 'another-post')
    post.title = "Anther Post new title"  #update the post field
    post.save()


def all_posts(request) : 
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                    'blog/post/lists.html',
                    {'page': page,
                        'posts': posts})


def filter_posts(request) : 
    # posts =  Post.objects.filter(publish__year=2020)  #The filter() method in Django is used to retrieve records from the database that match certain criteria.
    # Post.objects.filter(publish__year=2020, author__username='admin')  #multiple filter conditions
    filtered_posts = Post.objects.filter(author__username='admin').exclude(status='draft').order_by('-publish') #The query retrieves all posts by the user 'admin', excluding drafts posts, and orders them in descending order.


def delete_post(request) : 
    post = Post.objects.get(id=1)
    post.delete()


def post_details(request, id=2) : 
    post = get_object_or_404(Post, id=2)
    return render(request,
                'blog\post\details.html',
                {'post_details' : post})
