from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('all-products', ProductsView.as_view(), name='products'),
    path('categories', CategoriesView.as_view(), name='category'),
    path('new-product', ProductCreateView.as_view(), name='new-product'),
    path('<int:pk>', ProductsDetailView.as_view(), name='product'),
    path('<int:pk>/order', OrderFormView.as_view(), name='new-order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
