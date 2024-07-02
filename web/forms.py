from django import forms

from web.models import User

from django.contrib.auth.forms import UserChangeForm,SetPasswordForm

from django.contrib.auth import password_validation






class UserRegistration_form(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","first_name","last_name","email","password"]

        widgets={
            'username':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Username"}),
            'first_name':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your First Name"}),
            'last_name':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Last Name"}),
            'email':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Email"}),
            'password':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Password"})
            }
        
class UserLogin_form(forms.Form):

    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Username"}))

    password=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your password"}))

    
class UpdateUser_form(UserChangeForm):

    password=None

    class Meta:

        model=User

        fields=["username","first_name","last_name","email"]

        read_only_fields=["password"]

        widgets={
            'username':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Username"}),
            'first_name':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your First Name"}),
            'last_name':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Last Name"}),
            'email':forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Your Email"}),
        }
       
class ChangeUserPassword_form(SetPasswordForm):

    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","placeholder":"Enter your new password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control","placeholder":"Re-Enter your new password"}),
    )


