from django.urls import path
from .views import ArticleDetailView
from .views import ArticleListView, ArticleCreateView, ArticleDeleteView


urlpatterns = [
    path('article', ArticleListView.as_view(), name='customer'),
    path('article/create', ArticleCreateView.as_view(), name='customer_create'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='customer_detail'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='customer_delete')
]
