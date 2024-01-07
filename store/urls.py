from django.urls import path

from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
  path('', views.store, name='store'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name='checkout'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
