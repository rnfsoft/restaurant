"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic import TemplateView

from restaurants.views import RestaurantListView, RestaurantDetailView, RestaurantCreateView
						

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/', TemplateView.as_view(template_name='home.html')),
    url(r'^about/', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^login/', LoginView.as_view(), name='login'),
    # url(r'^logout/', LogoutView.as_view(), name='logout'),
    # url(r'^password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset_done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^password_reset_complete/',PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view()), # restaurants/create/ url must be above restaurants/(?P<slug>[\w-]+)/$, if not will not work
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    
]
