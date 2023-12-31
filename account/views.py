from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls.conf import path
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from account import serializers
from account.permissions import IsAdmin
from account.send_mail import send_confirmation_email
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

User = get_user_model()


class UserViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

    @action(['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if user:
            send_confirmation_email(user.email, user.activation_code)
            return Response(serializer.data, status=201)
        # return render(request, 'authentication/index.html')

    @action(['GET'], detail=False, url_path='activate/(?P<uuid>[0-9A-Fa-f-]+)')
    def activate(self, request, uuid):
        try:
            user = User.objects.get(activation_code=uuid)
        except User.DoesNotExists:
            # return render(request, 'authentication/index.html')
            return Response({'msg': 'Invalid link or link expired!'}, status=400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        # return render(request, 'authentication/index.html')
        return Response({'msg': 'Successfully activated!'}, status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny, )


class RefreshView(TokenRefreshView):
    permission_classes = (AllowAny, )


class UserViewSetSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserSerializer
        return serializers.UserDetailSerializer

    def get_permissions(self):
        # может удалять только админ
        if self.action == 'destroy':
            return [IsAdmin(), ]

        if self.action == 'create':
            return [IsAdmin(), ]
        return [IsAuthenticated(), ]
