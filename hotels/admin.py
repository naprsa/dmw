from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Hotel, HotelImage

# Register your models here.


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 0


class HotelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    inlines = [HotelImageInline]


admin.site.register(Hotel, HotelAdmin)
