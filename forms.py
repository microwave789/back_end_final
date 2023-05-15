from django import forms 
from .models import Voucher 
from django.utils import timezone 
from datetime import time 
from django import forms 
from .models import Voucher 
from datetime import date
from django.urls import reverse
from .models import BookTable
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Comment

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):              
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)        
    class Meta:        
        model = Comment
        fields = ['name', 'comment']    
    def clean_name(self):        
        """Make sure people don't use my name"""
        data:str = self.cleaned_data['name']        
        if not self.request.user.is_authenticated and data.lower().strip() == 'samuel':
            raise ValidationError("Sorry, you cannot use this name.")
        return data


class VoucherForm(forms.ModelForm): 
    class Meta: 
        model = Voucher 
        fields = ['menu', 'number_of_guests', 'date', 'time', 'name_and_surname', 'email_address', 'telephone'] 
        labels = { 
            'menu': 'Menu', 
            'number_of_guests': 'Number of guests', 
            'date': 'Date', 
            'time': 'Time', 
            'name_and_surname': 'Name and Surname', 
            'email_address': 'Email Address', 
            'telephone': 'Telephone', 
        } 
    def clean_number_of_guests(self): 
        number_of_guests = int(self.cleaned_data['number_of_guests']) 
        if number_of_guests > 750: 
            raise forms.ValidationError("Number of guests cannot exceed 750.") 
        return number_of_guests 
     
     
    def clean_time(self): 
        time_value = self.cleaned_data['time'] 
        if time_value > time(hour=23): 
            raise forms.ValidationError("Time cannot be later than 23:00.") 
        return time_value 
 
    def clean_date(self): 
        date = self.cleaned_data['date'] 
        if date < timezone.now().date(): 
            raise forms.ValidationError("The selected date is in the past.") 
        return date 
     
    def clean_telephone(self): 
        telephone = self.cleaned_data['telephone'] 
        if not telephone.isdigit(): 
            raise forms.ValidationError("Telephone number must contain only digits.") 
        return telephone



  
class BookTableForm(forms.ModelForm): 
    class Meta: 
        model = BookTable 
        fields = ['first_name', 'last_name', 'phone', 'email', 'message'] 
 
 
    def clean_phone(self): 
        phone = self.cleaned_data['phone'] 
        if not phone.isdigit(): 
            raise forms.ValidationError("Phone number must contain only digits.") 
        return phone
