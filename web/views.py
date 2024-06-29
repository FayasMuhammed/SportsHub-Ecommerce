from django.shortcuts import render,redirect

from django.views.generic import View

from web.forms import UserRegistration_form,UserLogin_form

from web.models import User

from django.contrib.auth import authenticate,login,logout




class UserRegistration_view(View):

    def get(self,request,*args,**kwargs):

        form=UserRegistration_form()

        return render(request,"UserRegistration.html",{"form":form})
    

    def post(self,request,*args,**kwargs):

        form=UserRegistration_form(request.POST)

        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)

            form=UserRegistration_form()
        
        return render(request,"UserRegistration.html",{"form":form})



class UserLogin_view(View):

    def get(self,request,*args,**kwargs):

        form=UserLogin_form()

        return render(request,"UserLogin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        form=UserLogin_form(request.POST)

        if form.is_valid():

            u_name=form.cleaned_data.get("username")

            pwd=form.cleaned_data.get("pasword")

            user_obj=authenticate(usename=u_name,password=pwd)

            if user_obj:

                login(request,user_obj)

                print("valid credentials")
            
            form=UserLogin_form()

            return redirect("ureg") #redirect page home page aakkanam


