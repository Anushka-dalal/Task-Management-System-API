from django.shortcuts import render
from rest_framework.response import Response #type:ignore
from rest_framework.decorators import APIView #type:ignore
from rest_framework.decorators import api_view  #type:ignore
from .serializers import TaskSerializer
from .models import Tasks
from abc import ABC,abstractmethod
# Create your views here.

class addTask(APIView):
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task added.'},status=201)
        return Response(serializer.errors,status=400)

    def put(self,request):
        id = request.GET.get('id')
        if id:
            try:
                tasks = Tasks.objects.get(id = id)
                serializer = TaskSerializer(tasks,data = request.data)
                if serializer.is_valid():
                    serializer.save() 
                    return Response({"message" : "Task updated successfully!"},status=204)
            except Exception as e:
                return Response({"error" : str(e)},status=404)
        else:
            return Response({"error" : "task is required"},status=400)   
        
    def patch(self,request):
        id = request.GET.get('id')
        if id:
            try:
                tasks = Tasks.objects.get(id = id)
                serializer = TaskSerializer(tasks,data = request.data, partial = True)
                if serializer.is_valid():
                    serializer.save() 
                    return Response({"message" : "Task updated successfully!"},status=204)
            except Exception as e:
                return Response({"error" : str(e)},status=404)
        else:
            return Response({"error" : "task is required"},status=400)
    
class retrieveTasks(APIView):
    def get(self,request):
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data,status=200)
    
class deleteTask(APIView):
    def delete(self,request):
        id = request.GET.get('id')
        if id :
            try:
                task = Tasks.objects.get(id = id)
                task.delete()
                return Response({"message": "Task deleted successfully!"},status=204) 
            except Exception as e:
                return Response({"error" : str(e)},status=404) 
        else:
            return Response({"error" : "task id is required"}, status=400) 
        