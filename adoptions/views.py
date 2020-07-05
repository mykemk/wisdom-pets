from django.shortcuts import render,HttpResponse
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets':pets
    })
def pet_detail(request,pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Page not Found')
    return render(request,'pet_detail.html',{
                  'pet':pet
                  })
    