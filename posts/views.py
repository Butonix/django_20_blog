from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from .models import Post
from .forms import PostForm


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'title': 'List',
        'object_list': queryset
    }

    return render(request, 'posts/index.html', context)

def post_detail(request, id=None):
    isinstance = get_object_or_404(Post, id=id)
    context = {
        'title': isinstance.title,
        'instance': isinstance
    }

    return render(request, 'posts/post_detail.html', context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        'form': form
    }
    return render(request, 'posts/post_form.html', context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")