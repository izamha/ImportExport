from django.contrib import admin
from .models import (Post, Comment,)
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field


class PostResource(resources.ModelResource):
    author = Field()
    liked = Field()
    created_at = Field()
    comments = Field()

    class Meta:
        model = Post
        fields = ('id', 'author', 'body', 'liked', 'created_at',)
        export_order = fields

    def dehydrate_author(self, obj):
        return str(obj.author.username)

    def dehydrate_liked(self, obj):
        data = [x.username for x in obj.liked.all()]
        users_liked = ", ".join(data)
        return users_liked

    def dehydrate_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y')

    
    def dehydrate_comments(self, obj):
        data = [x.body for x in obj.comments.all()]
        comments = ", ".join(data)
        return comments



class PostAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PostResource

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
