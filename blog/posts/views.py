from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.db.models import Q

# Create your views here.
from .forms import PostForm
from .models import Post


#create
def post_create(request):

    if not request.user.is_authenticated():
        return(redirect("posts:post_timeline"))

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.POST and request.user.is_authenticated():

        instance = form.save(commit=False)
        instance.post_author = request.user
        instance.save()
        
        return(HttpResponseRedirect(instance.get_absolute_url()))

    if request.user.is_authenticated():
        context = {
            "form": form,
        }

        return render(request, "post_form.html", context)


def post_edit(request, post_id = None):

    if not request.user.is_authenticated():
        return(redirect("posts:post_timeline"))
    
    instance = get_object_or_404(Post, id = post_id)

    form = PostForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid() and request.POST and request.user.is_authenticated():
        instance = form.save()

        return(HttpResponseRedirect(instance.get_absolute_url()))
    
    if request.user.is_authenticated():
        context = {
            "title": instance.post_title,
            "instance": instance,
            "form": form,
        }    

        return render(request, "post_edit.html", context)


def post_delete(request, post_id = None):
    instance = get_object_or_404(Post, id=post_id)

    if request.user.is_authenticated():
        instance.delete()
        return(redirect("posts:post_timeline"))

    else:
        return(HttpResponseRedirect(instance.get_absolute_url()))


def post_display(request, post_id=None):
    instance = get_object_or_404(Post, id = post_id)
    context = {
        "title": instance.post_title,
        "instance": instance,
    }

    return render(request, "post_display.html", context)


def post_timeline(request):
    object_list = Post.objects.all().order_by("-post_date_time")
    
    search_req = request.GET.get("search")
    
    if search_req:
        object_list = object_list.filter(
            Q(post_title__contains=search_req)|
            Q(post_author__username__contains=search_req)
            )
            

    page = request.GET.get('page')    
    
    paginator = Paginator(object_list, 7) 
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    
    context = {
        "object_list": object_list,
        "title": "Timeline",
    }

    return render(request, "post_timeline.html", context)