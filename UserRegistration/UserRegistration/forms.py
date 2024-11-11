from django import forms

class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(max_length=15, required=True)
    age = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(18, 100)], required=False)
    occupation = forms.CharField(max_length=50, required=False)
    interests = forms.CharField(max_length=200, required=False, widget=forms.Textarea)
