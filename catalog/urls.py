from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    HomeView, ContactView, ProductDetailView, CatalogView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductUnpublishView, CategoryView
)

app_name = CatalogConfig.name

urlpatterns = [
    # Основные страницы
    path("", HomeView.as_view(), name="home"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("contacts/", ContactView.as_view(), name="contact"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),

    # CRUD операции
    path("create/", ProductCreateView.as_view(), name="create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),


    path("product/<int:pk>/unpublish/", ProductUnpublishView.as_view(), name="product_unpublish"),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
]
