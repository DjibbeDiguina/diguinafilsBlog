from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category_name

STATUS_CHOISE = (
    ('Draft', 'Draft'),
     ('Published', 'Published')
)

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    featured_image = models.ImageField(upload_to='upload/%Y/%m/%d')
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOISE, default='Draft')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    header = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.header