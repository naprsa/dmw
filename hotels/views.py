# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from .models import Hotel, HotelImage

# Create your views here.


class HotelListView(ListView):
    model = Hotel
    queryset = Hotel.objects.all()

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('hotels-list-menu', 'Hotels')
            menu.add_sideframe_item(u'Hotel representations list', url=reverse('admin:hotels_hotel_changelist'))
            menu.add_modal_item('Add new representation', url="%s" % (reverse('admin:hotels_hotel_add')))

        return super(HotelListView, self).render_to_response(context, **response_kwargs)


class HotelDetailView(DetailView):
    model = Hotel
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super(HotelDetailView, self).get_context_data(**kwargs)
        context['images'] = HotelImage.objects.all().filter(hotel=self.object)

        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('hotels-detail-menu', 'Hotel representation')
            menu.add_modal_item('change representation', url="%s" % (reverse('admin:hotels_hotel_change',
                                                                       args=[self.object.id])))

        return super(HotelDetailView, self).render_to_response(context, **response_kwargs)
