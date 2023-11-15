from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import Student
import json
from app.serializers import  StudentSerializer


@api_view(['GET', 'POST'])
def student_view(request):
    if request.method == 'GET':
        students =Student.objects.all().order_by('-created_at')
        serializer = StudentSerializer(students, many=True)
        
        return  Response(serializer.data , status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        print("data before jsnon",request.data)
        # data = request.data
        # print("--------------------------")
        # print(data)
        # create_student = Student.objects.create(name= data['name'], age = data['age'], gender = data['gender'])
        # create_student.save()
        if request.data == " ":
            pass
        else:
            serializer = StudentSerializer(data=request.data)
            print(type(request.data))
            print("--------------------------")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    

        
@api_view(['DELETE'])
def deletestudent(request, pk=None):

    if pk:
        stu_del = Student.objects.get(pk=pk)
        stu_del.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)




