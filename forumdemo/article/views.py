from django.shortcuts import redirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from article.forms import ArticleForm
from article.models import Article
from block.models import Block


def article_list(request, block_id):
    ARTICLE_CNT_1PAGE = 1
    page_no = int(request.GET.get("page_no", "1"))
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    page_articles, pagination_data = paginate_queryset(articles_objs, page_no, ARTICLE_CNT_1PAGE)

    return render(request, "article_list.html", {"articles": page_articles, "b": block,
                                                 "pagination_data": pagination_data})


def paginate_queryset(objs, page_no, cnt_per_page=10, half_show_length=5):
    p = Paginator(objs, cnt_per_page)
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no <= 0:
        page_no = 1

    page_links = [i for i in range(page_no - half_show_length, page_no + half_show_length + 1)
                  if i > 0 and i <= p.num_pages]
    page = p.page(page_no)
    previous_link = page_links[0] - 1
    next_link = page_links[-1] + 1
    pagination_data = {"page_cnt": p.num_pages,
                       "page_no": page_no,
                       "page_links": page_links,
                       "previous_link": previous_link,
                       "next_link": next_link,
                       "has_previous": previous_link > 0,
                       "has_next": next_link <= p.num_pages}
    return (page.object_list, pagination_data)


@login_required
def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
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
