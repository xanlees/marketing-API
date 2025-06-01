from django.db import models
from enum import Enum

class DocumentType(Enum):
    Passport = "Passport"
    Visa = "Visa"
    Marriage = "Marriage"
    Drivers_licence = "Drivers Licence"
    International_Drivers_licence = "International Drivers Licence"
    Other = "Other"

    @classmethod
    def choices(cls):
        """Return choices as a list of tuples."""
        return [(choice.value, choice.name.replace("_", " ").title()) for choice in cls]

class Apply_Booking(models.Model):
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    ]
    username = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(auto_now_add=False)
    document_type = models.CharField(
        max_length=255, choices=DocumentType.choices(), default=DocumentType.Passport.value
    )
    address = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Apply_Booking"
        verbose_name_plural = "Apply_Bookings"

    def __str__(self):
        return f"Apply_Booking: {self.username}"
