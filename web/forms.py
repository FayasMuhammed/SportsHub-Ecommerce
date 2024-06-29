from django import forms

from web.models import User




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

    
       