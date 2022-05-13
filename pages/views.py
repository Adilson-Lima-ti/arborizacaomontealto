from django.views.generic import TemplateView
from trees.models import Square


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['square'] = Square.objects.all() #ordem aleatória
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"

    


