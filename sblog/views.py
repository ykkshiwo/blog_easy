from django.template import Template, Context
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from sblog.models import Blog
from django.http import Http404


def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "sblog/blog_list.html", {"blogs": blogs})


def blog_show(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render(request, "sblog/blog_show.html", {"blog": blog})