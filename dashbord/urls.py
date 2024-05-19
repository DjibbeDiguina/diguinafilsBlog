from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashbord, name='dashbord'),
    path('categories/', views.categories, name='categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('delete_category/<int:id>',views.delete_category, name='delete_category' ),
    #---post url 
    path('posts/',views.posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:id>',views.edit_post, name='edit_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    ]