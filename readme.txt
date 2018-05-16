Code from https://github.com/codingforentrepreneurs/Try-Django-1.11

Based on Class View

27 - Simple + Effective Validation
	a. created a validators.py
	b. applied a function of the validators.py to either form.py or model.py eg) validate_category(value)
	c. saved a value entered as caplitalize before commit

28 - Letting Users own Data
	a. Shell (User to RestaurantLocation)
		from django.contrib.auth import get_user_model
		User = get_user_model()
		User.objects.all()
		admin = User.objects.get(id=1)
		admin.username 
		admin.email
		admin.password
		admin.is_active

		grab related data for a user
		admin.restaurantlocation.all() not working due to models.ForeignKey, it works if OneToOneField
		admin.restaurantlocation_set.all() all data class_instance.model_set.all(), QS associated with user

	b. Shell (RestaurantLocation to User)
		from restaurants.models import RestaurantLocation
		RestaurantLocation.objects.filter(owner__id=1)
		RestaurantLocation.objects.filter(owner__username__iexact='admin')

		qs = RestaurantLocation.objects.filter(owner__username__iexact='admin')
		obj = qs.first()
		obj.owner()
		User = obj.owner.__class__
		User.objects.all() return QS of users

32 - LoginView: In order to view authentication is needed
	a. from django.conf.urls import url, include in the root urls.py
	b. Add url(r'^accounts/', include('django.contrib.auth.urls')) in the root urls.py
	c. Add registration folder in the main template folder
	d. Create registration forms, logged_out, login, password_reset_complete, password_reset_confirm, password_reset_done, password_reset_email, password_reset_form
	e. Add LoginRequiredMixin class RestaurantCreateView(LoginRequiredMixin, CreateView)
	f. include below in the class RestaurantCreateView 
		login_url = '/accounts/login/'
    	login_redirect_url = '/restaurants/create/' or LOGIN_REDIRECT_URL can be added to settings.py
    g. Add EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' in the settings.py for email testing, it only works for existing users


33 - Using Reverse to Shortcut URLs
	a. Add urls.py in the app
	b. Add 
		url(r'^create/$', RestaurantCreateView.as_view(), name='create'), 
		url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
		url(r'$', RestaurantListView.as_view(), name='list'), must be the last if not detail page not working
	c. url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')) in the main urls.py
	d. get_absolute_url in the model, pass namespace:name and slug
	 









