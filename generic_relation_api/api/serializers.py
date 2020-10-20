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

"""class TaggedObjectRelatedField(serializers.ModelSerializer):

    class Meta:
        model = TaggedItem
        fields = '__all__'
       
    def to_representation(self, value):
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print(value.content_type)
        print(value.object_id)
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        if isinstance(value.content_type, Bookmark):
            serializer = BookmarkSerializer(value)
        elif isinstance(value.content_type, Note):
            serializer = NoteSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data
"""