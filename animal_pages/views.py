from django.shortcuts import render
from .models import Animal
from .forms import AnimalCreateForm


def animal_list(request):
    animals = Animal.objects.all()
    context = {
        "animals": animals
    }
    return render(request, "animal_pages/animal_list.html", context)


def animal_profile(request, id):
    obj = Animal.objects.get(id=id)
    context = {
        "obj": obj
    }
    return render(request, "animal_pages/animal_profile.html", context)


# def create_page(request):
#    if request.method == 'GET':
#        return render(request, "animal_pages/create_page.html/")

#    if request.method == 'POST':
#        animals = request.POST['animal_name']
#        context = {
#            "animals": animals
#        }
#        return render(request, "animal_pages/bastim.html", context)


# def create_page(request):
#    if request.method == 'GET':
#        return render(request, "animal_pages/create_page.html/")

#    if request.method == 'POST':
#   animals = Animal(
#       animal_name=request.POST['animal_name'],
#       descriptions=request.POST['descriptions'],
#   )
#   animals.save()
#
#   animals_list = Animal.objects.all()
#   context = {
#       "animals_list": animals_list
#   }
#   return render(request, "animal_pages/bastim.html", context)


def create_page(request):
    if request.method == 'GET':
        form = AnimalCreateForm()
        context = {
            'form': form
        }
        return render(request, "animal_pages/create_page2.html/", context)

    if request.method == 'POST':
        form = AnimalCreateForm(request.POST)
        if form.is_valid():
            animal_create = Animal()
            animal_create.animal_name = form.cleaned_data['animal_name']
            animal_create.descriptions = form.cleaned_data['descriptions']
            animal_create.save()

        animals_list = Animal.objects.all()
        context = {
            "animals_list": animals_list
        }
        return render(request, "animal_pages/bastim.html", context)
