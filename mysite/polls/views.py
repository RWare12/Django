from django.http import HttpResponse

def index(request):
    return HttpResponse("nasa index polls ako!")