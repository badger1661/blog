from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["post_title", "post_date", "last_updated", "id"]
    list_filter = ["post_title", "post_date"]
    search_fields = ["post_title", "post_date", "post_content", "id"]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
