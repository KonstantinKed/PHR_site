from django.shortcuts import render
from django.http import HttpResponse

# from inventory.models import Apartments, Condition

def index(request):  # our controller!
    return HttpResponse ("Soon you will have an option to use Inventory application to control items availability, and create lists of items for each apartment")
# Create your views here.

# def apartment_list(request, pk):
#     apt_obj = Apartments.objects.get(pk=pk)
#     cond_obj = Condition.object.get(pk=pk)
#
#     context = {}