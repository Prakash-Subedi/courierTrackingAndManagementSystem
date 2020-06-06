from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # widgets = {
        #     'full_name': forms.CharField(attrs={'placeholder': 'Name'}),
        #     'email': forms.EmailField(attrs= {'placeholder': 'Email address'}),
        #     'subject': forms.CharField(attrs={'placeholder': 'Subject'}),
        #     'messsage': forms.Textarea(attrs={'placeholder': 'Enter Message here'}),
        # }

        # def __init__(self, *args, **kwargs):
        #     super(ContactForm, self).__init__(*args, **kwargs)
        #     for k, v in self.fields.items():
        #         v.widget.attrs['placeholder'] = k.capitalize()