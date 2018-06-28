# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from .models import Destination, DestinationImage

# Create your views here.


class DestinationListView(ListView):
    model = Destination
    queryset = Destination.objects.all()

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('destinations-list-menu', 'Destinations')
            menu.add_sideframe_item(u'Destinations list', url=reverse('admin:destin_destination_changelist'))
            menu.add_modal_item('Add new destination', url="%s" % (reverse('admin:destin_destination_add')))

        return super(DestinationListView, self).render_to_response(context, **response_kwargs)

class DestinationDetailView(DetailView):
    model = Destination
    context_object_name = 'destination'

    def get_context_data(self, **kwargs):
        context = super(DestinationDetailView,
                        self).get_context_data(**kwargs)
        context['images'] = DestinationImage.objects.all().filter(
            destination=self.object)
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('destinations-detail-menu', 'Destination')
            menu.add_modal_item('Change destination', url="%s" % (reverse('admin:destin_destination_change',
                                                                       args=[self.object.id])))

        return super(DestinationDetailView, self).render_to_response(context, **response_kwargs)
