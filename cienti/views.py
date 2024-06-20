from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib import messages
from .forms import VotoCreateForm
from utils.view_tools import SuccessUrlToItselfMixin


class VotoCreate(SuccessUrlToItselfMixin, CreateView):
    template_name = 'cienti/voto_create.html'
    form_class = VotoCreateForm
    extra_context = {'title': 'cienTI Power BI Demo'}

    def form_valid(self, form) -> HttpResponse:
        messages.success(self.request, 'Resposta Enviada!')
        return super().form_valid(form)
