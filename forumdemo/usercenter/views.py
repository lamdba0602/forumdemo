from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import os
from forumdemo.settings import portrait_root
from forumdemo.settings import portrait_url


@login_required
def portrait_upload(request):
    if request.method == "GET":
        return render(request, "portrait_upload.html")
    else:
        profile = request.user.userprofile
        portrait_file = request.FILES.get("portrait", None)
        file_path = os.path.join(portrait_root,
                portrait_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in portrait_file.chunks():
                destination.write(chunk)
        url = "%s/%s" % (portrait_url, portrait_file.name)
        profile.portrait = url
        profile.save()
        return redirect("/")
