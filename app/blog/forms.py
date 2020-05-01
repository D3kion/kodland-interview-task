from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
