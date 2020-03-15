from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from .models import Employe
from .forms import EmployeForm
from .seed import lunch_seed

# Create your views here.
def employe(request):
    """
        Employe List endpoint
    """
    # lunch_seed()
    employes = Employe.objects.all()
    context = {
        'employes': employes,
    }
    template_name = 'employe/index.html'
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

@require_http_methods(["POST"])
def create_employe(request):
    """
        Create employe data
    """
    form = EmployeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
        'status': True if form.is_valid() else False,
    }
    return JsonResponse(context, status=201)
