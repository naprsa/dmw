from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import Slider
from destin.models import Destination
from world.models import Platform
from aboutus.models import CompanyInfo
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.template.context_processors import csrf
import json
from itertools import chain

from mice.settings.dev import EMAIL_HOST as EMAIL
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        args = {}
        slider_imgs = Slider.objects.all()
        destinations = Destination.objects.all().exclude(name='zzz')[:6]
        company = CompanyInfo.objects.get()
        world_slider = Platform.objects.all()
        slider = list(chain(slider_imgs, destinations, world_slider))
        args['slider'] = slider
        args['destinations'] = destinations
        args['company'] = company
        args['form'] = ContactForm()
        return render(request, self.template_name, args)

    def post(self, request):
        send_to = CompanyInfo.objects.values('email')[0].get('email')
        args = {}
        form = ContactForm(self.request.POST)
        token = csrf(request)
        args['csrf_token'] = token['csrf_token']
        if form.is_valid():
            # form = form.save()
            cd = form.cleaned_data
            print(cd)
            message = """
            This message is from DMWTRAVER.COM!
            {0} {1}, email {2}
            wrote to you: {3}
            """.format(cd['name'],
                       cd['phone'],
                       cd['email'],
                       cd['message'])
            print(message)
            try:
                send_mail('This message is from DMWTRAVER.COM!',
                          message,
                          EMAIL,
                          [send_to],
                          fail_silently=False)
            except BadHeaderError:
                print('error bad header')
                return_str = render_to_string('inc_message_error.html')
                return HttpResponse(json.dumps(return_str),
                                    content_type='application/json')
            return_str = render_to_string('inc_message_success.html')
            return HttpResponse(json.dumps(return_str),
                                content_type='application/json')

        else:
            args = {'form': form}
            token = csrf(request)
            args['csrf_token'] = token['csrf_token']
            return_str = render_to_string('inc_message_error.html', args)
            return HttpResponse(json.dumps(return_str),
                                content_type='application/json')
