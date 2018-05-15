from django.core.exceptions import ValidationError


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']

def validate_category(value):
	cat = value.capitalize()
	if not cat in CATEGORIES:
		raise ValidationError(f"{value} not a valid")
