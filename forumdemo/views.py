from django.shortcuts import render
from block.models import Block

from message.models import Message


def index(request):
    block_infos = Block.objects.filter(status=0).order_by("-id")
    owner = request.user
    if request.user.is_authenticated():
        msg_cnt = Message.objects.filter(owner=owner, status=0).count()
    else:
        msg_cnt = 0
    return render(request, "index.html", {"blocks": block_infos, "msg_cnt": msg_cnt})
