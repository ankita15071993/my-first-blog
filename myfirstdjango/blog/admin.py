from django.contrib import admin
# include our Post model
from .models import Post
# Register your models here, to make our model visible on the admin page
admin.site.register(Post)