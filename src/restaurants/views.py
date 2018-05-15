from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView


from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm
# Create your views here.

class RestaurantListView(ListView):
	# def get_queryset(self):

	# 	slug = self.kwargs.get("slug")
	# 	print("slug",slug)
	# 	if slug:
	# 		queryset = RestaurantLocation.objects.filter(
	# 			Q(category__iexact=slug) |
	# 			Q(category__icontains=slug)	
	# 			)
	# 	else:
	# 		queryset = RestaurantLocation.objects.all()

	# 	return queryset
	queryset = RestaurantLocation.objects.all()



class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = "/restaurants/"