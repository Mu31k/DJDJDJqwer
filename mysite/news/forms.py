from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'from-control',
                'placeholder': '25.12.2021 11:59:59'
            }),
            'full_text': Textarea(attrs={
                'class': 'from-control',
                'placeholder': 'Текст статьи'
            })
        }