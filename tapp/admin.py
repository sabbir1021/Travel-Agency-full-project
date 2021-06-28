from django.contrib import admin
from .models import Country , Articale , Client , Blog , BlogComment , Subscribe , BlogCategory , ArticaleContact , Contact , Review
# Register your models here.

admin.site.register(Country)
admin.site.register(Articale)
admin.site.register(Client)

class BlogModel(admin.ModelAdmin):
    list_display = ["id","__str__"]
    list_per_page = 10
    class Meta:
        Model = Blog
admin.site.register(Blog , BlogModel)

class CommentModel(admin.ModelAdmin):
    list_display = ["__str__","name"]
    list_per_page = 10
    class Meta:
        Model = BlogComment
admin.site.register(BlogComment , CommentModel)
admin.site.register(Subscribe)
admin.site.register(BlogCategory)

class ArticaleContactModel(admin.ModelAdmin):
    list_display = ["__str__","phone","post" , "message"]
    class Meta:
        Model = ArticaleContact
admin.site.register(ArticaleContact , ArticaleContactModel)

class ContactModel(admin.ModelAdmin):
    list_display = ["__str__", "email"]
    class Meta:
        Model = Contact
admin.site.register(Contact , ContactModel)

class ReviewModel(admin.ModelAdmin):
    list_display = ["__str__", "mark"]
    class Meta:
        Model = Review
admin.site.register(Review , ReviewModel)