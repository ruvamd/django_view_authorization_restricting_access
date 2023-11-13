from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def private_place(request):
    return HttpResponse("Shhh, members only!", 
    content_type="text/plain")
    