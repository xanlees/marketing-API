
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from sorl.thumbnail import ImageField
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import JSONField

# Create your models here.



class Products(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("name"), max_length=200,
                              db_index=True, unique=True),
    )
    description = models.TextField(blank=True, null=True) 
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Products")
        verbose_name_plural = _("Products")
    
    def __str__(self):
        
        return self.name
    
    
    # def update_color_field(self):
    #     """Automatically updates the color JSONField with uploaded images."""
    #     colors = {color_obj.color_name: color_obj.image.url for color_obj in self.color_images.all()}
    #     self.color = colors
    #     self.save(update_fields=['color'])
    
class ProductSizeStock(models.Model):
    """Stores color variations with images for products."""
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="size_stocks")
    size = models.CharField(max_length=50)
    stock = models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name = _("Products_size_stocks")
        verbose_name_plural = _("Products_size_stocks")

    def __str__(self):
        return f"{self.size} - {self.stock} units for {self.product.name}"
    

    # def save(self, *args, **kwargs):
    #     """Update product's color JSONField on save"""
    #     super().save(*args, **kwargs)
    #     self.product.update_sizes_field()


class ProductColorImage(models.Model):
    """Stores color variations with images for products."""
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="color_images")
    color_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products/colors/")

    class Meta:
        verbose_name = _("Products_color_image")
        verbose_name_plural = _("Products_color_images")

    def __str__(self):
        return f"{self.color_name} - {self.image} units for {self.product.name}"
    

    # def save(self, *args, **kwargs):
    #     """Update product's color JSONField on save"""
    #     super().save(*args, **kwargs)
    #     self.product.update_color_field()
        
        
class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="additional_images")
    image = models.ImageField(upload_to="products/")
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = _("Products_image")
        verbose_name_plural = _("Products_images")

    def __str__(self):
        return f"Image for {self.product.id}"
    
