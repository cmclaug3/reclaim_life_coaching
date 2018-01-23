from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse

from member.forms import BecomeCoachForm, MemberRegisterForm, MemberLoginForm
from member.models import Member, Space, MemberSpace

from coaching.forms import ClientJoinCoachForm



def coaching_home(request):
    if not request.user.is_authenticated:
        return redirect(reverse('member_login'))
    member = get_user_model().objects.get(username=request.user.username)
    spaces = member.get_spaces
    context = {
        'member': member,
        'spaces': spaces,
    }
    return render(request, 'coaching/coaching_home.html', context)


def client_join_coach_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('member_login'))
    form = ClientJoinCoachForm(request.POST)
    member = get_user_model().objects.get(username=request.user.username)
    if request.method == 'POST':
        if form.is_valid():
            coach_username = form.cleaned_data['coach_username']
            coach_link_code = form.cleaned_data['coach_link_code']

            # need error handling here in case form coach_username doent match a user
            coach = get_user_model().objects.get(username=coach_username)

            coach_space = coach.get_spaces()[0]
            if coach.status != 'Coach':
                messages.add_message(request, messages.ERROR, 'Not the right type of user')
                return redirect(reverse('home'))
            if coach.link_code == coach_link_code:
                new_member_space = MemberSpace.objects.create(member=member, space=coach_space)
                member.status = 'Client'
                member.save()
                new_member_space.save()
                messages.add_message(request, messages.ERROR, 'You just Joined a Coach!!!')
                return redirect(reverse('home'))
            else:
                print('creds didnt match')
                messages.add_message(request, messages.ERROR, 'Creds didnt match')
                return redirect(reverse('home'))
        else:
            print('form was not valid')

    form = ClientJoinCoachForm()
    context = {
        'form': form,
    }
    return render(request, 'coaching/client_join_coach_view.html', context)