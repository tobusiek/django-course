from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(min_length=1, max_length=100)
