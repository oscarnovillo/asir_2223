from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Coche
from api.serializers import CocheSerializer



class CocheViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Coche.objects.all()
    serializer_class = CocheSerializer
    permission_classes  = [permissions.IsAuthenticated]
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CocheSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CocheSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

@api_view(['GET', 'POST'])
def coches_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        coches = Coche.objects.all()
        serializer = CocheSerializer(coches, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CocheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)