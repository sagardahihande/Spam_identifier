from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import User, Contact, SpamMarking
from .serializers import UserSerializer, ContactSerializer, SpamSerializer

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            phone_number=data['phone_number'],
            email=data.get('email', ''),
        )
        Token.objects.create(user=user)
        return Response({"message": "User registered successfully!"})

class SpamMarkingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        SpamMarking.objects.create(
            phone_number=data['phone_number'], marked_by=request.user
        )
        return Response({"message": "Number marked as spam."})

# More views like login, search, etc., can be added similarly.
