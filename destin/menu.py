from django.utils.translation import ugettext_lazy as _
# from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import Destination


class DestinationSubMenu(CMSAttachMenu):
    name = _('Destinations sub_menu')

    def get_nodes(self, request):
        nodes = []
        last_node = NavigationNode(
            _('All...'), '/destinations/', 999)
        for item in Destination.objects.only('name', 'pk'):
            node = NavigationNode(item.name,
                                  item.absolute_url,
                                  item.pk
                                  )

            nodes.append(node)
        nodes.append(last_node)
        return nodes


menu_pool.register_menu(DestinationSubMenu)
