from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth import login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from auth_app.forms import registerform
# Create your views here.

class base(View):
    def get(self,request,*args, **kwargs):
        return render(request,'base.html')

class register_view(View):
    def get(self,request,*args, **kwargs):
        form=registerform()
        return render(request,'register.html',{'form':form})
    
    def post(self,request,*args, **kwargs):
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
class login_view(View):
    def get(self,request,*args, **kwargs):
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,*args, **kwargs):
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'login.html',{'form':form,'invalid':'invalid username or passowrd'})

class password_reset(View):
    @method_decorator(login_required(login_url='login'))
    def get(self,request,*args, **kwargs):
        form=PasswordChangeForm(user=request.user)
        return render(request,'password_reset.html',{'form':form})

    def post(self,request,*args, **kwargs):
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            form.save()
            return redirect('dashboard')

class dashboard_view(View):
    @method_decorator(login_required(login_url='login'))
    def get(self,request,*args, **kwargs):
        return render(request,'dashboard.html')

@login_required(login_url='login')
def logout__view(reuqest):
    logout(reuqest)
    return redirect('login')