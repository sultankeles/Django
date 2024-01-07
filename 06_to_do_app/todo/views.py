from django.shortcuts import render, get_object_or_404

from .models import Todo
from .serializers import TodoSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from rest_framework.viewsets import ModelViewSet

# Create your views here.

@api_view(['GET', 'POST'])
def todo_list_create(request):

    if request.method == 'GET':
        todos = Todo.objects.filter(is_done = False)
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
def todo_view_update_delete(request, id):
    todo = get_object_or_404(Todo, id=id)


    if request.method == 'GET':
        # todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializer(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        todo.delete()
        return Response({"message":"deleted successfully"})
    


class Todos(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class Todo_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        message = {
            "massage":"Deleted Successfully"
        }

        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()





class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer