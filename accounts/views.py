from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserChangeForm
from accounts.forms import SignUpForm, Profile_update

from .models import User

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # creating user
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            # taking input from user
            user.raw_password = form.cleaned_data.get('password1')
            user.first_name = form.cleaned_data['first_name']
            user.middle_name = form.cleaned_data['middle_name']
            user.last_name = form.cleaned_data['last_name']
            user.contact_mail = form.cleaned_data['email']
            user.bloodgroup = form.cleaned_data['bloodgroup']
            user.phone = form.cleaned_data['phone']
            user.last_donate_date = form.cleaned_data['last_donate_date']
            user.address = form.cleaned_data['address']
            """ user.municipality = form.cleaned_data['municipality']
            user.district = form.cleaned_data['district'] """
            user.is_staff = False
            # save user data
            user.save()
            raw_password = form.cleaned_data.get('password1')
            # login user
            user = authenticate(username=user.email, password=raw_password)
            # giving promission
            # my_group = Group.objects.get(name='Donor')
            # my_group.user_set.add(user)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    # donner = User.objects.filter(id=request.user.id).get()
    return render(request, 'registration/profile.html')  # , {'donner':donner})


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = Profile_update(request.POST, instance=request.user)
        if form.is_valid():
            user = request.user
            user.municipality = form.cleaned_data['municipality']
            user.district = form.cleaned_data['district']
            if form.cleaned_data['last_donate_date'] != '':
                user.last_donate_date = form.cleaned_data['last_donate_date']
                user.donation_no = user.donation_no + 1
            if form.cleaned_data['phone'] != '':
                user.phone = form.cleaned_data['phone']
            form.save()
            return redirect('profile')
    else:
        form = Profile_update(instance=request.user)
    return render(request, 'registration/profile_update.html', {'form': form})


@login_required
def backup(request):
    # donner = User.objects.filter(id=request.user.id).get()
    return render(request, 'registration/profile.html')  # , {'donner':donner})


@login_required
def del_user(request, username):
    try:
        u = User.objects.get(email=username)
        u.is_active = False
        u.save()
        #messages = {'success': 'Your account delete successfully'}
        return redirect('/')
    except User.DoesNotExist:
        #messages = {'error': 'Your account doesn\'t found' }
        return redirect('/accounts/login/')
    except Exception as e:
        return render(request, 'front.html', {'error': e.message})
    return redirect('/accounts/login/')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})
