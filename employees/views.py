from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from drf_spectacular.utils import extend_schema


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = UserSerializer
    queryset = User.objects.get_queryset().order_by("id")


@extend_schema(
    methods=["PUT"],
    exclude=True,
)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAccountOwner]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "user_id"
