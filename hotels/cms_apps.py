from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
# from django.utils.translation import ugettext_lazy as _


class HotelsApphook(CMSApp):
    app_name = 'hotels'
    name = 'Hotels app'
    urls = ['hotels.urls']


apphook_pool.register(HotelsApphook)
