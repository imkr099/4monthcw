from django import forms


class PostCreateForm(forms.Form):
    image = forms.FileField()
    title = forms.CharField(min_length=5)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(required=False)


class CommentCreateForm(forms.Form):
    text = forms.CharField(min_length=1)