from django.conf.urls import url

from .views import MenuItemListView, MenuItemDetailView, MenuItemCreateView, MenuItemUpdateView

urlpatterns = [
	url(r'^create/$', MenuItemCreateView.as_view(), name='create'),
	url(r'^(?P<pk>\d+/$)', MenuItemDetailView.as_view(), name='detail'),
	url(r'$', MenuItemListView.as_view(), name='list')

]
