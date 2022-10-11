from rest_framework import viewsets,mixins
from .models import Product
from .serializers import ProductSerializers

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.object.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

class ProductGenericViewSets(viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin):
    queryset = Product.object.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

# product_list = ProductGenericViewSets.as_view({'get':'list'})
# product_retrive = ProductGenericViewSets.as_view({'get':'retrive'})