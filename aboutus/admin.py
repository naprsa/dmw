from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import CompanyInfo, TeamMember

admin.site.register(CompanyInfo, SingletonModelAdmin)


class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember


admin.site.register(TeamMember, TeamMemberAdmin)

# There is only one item in the table, you can get it this way:
config = CompanyInfo.objects.get()

# # get_solo will create the item if it does not already exist
# config = CompanyInfo.get_solo()
