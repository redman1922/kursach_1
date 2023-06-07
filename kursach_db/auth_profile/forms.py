from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("picture",
                  "last_name",
                  "first_name",
                  "age",
                  "passport",
                  "passport_region",
                  "study_type",
                  "study_place",
                  "professions",
                  "archived",
                  )

    picture = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        required=False,
    )
    last_name = forms.TextInput()
    first_name = forms.TextInput()
    age = forms.NumberInput()
    passport = forms.TextInput()
    passport_region = forms.TextInput()
    study_type = forms.TextInput()
    study_place = forms.TextInput()
    professions = forms.CheckboxSelectMultiple()
    archived = forms.CheckboxInput()
