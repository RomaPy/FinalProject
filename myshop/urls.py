"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from django.conf.global_settings import STATIC_ROOT
from django.urls import path


from shopsite import views
from shopsite.views import gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('checkout', views.checkout, name='checkout'),
    path('gallery', views.gallery, name='gallery'),
    path('my-account', views.my_account, name='my-account'),
    path('shop', views.shop, name='shop'),
    path('shop-detail', views.shop_detail, name='shop-detail'),
    path('wishlist', views.wishlist, name='wishlist'),

]
# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)