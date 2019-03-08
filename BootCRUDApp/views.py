from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm, ItemModel

# Create your views here.
# pulls all objects from the model
def index(request):
    item_list = ItemModel.objects.all()
    context = {'item_list':item_list}


    return render(request, 'BootCRUDApp/additem.html', context)

# renders the additem page and saves  validated form data
def additem(request):

    new_form = ItemForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')


    return render(request, 'BootCRUDApp/additem.html',{'form': new_form})

# allows the item in the database to be edited and saved
def edititem(request):
    item = get_object_or_404(ItemModel, pk =id)
    edit_form = ItemForm(request.POST or None, instance=item)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    return render(request, 'BootCRUDApp/index.html',{'form': edit_form})
