from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import os


@login_required
def portrait_upload(request):
    if request.method == "GET":
        return render(request, "portrait_upload.html")
    else:
        profile = request.user.userprofile
        portrait_file = request.FILES.get("portrait", None)
        file_path = os.path.join("/Users/mingdang1/Documents/userres/portrait",
                portrait_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in portrait_file.chunks():
                destination.write(chunk)
        url = "http://forumdemo.com:8080/portrait/%s" % portrait_file.name
        profile.portrait = url
        profile.save()
        return redirect("/")
