from django import forms
from accounts.models import User

BLOOD_CHOICES = (
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
)

district =(
    ('Achham', 'Achham'),
    ('Arghakhanchi', 'Arghakhanchi'),
    ('Baglung', 'Baglung'),
    ('Baitadi', 'Baitadi'),
    ('Bajhang', 'Bajhang'),
    ('Bajura', 'Bajura'),
    ('Banke', 'Banke'),
    ('Bara', 'Bara'),
    ('Bardiya', 'Bardiya'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Bhojpur', 'Bhojpur'),
    ('Chitwan', 'Chitwan'),
    ('Dadeldhura', 'Dadeldhura'),
    ('Dailekha', 'Dailekha'),
    ('Dang', 'Dang'),
    ('Darchula', 'Darchula'),
    ('Dhading', 'Dhading'),
    ('Dhankuta', 'Dhankuta'),
    ('Dhanusa', 'Dhanusa'),
    ('Dolakha', 'Dolakha'),
    ('Dolpa', 'Dolpa'),
    ('Doti', 'Doti'),
    ('Gorkha', 'Gorkha'),
    ('Gulmi', 'Gulmi'),
    ('Humla', 'Humla'),
    ('Ilam', 'Ilam'),
    ('Jajarkot', 'Jajarkot'),
    ('Jhapa', 'Jhapa'),
    ('Jumla', 'Jumla'),
    ('Kailali', 'Kailali'),
    ('Kalikot', 'Kalikot'),
    ('Kanchanpur', 'Kanchanpur'),
    ('Kapilvastu', 'Kapilvastu'),
    ('Kaski', 'Kaski'),
    ('Kathmandu', 'Kathmandu'),
    ('Kavrepalanchok', 'Kavrepalanchok'),
    ('Khotang', 'Khotang'),
    ('Lalitpur', 'Lalitpur'),
    ('Lamjung', 'Lamjung'),
    ('Mahottari', 'Mahottari'),
    ('Makwanpur', 'Makwanpur'),
    ('Manang', 'Manang'),
    ('Morang', 'Morang'),
    ('Mugu', 'Mugu'),
    ('Mustang', 'Mustang'),
    ('Myagdi', 'Myagdi'),
    ('NawalParasi', 'NawalParasi'),
    ('Nawalpur', 'Nawalpur'),
    ('Nuwakot', 'Nuwakot'),
    ('Okhaldunga', 'Okhaldunga'),
    ('Palpa', 'Palpa'),
    ('Panchthar', 'Panchthar'),
    ('Parbat', 'Parbat'),
    ('Parsa', 'Parsa'),
    ('Paschim Rukum', 'Paschim Rukum'),
    ('Purbi Rukum', 'Purbi Rukum'),
    ('Pyuthan', 'Pyuthan'),
    ('Ramechhap', 'Ramechhap'),
    ('Rasuwa', 'Rasuwa'),
    ('Rautahat', 'Rautahat'),
    ('Rolpa', 'Rolpa'),
    ('Rupandehi', 'Rupandehi'),
    ('Salyan', 'Salyan'),
    ('Sankhuwasabha', 'Sankhuwasabha'),
    ('Saptari', 'Saptari'),
    ('Sarlahi', 'Sarlahi'),
    ('Sindhuli', 'Sindhuli'),
    ('Sindhupalchok', 'Sindhupalchok'),
    ('Siraha', 'Siraha'),
    ('Solukhumbu', 'Solukhumbu'),
    ('Sunsari', 'Sunsari'),
    ('Surkhet', 'Surkhet'),
    ('Syangja', 'Syangja'),
    ('Tanahu', 'Tanahu'),
    ('Taplejung', 'Taplejung'),
    ('Terhathum', 'Terhathum'),
    ('Udayapur', 'Udayapur'),
    )



class DonorForm(forms.Form):
	BloodGroup = forms.ChoiceField(required = False, choices=BLOOD_CHOICES, widget=forms.Select())
	District = forms.ChoiceField(choices=district, widget=forms.Select(attrs={'id': 'id_District'}))
	Municipality = forms.ChoiceField(required = False, widget=forms.Select(attrs={'class':'', 'id': 'id_Municipality'}))
	
	class Meta:
                fields = ['BloodGroup','District', 'Municipality']



class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


    class Meta:
                fields = ['name','email','subject','comment']




class MailForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    time = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
                fields = ['name','phone','location','time']


class AjaxChoiceField(forms.ChoiceField):
    def valid_value(self, value):
        return True
