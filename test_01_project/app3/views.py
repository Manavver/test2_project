from django.shortcuts import render,redirect


# Create your views here.
from .models import Villian
# Create your views here.


def villian_list(request):
    v=Villian.objects.all()
    return render(request,'Villian_list.html',{'v':v})

def data_post3(request):
    if request.method=="POST":
        V=Villian()
        V.Name=request.POST['name']
        V.details=request.POST['details']

        V.save()
        return redirect('/app3/villian_list/')
    else:
        return render(request, 'post3.html')
def update_villian(request,id):
    v=Villian.objects.get(id=id)
    print(v)
    return render(request,'update_villian.html',{'v':v})

def do_update_villian(request ,id):
    Name = request.POST.get('name')
    details = request.POST.get('details')
    std=Villian.objects.get(pk=id)
    print(std)
    std.Name=Name
    std.details=details

    std.save()
    print(std.Name)
    print(std.details)

    return redirect('/app3/villian_list/')