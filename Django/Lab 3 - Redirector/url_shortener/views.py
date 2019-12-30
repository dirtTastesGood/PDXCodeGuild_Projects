import string, random
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import CustomURL

def index(request):
    return render(request, 'url_shortener/index.html')

def saveurl(request):
    if(request.method == 'POST'):

        print('')
        print('')
        print('')

        print('CALLED!')
        print(f"long_url: {request.POST['long_url']}")

    print('')
    print('')
    print('')

    new_code = ''

    for i in range(6):
        new_code += random.choice(string.ascii_lowercase + string.digits)

    try:
        new_url = CustomURL.objects.get(code=new_code)
    except CustomURL.DoesNotExist:
        new_url = CustomURL.objects.create(url=request.POST['long_url'], code=new_code)
    return redirect('/')

def redirect_it(request):
    pass