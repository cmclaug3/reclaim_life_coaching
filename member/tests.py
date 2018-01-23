from django.test import TestCase

from member.forms import BecomeCoachForm, MemberRegisterForm, MemberLoginForm
from member.models import Member, Space, MemberSpace


# VIEWS

class RegisterViewTest(TestCase):

    def setUp(self):

        # THIS NEEDS MAJOR WORK
        # need to account for new features
        # (email, password_confirmation)

        stuff = {'username': 'tyrone35', 'password': 'pirates2016'}
        yee = MemberRegisterForm(stuff)
        yee.is_valid()
        username = yee.cleaned_data['username']
        password = yee.cleaned_data['password']

        self.user = Member.objects.create(username=username, password=password)


    # Registering users are added to the user/member database
    def test_successful_member_registration(self):
        coco = Member.objects.get(username='tyrone35', password='pirates2016')
        self.assertTrue(coco)

    # Member defaulted to None upon registration
    def test_new_member_default_status(self):
        self.assertEqual(self.user.status, "None")


    # Successful registration redirects to home page


    # Unsuccessful registration...





# TEMPLATES


# MODELS


# URLConf