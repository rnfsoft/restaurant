from django.conf.urls import url
from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView

urlpatterns =[
	
	url(r'^create/$', RestaurantCreateView.as_view(), name='create'), # restaurants/create/ url must be above restaurants/(?P<slug>[\w-]+)/$, if not will not work
	url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
	url(r'$', RestaurantListView.as_view(), name='list'),
]
