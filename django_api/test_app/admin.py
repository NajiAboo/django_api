from django.contrib import admin
from .models import TestModel, ModelX, ModelY
# Register your models here.

admin.site.register(TestModel)
admin.site.register(ModelX)
admin.site.register(ModelY)