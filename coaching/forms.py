from django import forms
from member.models import Member


class ClientJoinCoachForm(forms.Form):
    coach_username = forms.CharField(help_text='Coach\'s Username you wish to join')
    coach_link_code = forms.CharField(help_text='Coach\'s Link Code')



