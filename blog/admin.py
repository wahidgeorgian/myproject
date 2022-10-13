from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CategoryTable, Post, Tags, Comment, User
from django.http import HttpResponse
import csv, datetime


class UserAdmin(UserAdmin):
    list_display =('username','first_name','last_name')
    actions = ("export_as_csv",)

    def export_as_csv(self, request, queryset):

        meta = 'users'
        field_names = ['username','first_name','last_name','email','mobile_number','city','state','country']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([str(obj.username),str(obj.first_name),str(obj.last_name),str(obj.email),str(obj.mobile_number),str(obj.city),str(obj.state),str(obj.country)])

        return response

    export_as_csv.short_description = "Export Selected"

class PostAdmin(Post):
    list_display =('title','author','category')
    actions = ("export_as_csv",)

    def export_as_csv(self, request, queryset):

        meta = 'posts'
        field_names = ['title','author','category']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([str(obj.title),str(obj.author),str(obj.category),])

        return response

    export_as_csv.short_description = "Export Selected"


class PostAdmin(admin.ModelAdmin):
    list_display =('title','author','category')
    list_filter =('title','author','category')
    search_fields = ['title',]
    

admin.site.register(Post,PostAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(CategoryTable)
admin.site.register(Tags)
admin.site.register(Comment)