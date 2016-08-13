from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm


def User_register(request):
    if request.method == "GET":
        return render(request, "User_register.html")
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
            user.is_active = False
            user.save()
            return redirect("/activate?id=%s" % user.id)
        else:
            return render(request, "User_register.html", {"form": form})


def User_login(request):
    return render(request, "User_login.html")
