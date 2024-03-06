from django.forms import ModelForm, EmailInput

from people.models import People


class PersonForm(ModelForm):
    class Meta:
        model = People
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }