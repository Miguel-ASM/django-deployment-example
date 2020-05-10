from django import forms
from .models import Rider
from django.utils import timezone


current_year = timezone.now().year
oldest_year = current_year - 100
years = tuple(year for year in range(current_year,oldest_year,-1) )

class NewRider(forms.ModelForm):
    class Meta:
        model = Rider
        fields = '__all__'
        widgets = {
            'riderBirthData' : forms.SelectDateWidget(
                years = years,
            )
        }
        labels = {
            'riderName' :'Full Name',
            'riderBirthData' : 'Birth date',
            'riderNationality' : 'Country',
            'bikeBrand' : 'Brand of your bike',
            'bikeModel' : 'Model'
        }

    def __init__(self, *args, **kwargs):
        super(NewRider, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class myForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
