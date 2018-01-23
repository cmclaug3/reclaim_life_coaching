from django import forms
from member.models import Member



class MemberRegisterForm(forms.ModelForm):
    username = forms.CharField(help_text='')
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ('email', 'username', 'password')

    def clean(self):
        cleaned_data = super(MemberRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            print('did not register, passwords did not match')
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class MemberLoginForm(forms.ModelForm):
    username = forms.CharField(help_text='')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ('username', 'password')


class BecomeCoachForm(forms.Form):
    key_code = forms.CharField()