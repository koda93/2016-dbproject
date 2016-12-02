from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'writer','created_at', 'updated_at')
    search_fields = ('title', 'writer')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','message','created_at','updated_at')
    search_fields = ('author', )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)