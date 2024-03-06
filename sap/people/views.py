from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from people.form import PersonForm
from people.models import People


# Create your views here.
def personDetail(request, id):
    #person= People.objects.get(pk = id)
    person = get_object_or_404(People, pk = id)
    return render(request, 'people/detail.html', {'person': person})

#PersonForm = modelform_factory(People, exclude = [])

def newPerson(request):
    if request.method == "POST":
        personForm = PersonForm(request.POST)
        if personForm.is_valid():
            personForm.save()
            return redirect('start')

    else:
        personForm = PersonForm()

    return render(request, "people/new.html", {'personForm': personForm})

def editPerson(request, id):
    person = get_object_or_404(People, pk=id)
    if request.method == "POST":
        personForm = PersonForm(request.POST, instance = person)
        if personForm.is_valid():
            personForm.save()
            return redirect('start')

    else:
        personForm = PersonForm(instance = person)

    return render(request, "people/edit.html", {'personForm': personForm})

def deletePerson(request, id):
    person = get_object_or_404(People, pk=id)
    if person:
        person.delete()
    return redirect('start')

