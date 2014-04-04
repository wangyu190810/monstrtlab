from models import News
from django.contrib import admin
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','author','time')
    search_fields = ['title']
    date_hierarchy = 'time'
admin.site.register(News,NewsAdmin)

#admin.site.register(Choice)
