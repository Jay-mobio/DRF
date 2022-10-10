from rest_framework import generics,mixins,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin

from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Product
from .serializers import ProductSerializers

class ProductListCreateApiView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user = self.request.user, content=content)
    
    # def get_queryset(self,*args,**kwargs):
    #     qs = super().get_queryset(*args,**kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateApiView.as_view()

class PoductDetailApiView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    # lookup_field = 'pk'

    # Product.objects.get(pk)
product_detail_view = PoductDetailApiView.as_view()

class PoductUpdateApiView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ##

    # Product.objects.get(pk)
product_update_view = PoductUpdateApiView.as_view()

class PoductDestroyAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    

    def perform_delete(self, instance):
        super().destroy(instance)

product_delete_view = PoductDestroyAPIView.as_view()

@api_view(['Get','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            #detail view
            queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializers(obj, many=False)
            return Response()

        queryset = Product.objects.all()
        data = ProductSerializers(queryset, many=True).data
        return (data)

    if method == "POST":
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            # data = serializer.data
            return Response(serializer.data)
        return Response({"This field is required"})
        
class ProductMixinView(StaffEditorPermissionMixin,mixins.ListModelMixin,
mixins.CreateModelMixin,
mixins.RetrieveModelMixin,
generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    

    def get(self,request,*args,**kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

product_list_view = ProductMixinView.as_view()