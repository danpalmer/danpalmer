from django.contrib import admin

from .models import Post, PostImage


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'title',
        'created',
        'published',
    )
    date_hierarchy = 'published'


class PostImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'post',
        'title',
        'slug',
        'created',
    )
    date_hierarchy = 'created'

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
