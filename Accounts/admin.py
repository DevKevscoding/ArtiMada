from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username','email','get_image_url')
    search_fields = ('username','email')
    
    def get_image_url(self,obj):
        return obj.profile.photo if hasattr(obj, 'profile') and obj.profile else 'Aucun Images'
        
            
admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
    