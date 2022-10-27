from django.shortcuts import render
from .models import Animal


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


def create_page(request):
    if request.method == 'GET':
        return render(request, "animal_pages/create_page.html/")

    if request.method == 'POST':
        animals = Animal(
            animal_name=request.POST['animal_name'],
            descriptions=request.POST['descriptions'],
        )
        animals.save()

        animals_list = Animal.objects.all()
        context = {
            "animals_list": animals_list
        }
        return render(request, "animal_pages/bastim.html", context)
