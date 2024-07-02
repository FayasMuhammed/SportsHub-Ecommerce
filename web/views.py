from django.shortcuts import render,redirect

from django.views.generic import View,DeleteView

from web.forms import UserRegistration_form,UserLogin_form,UpdateUser_form,ChangeUserPassword_form

from web.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from django.urls import reverse_lazy

from django.utils.decorators import method_decorator


# def Login_required(fn):

#     def wrapper(request,**kwargs):

#         if not request.user.is_authenticated:

#             return redirect("ulog")
        
#         else:

#             return fn(request,**kwargs)
        
#     return wrapper

# @method_decorator(Login_required,name="dispatch")
class Home_view(View):

    def get(self,request,*args,**kwargs):
        
        return render(request,"home.html")


class UserRegistration_view(View):

    def get(self,request,*args,**kwargs):

        form=UserRegistration_form()

        return render(request,"UserRegistration.html",{"form":form})
    

    def post(self,request,*args,**kwargs):

        form=UserRegistration_form(request.POST)

        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)

            form=UserRegistration_form()
        
        return redirect("ulog")



class UserLogin_view(View):

    def get(self,request,*args,**kwargs):

        form=UserLogin_form()

        return render(request,"UserLogin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        form=UserLogin_form(request.POST)

        if form.is_valid():

            u_name=form.cleaned_data.get("username")

            pwd=form.cleaned_data.get("password")

            user_obj=authenticate(username=u_name,password=pwd)

            print(user_obj)
            
            if user_obj:

                login(request,user_obj)
                form=UserLogin_form()

            # messages.success(request,"Login Successfull")======================>add message at last

                return redirect("home") #redirect page home page aakkanam

            else:

                messages.warning(request,"Username or Password is incorrect")

                return redirect("ulog")


                


            

class UserLogout_view(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("ulog") #login button vechittilla
    

class UserProfileUpdate_view(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        data=User.objects.get(id=id)

        form=UpdateUser_form(instance=data)

        return render(request,"UserUpdate.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        data=User.objects.get(id=id)

        form=UpdateUser_form(request.POST,instance=data)

        if form.is_valid():

            form.save()
        
        form=UpdateUser_form()

        messages.success(request,"Profile has been successfully updated")

        return redirect("home")
        

class ChangeUserPassword_view(View):

    def get(self,request,*args,**kwargs):

        # id=kwargs.get("pk")

        # data=User.objects.get(id=id)

        form=ChangeUserPassword_form(request.user)

        return render(request,"ChangeUserPassword.html",{"form":form})
    
    def post(self,request,*args,**kwargs):

        form=ChangeUserPassword_form(request.user , request.POST)

        if form.is_valid():

            form.save()

            messages.success(request,"Password has been successfully updated, Please Login Again")

            return redirect("ulog")

        else:

            messages.error(request,form.errors)

            form=ChangeUserPassword_form(user=request.user)

            return render(request,"ChangeUserPassword.html",{"form":form})
        
        
    

class UserProfileDelete(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        User.objects.get(id=id).delete()

        messages.success(request,"Account was Deleted")

        return redirect("ulog")
