from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import json
from article.models import Article
from .forms import CommentForm
from .models import Comment


@login_required
def comment_create(request):
    article_id = request.POST["article_id"]
    article = Article.objects.get(id=article_id)
    to_comment_id = int(request.POST.get("to_comment_id", 0))
    if to_comment_id != 0:
        to_comment = Comment.objects.get(id=to_comment_id)
    else:
        to_comment = None

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.owner = request.user
        comment.article = article
        comment.to_comment = to_comment
        comment.save()
        return json_response({"status": "ok", "msg": ""})
    else:
        msg = ""
        for field in form:
            if field.errors:
                for error in field.errors:
                    msg += error
        return json_response({"status": "error", "msg": msg})


def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)
