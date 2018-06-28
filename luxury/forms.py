# from django import forms
# from mice_direct.models import MICEDirection


# class ProgramByDirectionFilterForm(forms.Form):
#     CHOICES = list(direction.name for direction in MICEDirection.ojects.all())
#     by_direction = forms.ChoiceField(choices=CHOICES,
#                                      required=True,
#                                      widget=None,
#                                      label='Directions',
#                                      initial=None,
#                                      help_text='Choose direction...')
