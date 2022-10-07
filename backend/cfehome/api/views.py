from django.shortcuts import render
import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse,HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializers

# Create your views here.
@api_view(["POST"])
def api_home(request,*args,**kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        # data = serializer.data
        return Response(serializer.data)
    return Response({"This field is required"})
