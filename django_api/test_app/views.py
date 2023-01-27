from django.http import response, JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from .models import TestModel
from .serializers import SimpleSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class Simple(APIView):
    def post(self,request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return JsonResponse({"data": serializer.data})
    
    def get(self, request):
        content = TestModel.objects.all()
        return JsonResponse({"data":  SimpleSerializer(content, many=True).data})
    
    def put(self, request, *args, **kwargs):
        model_id = kwargs.get('id', None)
        
        if not model_id:
            return JsonResponse({"error": "Put method is not allowed"})
        
        instance = TestModel.objects.get(id=model_id)
        
        
        serializer = SimpleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data": serializer.data})
        


class SimpleGenerics(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    
class SimpleGenericsUpdate(generics.UpdateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    lookup_field = "id"

class SimpleViewSet(ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    