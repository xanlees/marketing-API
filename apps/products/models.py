
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from sorl.thumbnail import ImageField
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import JSONField

# Create your models here.

class ShoeType(models.TextChoices):
    MEN = 'Men', 
    WOMEN = 'Women', 
    KIDS = 'Kids', 
    JORDAN = 'Jordan', 
    SPORT = 'Sport',


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Products(TranslatableModel):
    id = models.CharField(max_length=100, primary_key=True)
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=200,
                              db_index=True, unique=True),
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    type = models.CharField(
        max_length=10,
        choices=ShoeType.choices,
        default=ShoeType.MEN,
    )
    description = models.TextField(blank=True, null=True) 
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Products")
        verbose_name_plural = _("Products")
    
    def __str__(self):
        
        return self.name
    
    
class ProductColorImage(models.Model):
    """Stores color variations with images for products."""
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="color_images")
    color_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products/colors/")


    def __str__(self):
        return f"{self.product.name} - {self.color_name}"
    
    

class ProductSizeStock(models.Model):
    """Stores color variations with images for products."""
    color_image = models.ForeignKey(ProductColorImage, related_name='stock_sizes', on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.color_image.product.name} - {self.color_image.color_name} ({self.size})"
    
class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="additional_images")
    image = models.ImageField(upload_to="products/")
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image for {self.product.id}"
    
