from django.urls import path
from .views import ArticleListView
from .views import (
    ArticleDetailView,
    ArticleCreateView,  # for creating new articles
    ArticleUpdateView,
    ArticleDeleteView,
    
)

urlpatterns=[
    path("new/", ArticleCreateView.as_view(),name="article_new"),  # for creating new articles
    path("<int:pk>/",ArticleDetailView.as_view(),name="article_detail"),
    path("<int:pk>/edit/",ArticleUpdateView.as_view(),name="article_edit"),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name="article_delete"),
    
    path('',ArticleListView.as_view(),name='article_list'),
]