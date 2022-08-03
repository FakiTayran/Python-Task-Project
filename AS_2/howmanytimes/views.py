from django.shortcuts import render
from .models import Operation,Bin
# Create your views here.
from django.shortcuts import render,redirect
from datetime import datetime
from .forms import BinForm,BinUpdateForm

def getOperations(request):
    operations = Operation.objects.all()
    operations = seedForOperations(operations)

    return render(request, 'home.html', {'operations': operations})

def bin_create(request):
    form = BinForm()
    context = {
        'form':form.as_p
    }
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    collection_frequency = 1
    operation = request.POST.get('operation')
    last_collection = datetime.now()

    if request.method == "POST":
        operation = Operation.objects.get(id=operation)
        Bin.objects.create(latitude=latitude,longitude=longitude,collection_frequency=collection_frequency,operation = operation,last_collection=last_collection)
        bins = Bin.objects.all()
        return render(request, 'get.html', {'bins': bins})
    else:
        form = BinForm()

    return render(request,'form.html',context)

def getBins(request):
    bins = Bin.objects.all()

    return  render(request,'get.html',{'bins':bins})

def getBin(request,id):
    bin = Bin.objects.get(id=id)
    if bin.operation.name == "Get":
        bin.collection_frequency = bin.collection_frequency + 1
        bin.last_collection = datetime.now()
        bin.save()

    return render(request,'detail.html',{'bin':bin})

def bin_update(request,id):
    bin = Bin.objects.get(id=id)
    form = BinUpdateForm(instance=bin)



    if request.method == "POST":
        bin.latitude = request.POST.get('latitude')
        bin.longitude = request.POST.get('longitude')
        if bin.operation.name == "Update":
            bin.collection_frequency = bin.collection_frequency + 1
            bin.last_collection = datetime.now()
        bin.save()
        bins = Bin.objects.all()
        return render(request,'get.html',{'bins':bins})

    context = {
        'form': form.as_p
    }

    return render(request,'form.html',context)

def bin_delete(request,id):
    Bin.objects.filter(id=id).delete()

    bins = Bin.objects.all()

    return render(request, 'get.html', {'bins': bins})


def seedForOperations(operations):

    if len(operations) == 0:
        name = 'Add'
        Operation.objects.create(name=name)
        name = 'Get'
        Operation.objects.create(name=name)
        name = 'Update'
        Operation.objects.create(name=name)
        name = 'Delete'
        Operation.objects.create(name=name)
        operations = Operation.objects.all()

    return operations






