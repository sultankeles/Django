from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer

# FBV
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# CBV
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.


# FBV

@api_view()   # ['GET']
def home(request):
    return Response({       # JSON DATA TYPE -> Response
        "home":"Home Page"
    })



@api_view(['GET'])
def list_students(request):
    students = Student.objects.all()
    print(students)
    serializer = StudentSerializer(students, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def create_student(request):
    serializer_request = StudentSerializer(data=request.data)
    if serializer_request.is_valid():
        serializer_request.save()
        return Response(serializer_request.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer_request.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def display_special_student_details(request, pk):
    # try:
    #     special_student_queryset_data = Student.objects.get(id=pk)
    #     serializer = StudentSerializer(special_student_queryset_data)
    # except:
    #     massage = {
    #         "massage":"No such student number was found. Please try another ID number."
    #     }
    #     return Response(massage)

    special_student_queryset_data = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(special_student_queryset_data)

    return Response(serializer.data)


@api_view(['PUT'])
def refresh_object(request, pk):
    old_student_data = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=old_student_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            'message':'Student information has been updated.'
        }
        return Response(message)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(requet, pk):
    delete_student_data = get_object_or_404(Student, id=pk)
    delete_student_data.delete()
    message = {
        "message":"The student was successfully deleted."
    }
    return Response(message)



# CBV


class StudentListCreate(APIView):
    def get(self, request):
        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        serializer_request = StudentSerializer(data=request.data)
        if serializer_request.is_valid():
            serializer_request.save()
            return Response(serializer_request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_request.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StudentDetail(APIView):
    def display_special_student_details(request, pk):    
        special_student_queryset_data = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(special_student_queryset_data)
        return Response(serializer.data)

    def refresh_object(request, pk):
        old_student_data = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=old_student_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                'message':'Student information has been updated.'
            }
            return Response(message)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_student(requet, pk):
        delete_student_data = get_object_or_404(Student, id=pk)
        delete_student_data.delete()
        message = {
            "message":"The student was successfully deleted."
        }
        return Response(message)
    


class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    



class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


# Concreate Views

class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




# ViewSet

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer