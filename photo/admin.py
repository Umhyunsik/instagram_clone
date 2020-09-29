from django.contrib import admin

# Register your models here.
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created','updated','author']
    search_fields = ['text','created','author__username']#author은 foreign key라 __ 해당모델의 하위키값
    ordering=['-updated','-created']
admin.site.register(Photo,PhotoAdmin)
