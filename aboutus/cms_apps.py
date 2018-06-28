from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
# from django.utils.translation import ugettext_lazy as _


class AboutUsApphook(CMSApp):
    app_name = 'aboutus'
    name = 'AboutUs app'
    urls = ['aboutus.urls']


apphook_pool.register(AboutUsApphook)
