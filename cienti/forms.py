from django import forms
from .models import Voto
from utils.form_tools import LabelSuffixEmptyMixin


VotoCreateForm = forms.modelform_factory(
    model=Voto,
    # fields='__all__',
    exclude=['dispositivo', 'cor'],
    form=type('BaseFormClass', (LabelSuffixEmptyMixin, forms.ModelForm), {}),
    labels={
        'genero': 'Qual o seu gênero?',
        'idade': 'Qual a sua idade?',
        'dispositivo': 'Que tipo de computador você mais utiliza?',
        'opiniao': 'Qual a sua opinião sobre a expansão do uso e treinamento das IAs?',
        'cor': 'Dentre as cores abaixo, qual a sua favorita?',
    }
)
