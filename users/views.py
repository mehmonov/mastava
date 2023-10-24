from django.shortcuts import redirect, render
from django.views import View
from .forms  import LoginForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages

# Create your views here.


class LoginUser(View):
   
    def get(self, request):
        form = LoginForm
        
        if not self.request.user.is_authenticated:
            return render(request, 'user/login.html', {"form":form})
        else:
            return redirect("profileuser")
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                auth_login(request, user)
                return redirect("profileuser")
            else:
                messages.error(request, "Invalid login or password")
                return render(request, 'user/login.html', {"form": form})
        else:
            return redirect('loginuser')
        
        
class Profile(View):
    
    def get(self, request):
        
        return render(request, 'user/profile.html')