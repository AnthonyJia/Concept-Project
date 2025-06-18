from django import forms
from django.contrib.auth import get_user_model
from .models import Profile, PortfolioLink

User = get_user_model()

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=30, 
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        required=False, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'creative_fields']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us something about yourself...',
                'rows': 5
            }),
            'creative_fields': forms.SelectMultiple(attrs={
                'class': 'form-select select2'
            }),
            'profile_pic': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
            self._user = user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(pk=self._user.pk).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
            self.save_m2m()

            # Save user fields
            if hasattr(self, '_user'):
                self._user.first_name = self.cleaned_data['first_name']
                self._user.last_name = self.cleaned_data['last_name']
                self._user.email = self.cleaned_data['email']
                self._user.save()
        return profile

class PortfolioLinkForm(forms.ModelForm):
    class Meta:
        model = PortfolioLink
        fields = ['name', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link Name'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        url = cleaned_data.get("url")

        if name and not url:
            raise forms.ValidationError("You must provide a URL if you enter a name.")
        
        return cleaned_data
