from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response


class TodoViewset(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def list(self, request):
        req_data = request.GET
        status = req_data.get("status")
        if status:
            queryset = Todo.objects.filter(status=status)
        else:
            queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)
