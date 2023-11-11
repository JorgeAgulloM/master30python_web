from django import forms

class ArticleForm(forms.Form):
    title=forms.CharField(
        label='Title',
        max_length=100
    )
    content=forms.CharField(
        label='Content',
        widget=forms.Textarea
    )
    public=forms.TypedChoiceField(
        label='Is public?',
        choices=[        
            (1, 'Yes'),
            (0, 'No')
        ]
    )
    