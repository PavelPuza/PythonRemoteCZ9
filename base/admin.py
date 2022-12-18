from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from base.models import Room, Message


class MessageAdmin(ModelAdmin):
    # ListView
    @staticmethod
    def cleanup_body(modeladmin, request, queryset):
        queryset.update(body="-- Deleted ---")

    ordering = ['id']
    list_display = ['id','room', 'body_short']
    list_display_links = ['id', 'body_short']
    list_per_page = 20
    list_filter = ['room']
    search_fields = ['body', 'id']
    actions = ['cleanup_body']

    #FormView
    fieldsets = [
        (
            None,
            {
                'fields': ['id', 'body']
            }
        ),
        (
            'Detail',
            {
                'fields': ['room', 'created', 'updated'],
                'description': 'Detailed information about room.'
            }
        ),
        (
            'User Information',
            {
                'fields': ['user']
            }
        )
    ]
    readonly_fields = ['id', 'created', 'updated']


admin.site.register(Room)
admin.site.register(Message, MessageAdmin)
