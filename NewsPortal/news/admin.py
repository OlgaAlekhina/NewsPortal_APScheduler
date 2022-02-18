from django.contrib import admin
from .models import Category, Post, Author, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_text', 'post_author', 'post_type', 'post_categories', 'post_time', 'post_rating')
    list_filter = ('post_author', 'post_type', 'post_time', 'categories__name')
    search_fields = ('post_title', 'post_text')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'author_rating')
    search_fields = ('author__username',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_subscribers')
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'comment_text', 'post', 'comment_time', 'comment_rating')
    list_filter = ('comment_author', 'comment_time')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
