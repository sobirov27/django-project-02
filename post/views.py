from django.shortcuts import render, redirect
from .models import Post, PostComment, PostView

# Create your views here.


def home_page(request):
    context = {
        "posts": Post.objects.all().order_by("id")
    }
    return render(request, "index.html", context=context)

def post_create(request):
    if request.user.is_authenticated:
        return render(request, "post-create.html")
    else:
        return redirect("login")
    

def login(request):
    return render(request, "login.html")


def post_create_view(request):
    if request.method == "POST":
        post_matn = request.POST.get("post_description")
        if post_matn:
            Post.objects.create(
                user=request.user,
                description=post_matn,
        )
    return redirect("home")

