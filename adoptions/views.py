from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse('<p>Welcome home</p>')

def pet_detail(request,pet_id):
    return HttpResponse(f'<p>Details for pet id {pet_id}</p>')
    