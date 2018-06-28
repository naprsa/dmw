from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Destination, DestinationImage

# Register your models here.


class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 0


class DestinationAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    inlines = [DestinationImageInline]


admin.site.register(Destination, DestinationAdmin)
