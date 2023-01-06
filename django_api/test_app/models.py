from django.db import models
from django.utils import timezone

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True,  null=True, blank=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_Alive = models.BooleanField()
    amount = models.FloatField()
    extra_name = models.CharField(max_length=250, editable=False, default="null")
    created_at =models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return f" {self.name}"
    
    class Meta:
        ordering =("-created_at",)
        verbose_name_plural = "Test Model"
        
    def save(self, *args, **kwargs):
        self.extra_name = f"{self.name} - {self.phone_number}"
        super().save(*args, **kwargs)
        
        

class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name="test_content")
    mileage = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"
    
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "ModelX"
        


class ModelY(models.Model):
    test_content = models.OneToOneField(TestModel, on_delete=models.CASCADE, related_name="test_content_y")
    mileage = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"
    
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "ModelY"