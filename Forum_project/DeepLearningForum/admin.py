from django.contrib import admin

from .models import User, Article, Tag, Category, Comment, Follow

# Register your models here.
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Follow)



