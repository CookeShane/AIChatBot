from django import forms

class UserQuestionForm(forms.Form):
    """
    Form for users to submit their questions.

    Attributes:
        question (CharField): A text field for the user's question, with a maximum length of 255 characters.
            The field uses a TextInput widget with CSS class 'form-control' and a placeholder 'Ask your question here...'.

    Methods:
        clean():
            Cleans the form data.
            Returns:
                dict: The cleaned data.
    """
    question = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ask your question here...'
    }))

    def clean(self):
        cleaned_data = super().clean()
        
        return cleaned_data
