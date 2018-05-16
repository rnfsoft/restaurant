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






