from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from world.models import Platform, PlatformImage

# Register your models here.


class PlatformImageInline(admin.TabularInline):
    model = PlatformImage
    extra = 0


class PlatformAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    inlines = [PlatformImageInline]


admin.site.register(Platform, PlatformAdmin)
