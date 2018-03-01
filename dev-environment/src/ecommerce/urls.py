"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static


from django.contrib import admin
# from django.urls import path
from django.conf.urls import url

from .views import home_page, about_page, contact_page, login_page, register_page
from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view

urlpatterns = [
  # path('', home_page),
  # path('about/', about_page),
  # path('contact/', contact_page),
  # path('admin/', admin.site.urls),


  url(r'^$', home_page),
  url(r'^about/$', about_page),
  url(r'^contact/$', contact_page),
  url(r'^admin/', admin.site.urls),
  url(r'^login/$', login_page),
  url(r'^register/$', register_page),
  url(r'^products/$', ProductListView.as_view()),
  url(r'^products-fbv/$', product_list_view),

  # (?P<pk>\d+) is a regular expression meant to catch and register the id of the
  # product at the url
  # FURTHER READING: http://kirr.co/plqin
  url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
  url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view)
]

# when debug is turned off in production, also will the static files
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
