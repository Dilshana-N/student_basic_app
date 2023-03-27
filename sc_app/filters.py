import django_filters
from django.forms import TextInput
from django_filters import CharFilter

from sc_app.models import Student_Register
class NameFilter(django_filters.FilterSet):
    user = CharFilter(field_name="name",label='',lookup_expr="icontains",widget=TextInput(attrs={'placeholder':'Search by Name'}))
    class Meta:
        model = Student_Register
        fields = ('user',)