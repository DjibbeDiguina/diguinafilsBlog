
from django.forms import ModelForm

from blogs.models import Category

class Addcategory(ModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)