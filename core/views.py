from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    context = {}
    if request.method == 'POST':
        resp = requests.post(
            'https://script.google.com/macros/s/AKfycbzs0gUBNZZjkEq61cr5pKFZdPN8iJ4dmInVkPh4UjEVG4VfZvbj/exec',
            json=[request.POST.get('bla'), request.POST.get('bla2')])
        context = {'value': resp.text}
    return render(request, 'home.html', context)
