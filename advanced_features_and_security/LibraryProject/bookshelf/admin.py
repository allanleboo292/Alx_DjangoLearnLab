from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser  # Import your CustomUser model

# BookAdmin Registration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# CustomUserAdmin Registration
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  # Add custom fields here
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  # Add custom fields for adding a user
    )

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Alternatively, if you are using get_user_model() for registration:
User = get_user_model()

# Ensure you only register once and not with conflicting UserAdmin
if not admin.site.is_registered(User):
    admin.site.register(User, CustomUserAdmin)  # Register CustomUser only if it's not already registered
