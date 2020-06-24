from django.views.generic import ListView, DetailView
from home.models import HomeImage, WebMeta


class HomeIndex(ListView):
    template_name = 'home/index.html'
    queryset = HomeImage.objects.all()

    def get_context_data(self, **kwargs):
        banners = self.queryset.filter(is_banner=True)
        cards = self.queryset.filter(is_card=True)
        webmeta = WebMeta.objects.all().filter(is_use=True)
        context = super().get_context_data(**kwargs)
        context['banners'] = banners
        context['cards'] = cards
        context['webmeta'] = webmeta
        return context

