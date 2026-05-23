from django import forms
from .models import Category, Quiz

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'is_active']
        
        def clean_name(self):
            name = self.cleaned_data.get('name')
            if Category.objects.filter(name__iexact=name).exists():
                raise forms.ValidationError("Category with this name already exists.")
            return name
        
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'category', 'difficulty', 'passing_score', 'time_limit', 'is_active']

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if Quiz.objects.filter(title__iexact=title).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Quiz with this title already exists in the selected category.")
            return title