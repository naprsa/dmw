from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
# from django.utils.translation import ugettext_lazy as _


class DestinationsApphook(CMSApp):
    app_name = 'destin'
    name = 'Destinations App'
    urls = ['destin.urls']


apphook_pool.register(DestinationsApphook)
