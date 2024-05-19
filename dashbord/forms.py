
from django.forms import ModelForm

from blogs.models import Category, Blog

class Addcategory(ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)

class AddblogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'short_description', 'blog_body', 'featured_image', 'is_featured', 'status')