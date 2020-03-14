from django.shortcuts import render
from django.shortcuts import get_object_or_404

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

def profile(request, id_employe):
    """
        Employe profile endpoint
    """
    employe = get_object_or_404(Employe, pk=id_employe)
    context = {
        'employe': employe,
    }
    template_name = 'employe/profile.html'
    return render(request, template_name, context)
