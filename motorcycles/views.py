from django.shortcuts import render

from motorcycles.models import Bike
from motorcycles.models import Brand
# Create your views here.
def index(request):
    return render(request, "index.html")

def catalogue(request):
    items = Bike.objects.all().order_by('id')
    page_data  = {'items': items}
    return render(request, "catalogue.html", page_data )


#.com/item/<id>
#           ^^---> item_id
def items(request, item_id):
    context = {
    'items':Bike.objects.get(id=item_id)
    }
    return render(request, "items.html", context )


def datamodel(request):
    return render(request, "datamodel.html")
