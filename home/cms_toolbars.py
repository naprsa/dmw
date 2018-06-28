from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break, SubMenu
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK


@toolbar_pool.register
class SliderToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Settings'))
        position = admin_menu.get_alphabetical_insert_position(_('home'), SubMenu)

        if not position:
            position = admin_menu.find_first(
                Break, identifier=ADMINISTRATION_BREAK) + 1
            admin_menu.add_break('custom-break', position=position)

        menu = admin_menu.get_or_create_menu(
            'slider-menu', _('Home Slider'), position=position)

        # Добавляем ссылку на ПРИЛОЖЕНИЕ_МОДЕЛЬ_...
        url = reverse('admin:home_slider_changelist')
        menu.add_sideframe_item(_('Slider images'), url=url)

        url = reverse('admin:home_slider_add')
        menu.add_modal_item(_('Add slider image'), url=url)
