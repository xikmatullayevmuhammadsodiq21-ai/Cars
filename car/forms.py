from django import forms
# Remove 'from .models import Car' from the top
from .models import Car # This is usually fine, UNLESS models.py imports forms.py

class CarForm(forms.ModelForm):
    class Meta:
        from .models import Car  # Import it RIGHT HERE instead
        model = Car
        fields = '__all__'