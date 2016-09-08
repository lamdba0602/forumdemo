from django.shortcuts import render
from django.http import HttpResponse

import json
from article.models import Article
from .forms import CommentForm


def comment_create(request):
    article_id = request.POST["article_id"]
    article = Article.objects.get(id=article_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.owner = request.user
        comment.article = article
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
