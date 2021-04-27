from django.shortcuts import render
from .models import tablemodel
# Create your views here.

def form(request):
    if request.method=="POST":
        if request.POST.get("inp1") and request.POST.get("inp2") and request.POST.get("inp3") and request.POST.get("inp4"):
            rcd=tablemodel()
            rcd.name=request.POST.get("inp1")
            rcd.age=request.POST.get("inp2")
            rcd.address=request.POST.get("inp3")
            rcd.number=request.POST.get("inp4")
            rcd.save()
    return render(request,"app/form.html",{
    'access_records':tablemodel.objects.all()
    })
