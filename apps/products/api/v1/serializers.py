# from lottery_time.models import Lottery_time

from django.conf import settings
from django.utils.module_loading import import_string
from parler_rest.serializers import TranslatableModelSerializer
from products.models import ProductImage, Products, ProductColorImage, ProductSizeStock
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from rest_framework import serializers

TranslatedSerializerMixin = import_string(settings.TRANSLATE_MIXIN)
DRFTranslatedFieldsField = import_string(settings.TRANSLATE_FIELD)



class StockSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSizeStock
        fields = ["id", "size", "stock"]

        
class ColorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColorImage
        fields = ["id", "color_name", "image"]
        
        
class ProductImageSerializer(serializers.ModelSerializer):
    
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = ProductImage
        fields = ["id", "image_url"]
        
    def get_image_url(self, obj):
        """✅ Return full image URL"""
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None
        
        
class ProductSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    # color = serializers.SerializerMethodField()
    # sizes = serializers.JSONField() 
    translations = DRFTranslatedFieldsField(shared_model=Products)
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={"crop": "center"},
        source='image',
        read_only=True

    )
    image = HyperlinkedSorlImageField('1024')
    
    additional_images = serializers.SerializerMethodField()
    stock_sizes = StockSizeSerializer(many=True, source="size_stocks", required=False)
    color_images = ColorImageSerializer(many=True, required=False)
  
    class Meta:
        model = Products
        fields = ['id','translations', 'thumbnail', 'description', 'price', 'image', 'additional_images','stock_sizes', 'color_images' ]
        
    # def get_size_stock(self, obj):
    #     """✅ Validate and return size stock properly"""
    #     if isinstance(obj.size_stock, dict):
    #         return obj.size_stock  # If it's already a valid dictionary
    #     return {}
    
    def get_additional_images(self, obj):
        """✅ Return a list of additional image URLs"""
        if obj.additional_images.exists():  # Prevent NoneType error
            request = self.context.get("request")
            return [
                request.build_absolute_uri(img.image.url) for img in obj.additional_images.all()
            ]
        return []
    
    # def get_color(self, obj):
    #     """Convert color image paths to absolute URLs"""
    #     request = self.context.get("request")  # ✅ Get request context
    #     return {
    #         color: request.build_absolute_uri(image_url)  # ✅ Convert to full URL
    #         for color, image_url in obj.color.items()
    #     }
