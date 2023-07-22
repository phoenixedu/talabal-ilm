from django import forms
from django_countries.fields import CountryField
from django.contrib.auth.forms import UserCreationForm
from .models import GenUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class GenUserForm(UserCreationForm):
    country = CountryField().formfield()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = GenUser
        fields = ['username', 'first_name', 'last_name','password1', 'password2', 'father_name', 'PhoneNumber',
                  'email', 'picture', 'cnic', 'DOB', 'country', 'sex']
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = GenUser 
        fields = ['username', 'password']

class editUserInfoGenUser(forms.ModelForm):
    class Meta:
        model = GenUser
        fields = [ 'first_name', 'last_name', 'PhoneNumber',
                  'email', 'picture',  'sex']
    
    def save(self, commit=True):
        gen_user = super(editUserInfoGenUser, self).save(commit=commit)
        user = gen_user.user
        User = get_user_model()
        user_model_instance = User.objects.get(pk=user.pk)
        user_model_instance.username = gen_user.username
        user_model_instance.first_name = gen_user.first_name
        user_model_instance.last_name = gen_user.last_name
        user_model_instance.email = gen_user.email
        if commit:
            user_model_instance.save()

        return gen_user







    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     if self.has_changed():
    #         if 'email' in self.changed_data:
    #             instance.emailConformation = False 
    #             User = get_user_model()
    #             try:
    #                 user = User.objects.get(email=instance.email)
    #                 user.email = instance.email
    #                 user.save()
    #             except User.DoesNotExist:
    #                 user = User.objects.get(username=instance.username)
    #                 user.email = instance.email
    #                 user.save()
    #         if 'first_name' in self.changed_data:
    #             instance.first_nameConformation = False 
    #             User = get_user_model()
    #             try:
    #                 user = User.objects.get(email=instance.email)
    #                 user.first_name = instance.first_name
    #                 user.save()
    #             except User.DoesNotExist:
    #                 user = User.objects.get(username=instance.username)
    #                 user.first_name = instance.first_name
    #                 user.save()
    #         if 'last_name' in self.changed_data:
    #             instance.last_nameConformation = False 
    #             User = get_user_model()
    #             try:
    #                 user = User.objects.get(email=instance.email)
    #                 user.last_name = instance.last_name
    #                 user.save()
    #             except User.DoesNotExist:
    #                 user = User.objects.get(username=instance.username)
    #                 user.last_name = instance.last_name
    #                 user.save()
    #         if 'username' in self.changed_data:
    #             instance.usernameConformation = False
    #             User = get_user_model()
    #             try:
    #                 user = User.objects.get(username=instance.username)
    #                 user.username = instance.username
    #                 user.save()
    #             except User.DoesNotExist:
    #                 user = User.objects.get(email=instance.email)
    #                 user.username = instance.username
    #                 user.save()
    #         if 'PhoneNumber' in self.changed_data:
    #             instance.PhoneNumberConformation = False
        
    #     if commit:
    #         instance.save()
    #         if 'email' in self.changed_data or 'username' in self.changed_data:
    #             user.save()

    #     return instance

       
