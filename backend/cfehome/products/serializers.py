from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import PublicSerializer,ProductInlineSerializer
from .validators import validate_title_no_hello,unique_product_title
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    owner = PublicSerializer(source='user',read_only=True)
    related_products = ProductInlineSerializer(source='user.product_set.all',read_only=True,many=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field="pk")
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello,unique_product_title])
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'my_user_data',
            'related_products',
        ]
    
    def get_my_user_data(self,obj):
        return {
            "username":obj.user.username
        }

    # def validate_title(self,value):
    #     qs = Product.objects.filter(title__exact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email,obj)
    #     return obj
    
    # def update(self,instance,validated_data):
    #     instance.title = validated_data.pop('title')
    #     return instance

    def get_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)

    def get_edit_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            None