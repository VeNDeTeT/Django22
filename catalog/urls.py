from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactView, ProductDetailView, CatalogView  # ← CBV!

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),           # ← .as_view()
    path("catalog/", CatalogView.as_view(), name="catalog"),     # ← .as_view()
    path("contacts/", ContactView.as_view(), name="contact"),    # ← .as_view()
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),  # ← .as_view()
]
