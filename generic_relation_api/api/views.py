from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import (
    TaggedObjectRelatedField,
    TaggedItemSerializer
)
from module1.models import (
    TaggedItem
)


class TaggedItemContentTypeViewSet(viewsets.ModelViewSet):
    """
    
    ModelViewSet for Task objects. Include
    create(), update(), list(), destroy()
    operations
    """
    queryset = TaggedItem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    serializer_class = TaggedItemSerializer
