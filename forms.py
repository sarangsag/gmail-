from django import forms


class SubscribeForm(forms.Form):
    # email = forms.EmailField()
    subject=forms.CharField(max_length=50)
    # contact = forms.CharField(max_length=50)
    # name = forms.CharField(max_length=50)
    message=forms.CharField(max_length=1000)