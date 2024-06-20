from django.views.generic import CreateView
from .forms import VotoCreateForm
from utils.view_tools import SuccessUrlToItselfMixin


class VotoCreate(SuccessUrlToItselfMixin, CreateView):
    template_name = 'cienti/voto_create.html'
    form_class = VotoCreateForm
    extra_context = {'title': 'cienTI Power BI Demo'}
