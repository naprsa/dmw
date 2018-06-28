from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse

from .models import TeamMember

# Create your views here.


class TeamView(ListView):
    template_name = 'aboutus_dteam.html'
    queryset = TeamMember.objects.all()

    # def get(self, request):
    #     args = {}
    #     team_members = TeamMember.objects.all()
    #     args['tm'] = team_members
    #     return render(request, self.template_name, args)

    def render_to_response(self, context, **response_kwargs):
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('dteam-menu', 'D-Team')
            menu.add_sideframe_item(u'D-Team list', url=reverse('admin:aboutus_teammember_changelist'))
            menu.add_modal_item('Add new representation', url="%s" % (reverse('admin:aboutus_teammember_add')))

        return super(TeamView, self).render_to_response(context, **response_kwargs)

class StoryView(TemplateView):
    template_name = 'aboutus_dstory.html'

    def get(self, request):
        return render(request, self.template_name)


class MissionVisionView(TemplateView):
    template_name = 'aboutus_dmv.html'

    def get(self, request):
        return render(request, self.template_name)
