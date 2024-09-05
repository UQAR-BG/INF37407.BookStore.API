from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import check_password, make_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import LoginSerializer, UserSerializer, UserDtoSerializer
from .models import User

# Create your views here.
@swagger_auto_schema(
    method="post", tags=["Authentication"], request_body=LoginSerializer
)
@api_view(['POST'])
def login(request):
    email = request.data["email"]
    password = request.data["password"]
    user = User.objects.filter(email = email)
    
    if(user.exists()):
        realUser = user.first()
        valid_credentials = check_password(password, realUser.password)
        
        if(valid_credentials):
            token = Token.objects.filter(user = realUser)
            if not (token.exists()):
                token = Token.objects.create(user = realUser)

            serializer = UserDtoSerializer(realUser)
            return Response(
                    {
                        "user": serializer.data,
                        "token": f"Token {token.key}"
                        
                    },
                    status=status.HTTP_200_OK
                )

    return Response(
        {
            "message": "Invalid credentials.",
        },
        status=status.HTTP_404_NOT_FOUND
    )

@swagger_auto_schema(
    method="post", tags=["Authentication"], request_body=UserSerializer
)
@api_view(['POST'])
def signUp(request):
    lastName = request.data["last_name"]
    firstName = request.data["first_name"]
    email =request.data["email"]
    password =request.data["password"]
    role =request.data["role"]
    
    user = User(first_name=firstName, last_name=lastName,
                                email=email, password=make_password(password), role = role)
    user.save()

    return Response(
                {
                    "message": "The user {} {} was successfully created.".format(firstName, lastName)
                },
                status=status.HTTP_201_CREATED
            )

@swagger_auto_schema(
    method="get", tags=["Authentication"]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
    invalidated_token = Token.objects.filter(key=token).first()

    if (invalidated_token):
        invalidated_token.delete()
        
    return Response({"message": "Déconnexion effectuée avec succès !"}, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method="get", tags=["Authentication"]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
    user = Token.objects.filter(key = token).first().user
    user_serializer = UserDtoSerializer(user, many=False)
    return Response(
        {
        "data": user_serializer.data,
        }, 
        status= status.HTTP_200_OK
    )