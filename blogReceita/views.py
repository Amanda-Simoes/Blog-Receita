from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Receita

class home(ListView):
    model = Receita
    template_name = 'index.html'
    context_object_name = 'receitas'