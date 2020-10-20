from rest_framework import serializers, validators

from module1.models import (
    Bookmark,
    Note,
    TaggedItem
)

class TaggedObjectRelatedField(serializers.RelatedField):
    
    def to_representation(self, value):

        if isinstance(value, Bookmark):
            serializer = BookmarkSerializer(value)
        elif isinstance(value, Note):
            serializer = NoteSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data

class BookmarkSerializer(serializers.ModelSerializer):
    #tags = TaggedObjectRelatedField(many=True, queryset=TaggedItem.objects.all())

    class Meta:
        model = Bookmark 
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    #tags = TaggedObjectRelatedField(many=True, queryset=TaggedItem.objects.all())
    
    class Meta:
        model = Note
        fields = '__all__'


class TaggedItemSerializer(serializers.ModelSerializer):
    tagged_object = TaggedObjectRelatedField(queryset=TaggedItem.objects.all())
    class Meta:
        model = TaggedItem
        fields = ('id', 'slug', 'tagged_object')
