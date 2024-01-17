from django.shortcuts import render, redirect

# Create your views here.
from .models import Actoress
# Create your views here.


def actoress_list(request):
    b=Actoress.objects.all()
    return render(request,'actoress_list.html',{'b':b})


def data_post2(request):
    if request.method=="POST":
        A=Actoress()
        A.Name=request.POST['name']
        A.details=request.POST['details']

        A.save()
        return render(request, 'post2.html')
    else:
        return render(request, 'post2.html')

def update_data(request,id):
    f=Actoress.objects.get(id=id)
    print(f)
    return render(request,'update_data.html',{'f':f})

def do_update_data(request ,id):
    Name = request.POST.get('name')
    details = request.POST.get('details')
    std=Actoress.objects.get(pk=id)
    print(std)
    std.Name=Name
    std.details=details

    std.save()
    print(std.Name)
    print(std.details)

    return redirect('/app2/actoress_list/')
