from django.views.generic import TemplateView
from pykafe.settings.base import mattermost


class KonversaView(TemplateView):
    template_name = 'pykafekonversa.html'

    def get_context_data(self, **kwargs):
        context = super(KonversaView, self).get_context_data(**kwargs)
        context["konversa"] = mattermost['url']
        return context

