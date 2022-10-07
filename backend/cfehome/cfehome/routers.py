from django.db import router
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSets,ProductGenericViewSets

router = DefaultRouter()
router.register('products-adc',ProductGenericViewSets,basename='products')
print(router.urls)
urlpatterns = router.urls