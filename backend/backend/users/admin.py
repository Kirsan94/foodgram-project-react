from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('username', 'email',)
    empty_value_display = '--empty--'
