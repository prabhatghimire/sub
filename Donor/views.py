from graphene_django.views import GraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from Donor.forms import DonorForm, FeedbackForm, MailForm
from Donor.models import Feedback, Event
from accounts.models import User, Location
from django.db.models import Q
import datetime
from django.http import JsonResponse
from django.core.mail import send_mail
#from django.views.generic.detail import DetailView


# home page to display blood request form and donner list on post request
def home(request):
    form = DonorForm()
    if request.is_ajax():  # Ajax request
        district = request.GET.get('District', None)
        data = {'result': list(Location.objects.filter(
            district__icontains=district).values('municipality').distinct())}
        return JsonResponse(data)
    elif request.method == 'POST':  # post request
        form = DonorForm(request.POST)
        municipality = request.POST.get('Municipality')
        form.fields['Municipality'].choices = [(municipality, municipality)]
        if form.is_valid():
            BloodGroup = form.cleaned_data['BloodGroup']
            district = form.cleaned_data['District']
            municipality = form.cleaned_data['Municipality']
            address = Location.objects.get(
                district__icontains=district, municipality__icontains=municipality).id
            require_date = datetime.date.today() - datetime.timedelta(days=100)
            result = User.objects.all().filter(Q(bloodgroup__icontains=BloodGroup)
                                               & Q(last_donate_date__lte=require_date) & Q(address=address))
            return render(request, 'donner/donnerlist.html', {'result': result})
        return render(request, 'donner/home.html', {'error': form.errors, 'form': form})
    else:  # get request
        return render(request, 'donner/home.html', {'form': form})


# display feedback form and on post request store feedback form on database
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            comment = form.cleaned_data['comment']
            Feedback.objects.create(
                name=name, email=email, subject=subject, comment=comment)
            message = 'Thank you {0} for your valuable time and comment we will see through your commentvand try to improve'.format(
                name)
            mail_from = 'prabhu10612@gmail.com'
            mail = tuple(list(User.objects.filter(
                is_staff=True).values('email').distinct()))
            send_mail(subject, message, mail_from, mail, fail_silently=False,)
            return render(request, 'donner/feedback return.html', {'name': name})
    else:
        form = FeedbackForm()
        return render(request, 'donner/Feedback.html', {'form': form})



# dispaly about page
def about(request):
    return render(request, 'donner/About Us.html')


# display conatact us page
def contact(request):
    return render(request, 'donner/contact Us.html')


def newsView(request, pk):
    news = Event.objects.all().get(pk=pk)
    return render(request, 'donner/news.html', {'news':news})
