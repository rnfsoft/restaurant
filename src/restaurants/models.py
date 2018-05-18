from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

# Create your models here.
class RestaurantLocation(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=120, null=True, blank=True)
	category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail', kwargs={'slug': self.slug})

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.category = instance.category.capitalize()
	if not instance.slug: # == instance.slug is None or is this not meanigful?
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
