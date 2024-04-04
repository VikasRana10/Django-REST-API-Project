# myapp/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Paragraph
from .serializers import UserSerializer, ParagraphSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ParagraphCreateAPIView(generics.CreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]

class ParagraphSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        word = request.query_params.get('word', None)
        if not word:
            return Response({'error': 'Word parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        paragraphs = Paragraph.objects.filter(text__icontains=word)[:10]
        serializer = ParagraphSerializer(paragraphs, many=True)
        return Response(serializer.data)
