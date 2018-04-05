from django.contrib import admin

# Register your models here.

from .models import Post

# Personalizar el model admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["titulo","actualizado","timestamp"]
    list_display_links = ["actualizado"]
    list_filter = ["timestamp"]
    list_editable = ["titulo"]
    search_fields = ["titulo","contenido"]
    
    class Meta:
        model = Post
        
admin.site.register(Post,PostModelAdmin)
