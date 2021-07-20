from django import forms

class RatingForm(forms.Form):
    design_rating = forms.IntegerField()
    usability_rating = forms.IntegerField()
    content_rating = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Leave a comment"}))