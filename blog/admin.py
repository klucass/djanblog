from django.contrib import admin
from .models import Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)