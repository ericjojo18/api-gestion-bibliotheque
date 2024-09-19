from crypt import methods

from rest_framework import viewsets
from rest_framework.decorators import action

from users.models import UserModel
from users.serializers.user_serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['patch'], url_path='set-password')
    def set_password(self, request, pk=None):
        user = self.get_object()
        data = request.data
        password = data['password']

        if not password:
            return Response('Password is required.', status=400)
        user.password = make_password(password)
        user.save()

        return Response('Password changed successfully.', status=200)

    def get_queryset(self):

        queryset = UserModel.objects.all()
        librarian = self.request.query_params.get('librarian')
        if librarian is not None:
            queryset = queryset.filter(librarian=librarian.lower() =='true')
        return queryset


