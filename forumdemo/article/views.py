from django.shortcuts import redirect
from django.shortcuts import render
from django.core.paginator import Paginator

from article.forms import ArticleForm
from article.models import Article
from block.models import Block


def article_list(request, block_id):
    ARTICLE_CNT_1PAGE = 1
    page_no = int(request.GET.get("page_no", "1"))
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    p = Paginator(articles_objs, ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    articles_objs = page.object_list
    page_links = [i for i in range(page_no - 5, page_no + 6) if i > 0 and i <= p.num_pages]
    return render(request, "article_list.html", {"articles": articles_objs, "b": block, "page_no": page_no,
        "page_cnt": p.num_pages, "page_links": page_links, "previous_link": page_links[0] - 1,
        "next_link": page_links[-1] + 1, "has_previous": page_links[0] - 1 > 0,
        "has_next": page_links[-1] + 1 <= p.num_pages,
        "next_page": page_no + 1, "previous_page": page_no - 1})


def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request, "article_create.html", {"b": block, "form": form})


def article_detail(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)

    return render(request, "article_detail.html", {"article": article})
