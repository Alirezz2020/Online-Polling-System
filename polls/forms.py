from django import forms
from django.forms import inlineformset_factory
from .models import Poll, Answer

class PollForm(forms.ModelForm):
    duration = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=99999999999,
        help_text="Enter the duration in minutes (e.g., 120 for 2 hours)."
    )

    class Meta:
        model = Poll
        fields = ['question', 'duration']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

# Create an inline formset for Answer linked to Poll.
AnswerFormSet = inlineformset_factory(
    Poll,
    Answer,
    form=AnswerForm,
    extra=4,      # By default, show 2 empty forms; adjust as needed.
    can_delete=False
)
