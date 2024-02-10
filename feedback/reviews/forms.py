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


class UserNameFormField(forms.CharField):
    ...


class RatingFormField(forms.IntegerField):
    ...


class ReviewForm(forms.ModelForm):
    user_name = UserNameFormField(
        max_length=100,
        min_length=1,
    )
    rating = RatingFormField(max_value=5, min_value=1)

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
