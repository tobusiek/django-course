from django import forms

from reviews.models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         min_length=1,
#         max_length=100,
#         label="Your name",
#         error_messages={
#             "required": "Your name must not be empty!",
#             "max_length": "Please enter a shorter name!",
#         },
#     )
#     review_text = forms.CharField(
#         label="Your feedback", widget=forms.Textarea, max_length=200
#     )
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = []  # excluded fields from Review model
        labels = {
            "user_name": "Your name",
            "review_text": "Your feedback",
            "rating": "Your rating",
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!",
            },
        }
