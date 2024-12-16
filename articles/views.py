from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from.models import Article

class ArticleListView(ListView):
    model = Article
    template_name="article_list.html"
    context_object_name = "article"
# Create your views here.

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = "article_edit.html"

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')
class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ['title', 'body','author']