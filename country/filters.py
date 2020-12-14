import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CountryFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	country_name = CharFilter(field_name='country_name', lookup_expr='icontains')


	class Meta:
		model = country
		fields = '__all__'
		#exclude = ['customer', 'date_created']