from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate

from member.forms import BecomeCoachForm, MemberRegisterForm, MemberLoginForm
from member.models import Member, Space, MemberSpace



def register(request):
    form = MemberRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.link_code = get_user_model().objects.make_random_password()
            user.save()

            # ADD automatic login and redirect to homepage

            return redirect(reverse('home'))
    form = MemberRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def member_login(request):
    form = MemberLoginForm(request.POST)
    if request.method == 'POST':
        username = form.data['username']
        password = form.data['password']
        member = authenticate(username=username, password=password)
        if member:
            if member.is_active:
                login(request, member)
                return redirect(reverse('home'))
            else:
                # user is not active
                pass
        else:
            messages.add_message(request, messages.ERROR, 'incorrect credentials')
            return redirect(reverse('member_login'))
    form = MemberLoginForm()
    context = {
        'form': form,
        'total_members': get_user_model().objects.count(),
    }
    return render(request, 'login.html', context)


def member_logout(request):
    print('before logout')
    logout(request)
    print('after logout')
    return redirect(reverse('member_login'))


def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse('member_login'))
    member = request.user
    context = {
        'member': member,
    }
    return render(request, 'home.html', context)


def become_coach(request):
    if not request.user.is_authenticated:
        return redirect(reverse('member_login'))
    form = BecomeCoachForm(request.POST)
    member = get_user_model().objects.get(username=request.user.username)
    if request.method == 'POST':
        if form.is_valid():
            key_code = form.cleaned_data['key_code']
            if key_code in settings.KEY_CODES:
                member.status = 'Coach'
                member.save()
                new_space = Space.objects.create(name='{}\'s Space'.format(member.username))
                new_member_space = MemberSpace.objects.create(member=member, space=new_space)
                new_space.save()
                new_member_space.save()
                messages.add_message(request, messages.ERROR, 'You just became a Coach!')
                return redirect(reverse('home'))
            else:
                messages.add_message(request, messages.ERROR, 'Incorrect Passcode!')
    form = BecomeCoachForm()
    context = {
        'form': form
    }
    return render(request, 'member/become_coach.html', context)