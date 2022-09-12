from asyncore import write
from urllib import response
from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import CategoryTable, Post, Tags, Comment
from .models import User
from django.http import HttpResponse
import csv, datetime
from django.contrib.auth import get_user_model


User = get_user_model()

def export_to_csv(modeladmin, request,queryset):
    opts =modeladmin.model._meta
    response = HttpResponse(content_type = 'text/csv')
    response['Conttent-Disposition'] = 'attachment;' 'filename = {}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [fields for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbos_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_discription = 'Export to CSV'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    action = [export_to_csv]






@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('title','author','category')
    list_filter =('title','author','category')



#admin.site.register(Post,PostAdmin)
# admin.site.register(User)
admin.site.register(CategoryTable)
admin.site.register(Tags)
admin.site.register(Comment)