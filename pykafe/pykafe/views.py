from django.views.generic import TemplateView
from pykafe.settings.base import mattermost, consolepython


class KonversaView(TemplateView):
    template_name = 'pykafekonversa.html'

    def get_context_data(self, **kwargs):
        context = super(KonversaView, self).get_context_data(**kwargs)
        context["konversa"] = mattermost['url']
        return context


class ConsolePython(TemplateView):
    template_name = 'consolepython.html'

    def get_context_data(self, **kwargs):
        context = super(ConsolePython, self).get_context_data(**kwargs)
        context["consolepython"] = consolepython['url']
        return context
