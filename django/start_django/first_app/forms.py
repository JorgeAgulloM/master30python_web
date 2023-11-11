from django import forms
from django.core import validators

class ArticleForm(forms.Form):
    title=forms.CharField(
        label='Title',
        max_length=50,
        min_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your title',
                'class': 'title_form_article'
            }
        ),
        validators=[
            validators.MaxLengthValidator(5, 'Title is small'),
            validators.RegexValidator('^[a-zA-Z0-9 ñÑ]*$', 'Invalid characters', 'invalid_title')
        ]
    )
    content=forms.CharField(
        label='Content',
        widget=forms.Textarea,
        max_length=2500,
        min_length=25
    )
    content.widget.attrs.update( #No me gusta, pero tb funciona
        {
            'placeholder': 'Write your article',
            'class': 'content_form_article'
        } 
    )
    
    public=forms.TypedChoiceField(
        label='Is public?',
        choices=[        
            (1, 'Yes'),
            (0, 'No')
        ]
    )
    