from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Receita

class home(ListView):
    model = Receita
    template_name = 'index.html'
    context_object_name = 'receitas'

class add(CreateView):
    model = Receita
    template_name = 'add.html'
    context_object_name = 'receita'
    fields = ('nome', 'ingredientes', 'preparo', 'porcao', 'tempoPreparo' , 'infoAdicional')
    success_url = reverse_lazy('home')