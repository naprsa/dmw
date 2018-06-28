# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse

from .models import LuxuryTravel, LuxuryTravelImage

# Create your views here.


class LuxuryListView(ListView):
    model = LuxuryTravel
    queryset = LuxuryTravel.objects.all()

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu(
                'luxury-list-menu', 'Luxury Travels')
            menu.add_sideframe_item(u'Luxury Travel list', url=reverse(
                'admin:luxury_luxurytravel_changelist'))
            menu.add_modal_item('Add new Luxury Travel', url="%s" % (
                reverse('admin:luxury_luxurytravel_add')))

        return super(LuxuryListView, self).render_to_response(context, **response_kwargs)


class LuxuryDetailView(DetailView):
    model = LuxuryTravel
    context_object_name = 'luxury'

    def get_context_data(self, **kwargs):
        context = super(LuxuryDetailView, self).get_context_data(**kwargs)
        context['images'] = LuxuryTravelImage.objects.all().filter(
            luxury=self.object)
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu(
                'luxury-detail-menu', 'Luxury Travel')
            menu.add_modal_item('change representation', url="%s" % (reverse('admin:luxury_luxurytravel_change',
                                                                             args=[self.object.id])))

        return super(LuxuryDetailView, self).render_to_response(context, **response_kwargs)
