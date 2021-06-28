from django.urls import path 
from . import views

urlpatterns = [
   path('', views.index , name="index"),
   path('destination/', views.destination , name="destination"),
   path('country/<int:id>', views.country, name="country"),
   path('about/', views.about , name="about"),
   path('blog/', views.blog , name="blog"),
   path('blogcategory/<int:id>', views.blogcategory, name="blogcategory"),
   path('blogsingle/<int:id>', views.blogsingle , name="blogsingle"),
   path('contact/', views.contact , name="contact"),
   path('single/<int:id>', views.single , name="single"),
   path('review/<int:id>', views.review , name="review"),
   path('register', views.register , name="register"),
   path('feedback', views.feedback , name="feedback"),
   path('post', views.post , name="post"),



]

