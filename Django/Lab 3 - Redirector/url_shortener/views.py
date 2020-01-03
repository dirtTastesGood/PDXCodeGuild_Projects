import string, random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import CustomURL

def index(request):
    urls = CustomURL.objects.all()[::-1]

    context = {
        'urls':urls,
    }

    return render(request, 'url_shortener/index.html', context)

def saveurl(request):
    if(request.method == 'POST'):

        new_code = ''

        for i in range(6):
            new_code += random.choice(string.ascii_lowercase + string.digits)

        try:
            new_url = CustomURL.objects.get(code=new_code)
        except CustomURL.DoesNotExist:
            new_url = CustomURL.objects.create(url=request.POST['long_url'], code=new_code)
        return redirect('/')

def redirect_it(request, code):
    try:
        row = CustomURL.objects.get(code=code)
        url = row.url
    except CustomURL.DoesNotExist:
        messages.error(request, f'{code} is not a valid code. Please try again.')
        url = '/'

    return redirect(url)