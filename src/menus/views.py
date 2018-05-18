from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.
from .forms import MenuItemForm
from .models import MenuItem

class MenuItemListView(ListView):
	def get_query(self):
		return MenuItem.objects.filter(user=self.request.user)

class MenuItemDetailView(DetailView):
	def get_query(self):
		return MenuItem.objects.filter(user=self.request.user)

class MenuItemCreateView(CreateView):
	template_name = 'form.html'
	form_class = MenuItemForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super(MenuItemCreateView, self).form_valid(form)

	def get_queryset(self):
		return MenuItem.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(MenuItemCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Create Menu Item'
		return context

class MenuItemUpdateView(UpdateView):
	template_name = 'form.html'
	form_class = MenuItemForm

	def get_queryset(self):
		return MenuItem.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(MenuItemUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update Menu Item'
		return context

