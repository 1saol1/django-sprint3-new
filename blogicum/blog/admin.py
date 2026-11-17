from django.contrib import admin

from blog.models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    search_fields = ('name',)
    list_filter = ('is_published', 'created_at')


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'location',
        'is_published',
        'created_at'
    )
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'created_at', 'category', 'location')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)