from django.contrib import admin
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Admin for the blog post."""
    pass
