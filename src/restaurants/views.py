from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm
# Create your views here.

class RestaurantListView(ListView):
	queryset = RestaurantLocation.objects.all()

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    login_url = '/accounts/login/'
    login_redirect_url = '/restaurants/create/'
    

    def form_valid(self, form):
    	instance = form.save(commit=False)
    	instance.owner = self.request.user
    	return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
    	context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
    	context['title'] = 'Add Restaurant'
    	return context 