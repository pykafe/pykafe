from django.views.generic import TemplateView
from pykafe.settings.base import consolepython


class ConsolePython(TemplateView):
    template_name = 'consolepython.html'

    def get_context_data(self, **kwargs):
        context = super(ConsolePython, self).get_context_data(**kwargs)
        context["consolepython"] = consolepython['url']
        return context
