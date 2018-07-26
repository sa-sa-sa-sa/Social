from django.views.generic import TemplateView

class ThanksPage(TemplateView):
    template_name='thanks.html'

class TestPage(TemplateView):
    template_name='test.html'

class HomePage(TemplateView):
    template_name='index.html'
