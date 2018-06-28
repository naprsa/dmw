from django.utils.translation import ugettext_lazy as _
# from django.utils.safestring import mark_safe

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu


class AboutUsSubMenu(CMSAttachMenu):
    name = _('AboutUs SubMenu')

    def get_nodes(self, request):
        team_node = NavigationNode(_('D-Team'), '/about-us/d-team/', 1)
        story_node = NavigationNode(_('D-Story'), '/about-us/d-story/', 2)
        # mv_node = NavigationNode(
        #     _('Mission&Vision'), '/about-us/mission-vision/', 3)
        nodes = [team_node, story_node]     # mv_node]
        return nodes


menu_pool.register_menu(AboutUsSubMenu)
