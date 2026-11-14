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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
admin.site.register(Post)
