from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

# from django.utils.translation import ugettext_lazy as _


class LuxurysApphook(CMSApp):
    app_name = 'luxury'
    name = 'Luxurys App'
    urls = ['luxury.urls']


apphook_pool.register(LuxurysApphook)
