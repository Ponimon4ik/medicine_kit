from djoser.serializers import SetPasswordSerializer
from rest_framework import pagination, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .mixins import ListCreateRetrieveViewSet
from .models import User
from .serializers import CustomUserCreateSerializer, CustomUserSerializer


class UserViewSet(ListCreateRetrieveViewSet):

    queryset = User.objects.all().order_by('id')
    pagination_class = pagination.LimitOffsetPagination

    def get_permissions(self):
        if self.action in ['me', 'set_password', 'retrieve']:
            self.permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['create', 'list']:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'set_password':
            return SetPasswordSerializer
        elif self.request.method == 'POST':
            return CustomUserCreateSerializer
        return CustomUserSerializer

    @action(detail=False,)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(['post'], detail=False,)
    def set_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.request.user.set_password(serializer.data["new_password"])
        self.request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

