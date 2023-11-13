from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from core.models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
def listing(request):
    data = {"blogs": Blog.objects.all()}
    return render(request, "listing.html", data)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {"blog": blog}
    return render(request, "view_blog.html", data)

def see_request(request):
    text = f"""
    Some attributes of the HttpRequest Object:

    scheme: {request.scheme}
    path:   {request.path}
    method: {request.method}
    GET:    {request.GET}
    user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")

def user_info(request):
    text = f"""
    Selected HttpRequest.user attributes:

    username:   {request.user.username}
    is_anonymous: {request.user.is_anonymous}
    is_staff:   {request.user.is_staff}
    is_superuser: {request.user.is_superuser}
    is_active:  {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")

@login_required
def private_place(request):
    return HttpResponse("Shhh, members only!",content_type="text/plain")