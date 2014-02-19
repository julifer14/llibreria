from django.shortcuts import render
from llibres.models import  Titol
# Create your views here.

def home(request):
    titols = Titol.objects.all()
    context = {'titols': titols}
    return render(request, 'home.html', context)


def xat(request):
    return render(request, 'xat.html')

