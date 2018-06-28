from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ('name', 'email',
                  'phone', 'message',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-sm form-full',
                                           'type': 'text',
                                           'placeholder': "Name"}
                                    ),
            'phone': forms.TextInput(attrs={'class': 'input-sm form-full',
                                            'type': 'text',
                                            'placeholder': "Phone"}
                                     ),
            'email': forms.EmailInput(attrs={'class': 'input-sm form-full',
                                             'type': 'email',
                                             'placeholder': 'your@email.com'}
                                      ),
            'message': forms.Textarea(attrs={'class': 'input-sm form-full',
                                             'rows': '3',
                                             'placeholder': 'Enter your message here...'}
                                      ),
        }
