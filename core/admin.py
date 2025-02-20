from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DailyHighlight, Task, EnergyLevel, Distraction, Reflection

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(DailyHighlight)
admin.site.register(Task)
admin.site.register(EnergyLevel)
admin.site.register(Distraction)
admin.site.register(Reflection)
