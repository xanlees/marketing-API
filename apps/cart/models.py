from django.db import models
from sorl.thumbnail import ImageField
from django.utils.translation import gettext as _


class Cart(models.Model):
    product_id = models.CharField(max_length=255)  # Store product ID
    name = models.CharField(max_length=255)  # Product name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
    quantity = models.PositiveIntegerField()  # Quantity of items
    color = models.CharField(max_length=50, null=True, blank=True)  # Optional color
    size = models.CharField(max_length=10, null=True, blank=True)  # Optional size
    image = ImageField(verbose_name='Image', upload_to='uploads/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp
    
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return f"{self.name} ({self.quantity})"