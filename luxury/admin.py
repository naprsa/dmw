from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from luxury.models import LuxuryTravel, LuxuryTravelImage

# Register your models here.


class LuxuryTravelImageInline(admin.TabularInline):
    model = LuxuryTravelImage
    extra = 0


class LuxuryTravelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    inlines = [LuxuryTravelImageInline]


admin.site.register(LuxuryTravel, LuxuryTravelAdmin)
