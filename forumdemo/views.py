from django.shortcuts import render
from block.models import Block

from message.models import Message


def index(request):
    block_infos = Block.objects.filter(status=0).order_by("-id")
    owner = request.user
    messages = Message.objects.filter(owner=owner, status=0)
    msg_cnt = messages.count()
    return render(request, "index.html", {"blocks": block_infos, "msg_cnt": msg_cnt})
