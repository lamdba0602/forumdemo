from django.shortcuts import redirect
from django.shortcuts import render

from .models import Message


def message_list(request):
    owner = request.user
    messages = Message.objects.filter(owner=owner, status=0).order_by("-id")
    return render(request, "message_list.html", {"messages": messages})


def message_read(request, message_id):
    message = Message.objects.get(id=message_id)
    message.status = -1
    message.save()

    return redirect(message.link)
