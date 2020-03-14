from django.shortcuts import render

from .models import Employe

# Create your views here.
def employe(request):
    """
        Employe List endpoint
    """
    employes = Employe.objects.all()
    context = {
        'employes': employes,
    }
    template_name = 'employe/home.html'
    return render(request, template_name, context)
