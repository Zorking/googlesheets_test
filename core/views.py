from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    context = {}
    if request.method == 'POST':
        resp = requests.post('YOUR_GOOGLE_APP_SCRIPT_URL', json=[request.POST.get('bla'), request.POST.get('bla2')])
        context = {'value': resp.text}
    return render(request, 'home.html', context)
