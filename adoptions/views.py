from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
#from django.template import loader

from .models import Pet
# Create your views here.


def home(request):
	
	pets = Pet.objects
	context = {
		'pets':pets,
	}
	#return HttpResponse('adoptions/home.html')
	return render(request,'adoptions/home.html',context)



def detail(request,pet_id):
	pet = get_object_or_404(Pet,pk=pet_id)
	pet_detail = {'pet':pet}
	return render(request,'adoptions/pet_detail.html',pet_detail)
