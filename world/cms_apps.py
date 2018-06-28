from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
# from django.utils.translation import ugettext_lazy as _


class WorldApphook(CMSApp):
    app_name = 'world'
    name = 'MICE World App'
    urls = ['world.urls']


apphook_pool.register(WorldApphook)
