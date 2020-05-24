from django import forms

from .models import ShortLink


class ShortLinkForm(forms.ModelForm):
    link = forms.URLField(label='')

    class Meta:
        model = ShortLink
        fields = ('link',)
