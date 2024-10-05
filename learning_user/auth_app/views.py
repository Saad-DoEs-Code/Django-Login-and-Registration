from django.shortcuts import render
from auth_app.forms import UserForm, UserProfileInfoForm

# Imports for Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.



def index(request):
    context = {}
    return render(request, "auth_app/index.html", context=context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_app:index'))

@login_required
def special(request):
    return HttpResponse("You Logged In")

def register(request):

    is_registered = False
    if is_registered == False and request.method == "POST":
        user = UserForm(request.POST)
        user_profile = UserProfileInfoForm(request.POST)
        if user.is_valid() and user_profile.is_valid():
            user = user.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile.save(commit=False)
            user_profile.user = user
            if "profile_picture" in request.FILES:
                user_profile.profile_picture = request.FILES['profile_picture']
            user_profile.save()
            is_registered = True
        else:
            print(user.errors, user_profile.errors)

    else:
        user = UserForm()
        user_profile = UserProfileInfoForm()

    context_dict = {"user_form": user,
                    "user_profile_form": user_profile, "is_registered": is_registered}
    return render(request, "auth_app/register.html", context=context_dict)


def user_login(request):
    if request.method == "POST":
        # get("name_of_tag")
        username = request.POST.get('username')
        password = request.POST.get("password")

        user = authenticate(username= username, password= password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('auth_app:index'))
            else:
                return HttpResponse("Account not active")
            
        else:
            print("Someone tried to login and failed")
            print(f"username: {username}, password {password}")
            return HttpResponse("Invalid Credentials")
        
    else:
        return render(request, "auth_app/login.html")
    