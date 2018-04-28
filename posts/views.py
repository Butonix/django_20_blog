from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus


# Create your views here.
from .models import Post
from .forms import PostForm


def post_list(request):
    queryset_list = Post.objects.all().order_by('-created')

    page = request.GET.get('page')

    paginator = Paginator(queryset_list, 5)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'title': 'List',
        'object_list': queryset,
    }

    return render(request, 'posts/post_list.html', context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        'title': instance.title,
        'instance': instance,
        'share_string': share_string,
    }

    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    elif form.errors:
        messages.error(request, "Not Successfully Created")
    else: pass

    context = {
        'form': form
    }
    return render(request, 'posts/post_form.html', context)


def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Updated')
        return HttpResponseRedirect(instance.get_absolute_url())


    context = {
        'title': instance.title,
        'instance': instance,
        'form': form
    }
    return render(request, 'posts/post_form.html', context)


def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Deleted")

    return redirect("posts:post_list")