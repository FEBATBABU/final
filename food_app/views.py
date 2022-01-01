from django.shortcuts import render, redirect
from . models import food
from . forms import ModeForms
# Create your views here.
def home(request):
    products=food.objects.all()
    return render(request,'home.html',{'products':products})


def detail(request,id):
    prod=food.objects.get(id=id)
    return render(request,'detail.html',{'pr':prod})


def update(request,item_id):
    obj=food.objects.get(id=item_id)
    form=ModeForms(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})

def add_product(request):
        if request.method=='POST':
            name=request.POST.get('name')
            desc=request.POST.get('desc')
            price=request.POST.get('price')
            img=request.FILES['img']
            s=food(name=name,desc=desc,price=price,img=img)
            s.save()
            print("product added")
            return redirect('/')
        return render(request,"add_product.html")


def delete(request,food_id):
    if request.method=='POST':
        obj=food.objects.get(id=food_id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')