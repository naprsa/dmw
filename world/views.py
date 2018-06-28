# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse

from .models import Platform, PlatformImage

# Create your views here.


class PlatformListView(ListView):
    model = Platform
    queryset = Platform.objects.all()

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('world-list-menu', 'MICE Worlds')
            menu.add_sideframe_item(u'MICE Worlds list', url=reverse('admin:world_platform_changelist'))
            menu.add_modal_item('Add new MICE World', url="%s" % (reverse('admin:world_platform_add')))

        return super(PlatformListView, self).render_to_response(context, **response_kwargs)


class PlatformDetailView(DetailView):
    model = Platform
    context_object_name = 'platform'

    def get_context_data(self, **kwargs):
        context = super(PlatformDetailView,
                        self).get_context_data(**kwargs)
        context['images'] = PlatformImage.objects.all().filter(
            platform=self.object)
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('world-detail-menu', 'MICE World')
            menu.add_modal_item('Change MICE World', url="%s" % (reverse('admin:world_platform_change',
                                                                         args=[self.object.id])))

        return super(PlatformDetailView, self).render_to_response(context, **response_kwargs)
