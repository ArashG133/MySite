from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = "-empty-"
    list_display = ["title",'author', 'status', 'create_date']
    search_fields = ["title", "content"]
    list_filter = ["status"]


admin.site.register(Post, PostAdmin)
