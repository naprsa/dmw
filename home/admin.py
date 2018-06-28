from django.contrib import admin
# from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import Slider

# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    model = Slider


admin.site.register(Slider, SliderAdmin)
