from django.contrib import admin


# Register your models here.

from .models import Project  #this is the model(table) Project we created

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    
    list_display=['title','description','images']   
    search_fields=['title','description']  #this provides ease of searching projects because one day thee may be 100 projects
    list_filter=['title']  #we added filter option by titles (which works aphabetically A-Z)

