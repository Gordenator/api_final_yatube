from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее только авторам объекта редактировать его.
    Просмотр доступен всем пользователям.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
