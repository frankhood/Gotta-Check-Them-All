from django.views.generic import TemplateView


class CheckThemAllTemplateView(TemplateView):
    template_name = "pokedex/check_them_all_homepage.html"