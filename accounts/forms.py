from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
import datetime


BLOOD_CHOICES = (
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

District = (
    ('Terhathum', 'Terhathum'),
    ('Taplejung', 'Taplejung'),
    ('Gulmi', 'Gulmi'),
    ('Panchthar', 'Panchthar'),
    ('Ilam', 'Ilam'),
    ('Jhapa', 'Jhapa'),
    ('Morang', 'Morang'),
    ('Sunsari', 'Sunsari'),
    ('Dhankutta', 'Dhankutta'),
    ('Sankhuwasabha', 'Sankhuwasabha'),
    ('Bhojpur', 'Bhojpur'),
    ('Okhaldunga', 'Okhaldunga'),
    ('Khotang', 'Khotang'),
    ('Solukhumbu', 'Solukhumbu'),
    ('Udaypur', 'Udaypur'),
    ('Saptari', 'Saptari'),
    ('Siraha', 'Siraha'),
    ('Dhanusa', 'Dhanusa'),
    ('Mahottari', 'Mahottari'),
    ('Sarlahi', 'Sarlahi'),
    ('Sindhuli', 'Sindhuli'),
    ('Ramechhap', 'Ramechhap'),
    ('Dolkha', 'Dolkha'),
    ('Sindhupalchauk', 'Sindhupalchauk'),
    ('Kavreplanchauk', 'Kavreplanchauk'),
    ('Lalitpur', 'Lalitpur'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Kathmandu', 'Kathmandu'),
    ('Nuwakot', 'Nuwakot'),
    ('Rasuwa', 'Rasuwa'),
    ('Dhading', 'Dhading'),
    ('Makwanpur', 'Makwanpur'),
    ('Rauthat', 'Rauthat'),
    ('Bara', 'Bara'),
    ('Parsa', 'Parsa'),
    ('Chitwan', 'Chitwan'),
    ('Ghorkha', 'Ghorkha'),
    ('Lamjung', 'Lamjung'),
    ('Tanahu', 'Tanahu'),
    ('Syangja', 'Syangja'),
    ('Kaski', 'Kaski'),
    ('Manag', 'Manag'),
    ('Mustang', 'Mustang'),
    ('Parwat', 'Parwat'),
    ('Myagdi', 'Myagdi'),
    ('Baglung', 'Baglung'),
    ('Palpa', 'Palpa'),
    ('Purba NawalParasi', 'Purba NawalParasi'),
    ('Paschim NawalParasi', 'Paschim NawalParasi'),
    ('Rupandehi', 'Rupandehi'),
    ('Arghakhanchi', 'Arghakhanchi'),
    ('Kapilvastu', 'Kapilvastu'),
    ('Pyuthan', 'Pyuthan'),
    ('Rolpa', 'Rolpa'),
    ('Purba Rukum', 'Purba Rukum'),
    ('Paschim Rukum', 'Paschim Rukum'),
    ('Salyan', 'Salyan'),
    ('Dang', 'Dang'),
    ('Bardiya', 'Bardiya'),
    ('Surkhet', 'Surkhet'),
    ('Dailekha', 'Dailekha'),
    ('Banke', 'Banke'),
    ('Jajarkot', 'Jajarkot'),
    ('Dolpa', 'Dolpa'),
    ('Humla', 'Humla'),
    ('Kalikot', 'Kalikot'),
    ('Mugu', 'Mugu'),
    ('Jumla', 'Jumla'),
    ('Bajura', 'Bajura'),
    ('Bajhang', 'Bajhang'),
    ('Aachham', 'Aachham'),
    ('Doti', 'Doti'),
    ('Kailali', 'Kailali'),
    ('Kanchanpur', 'Kanchanpur'),
    ('Dadeldhura', 'Dadeldhura'),
    ('Baitadi', 'Baitadi'),
    ('Darchula', 'Darchula'),
)


class SignUpForm(UserCreationForm):  # forms.Form
    """ first_name = forms.CharField(widget=forms.TextInput)
    middle_name = forms.CharField(widget=forms.TextInput, required=False)
    last_name = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    #address = 
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':''}))
    #BloodGroup = forms.ChoiceField(choices=BLOOD_CHOICES, widget=forms.Select(attrs={'class':'','id':'exampleFormControlSelect2'}))
    last_donate_date = forms.DateTimeField(input_formats=['%Y-%m-%d'], widget=forms.DateTimeInput(format='%Y-%m-%d',attrs={'placeholder':'year-month-day','value':datetime.date.today()-datetime.timedelta(days=100)}))
    # #district = forms.CharField(widget=forms.TextInput)#forms.ModelChoiceField(queryset=User.objects.values_list('district', flat=True).distinct(), empty_label=None, to_field_name="district")
    # municipality = forms.CharField(widget=forms.TextInput)#forms.ModelChoiceField(queryset=User.objects.values_list('municipality', flat=True).distinct(), empty_label=None, to_field_name="municipality")
 """

    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions','last_login','password', 'donation_no',
                   'date_joined']


#class Profile_update(models.Model):
class Profile_update(UserChangeForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # phone = forms.CharField(required= False)
    # district =  forms.ChoiceField(choices=district, widget=forms.Select(attrs={'id': 'id_District'}))#forms.ModelChoiceField(queryset=User.objects.values_list('district', flat=True).distinct(), empty_label=None, to_field_name="district")
    # municipality = forms.CharField(widget=forms.TextInput)#forms.ModelChoiceField(queryset=User.objects.values_list('municipality', flat=True).distinct(), empty_label=None, to_field_name="municipality")
    # last_donate_date = forms.CharField(required= False)
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'password', 'donation_no',
                   'date_joined']
