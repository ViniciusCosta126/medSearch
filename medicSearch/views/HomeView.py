from django.http import HttpResponse


def home_view(request):
    return HttpResponse('<h1>Ola mundo!</h1>',status = 200)
