from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff') 
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups') 
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'first_name', 'last_name', 'bio', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name') 
    ordering = ('email',) 


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['body', 'room',]
    list_filter = ('room',)
    ordering = ('-updated',)
    search_fields = ('user', 'room',  'body',)
    list_display_links = ('body',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'host', 'description', 'topic', 'created']
    list_filter = ('name', 'host', 'topic',)
    ordering = ('-updated',)
    search_fields = ('name', 'host',)
    list_display_links = ('name',)


admin.site.register(Topic)
admin.site.register(User, CustomUserAdmin)
