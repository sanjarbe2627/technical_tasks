from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import status
from django.utils.translation import gettext_lazy as _

from apps.api.v1.base.pagination import CustomPagination
from apps.api.v1.student import serializers
from apps.users.models import Student


# Task 3
class StudentView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        "user__fullname", "user__email", "user__date_joined__date", "user__username",
        "status", "university", "contract"
    ]
    pagination_class = CustomPagination

    def get_object(self, *args, **kwargs):
        try:
            object = self.queryset.get(pk=int(kwargs.get("pk")))
        except Exception as e:
            print("error", e)
            raise NotFound(_("Student not found"))
        return object

    def perform_create(self, serializer, request):
        user_serializer = serializers.StudentUserSerializer(
            data=self.request.data.get('user', {}), many=False,
            context={'request': request}
        )
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        serializer.save(user=user)

    def perform_update(self, serializer, instance_user, request):
        user_serializer = serializers.StudentUserSerializer(
            data=self.request.data.get('user', {}), many=False, instance=instance_user,
            context={'request': request}
        )
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        serializer.save(user=user)

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            instance = self.get_object(*args, **kwargs)
            serializer = self.get_serializer(instance)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(*args, **kwargs)
        serializer = self.get_serializer(instance, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer, instance_user=instance.user, request=request)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        student = self.get_object(*args, **kwargs)
        if not student:
            return Response({"error": _(f"Student  not found")},
                            status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)