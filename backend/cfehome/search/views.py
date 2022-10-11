from rest_framework import generics
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializers
from . import client

# Create your views here.

class SearchListView(generics.ListAPIView):
    def get(self,request,*args,**kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        queryset = request.GET.get('q')
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None
        print(user,queryset,public,tag)
        if not queryset:
            return Response('',status=400)
        results = client.perform_seacrh(queryset,tags=tag)
        return Response(results)
    def get_queryset(self):
        queryset = Product.object.all()
        return queryset

class SearchListOldView(generics.ListAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializers

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        q = self.request.GET.get('q')
        result = Product.object.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            result = qs.search(q,user=user)
        return Response(result)
