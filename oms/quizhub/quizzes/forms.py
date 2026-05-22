from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'is_active']
        
        def clean_name(self):
            name = self.cleaned_data.get('name')
            if Category.objects.filter(name__iexact=name).exists():
                raise forms.ValidationError("Category with this name already exists.")
            return name