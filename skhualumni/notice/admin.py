from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'writer','created_at', 'updated_at')
    search_fields = ('title', 'nt_writer')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'message', 'created_at', 'updated_at')
    search_fields = ('nt_author', )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
