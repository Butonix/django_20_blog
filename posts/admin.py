from django.contrib import admin

# Register your models here.
from . models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title', 'content']

    list_display_links = ['id']
    list_editable = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
