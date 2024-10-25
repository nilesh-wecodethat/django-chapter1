from django.db import models
from django.utils  import timezone
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

class Post(models.Model) : 
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250,    #A SlugField for the URL slug, unique for the date it is published.
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts')  #related_name='blog_posts' means that from the User model, you can access all posts written by a particular user
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')


    class Meta:
        ordering = ('-publish',) # Orders the posts by the publish date in descending order.
    def __str__(self):  #The __str__() method is the default human-readable representation of the object. Django will use it in many places, such as the administration site.
        return self.title
