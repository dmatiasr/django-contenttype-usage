from collections import OrderedDict

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

class TaggedObjectTypeRelatedField(serializers.RelatedField):
    
    def to_representation(self, value):

        if isinstance(value, Bookmark):
            return 'bookmark'
        elif isinstance(value, Note):
            return 'note'
        raise Exception('Unexpected type of tagged object')

class BookmarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bookmark 
        fields = ('slug','url')
    
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is None:
                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)
        ret['content_name'] = instance.__class__.__name__.lower()

        return ret
 
class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Note
        fields = ('slug', 'text')

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is None:
                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)
        ret['content_name'] = instance.__class__.__name__.lower()

        return ret


class TaggedItemSerializer(serializers.ModelSerializer):
    tagged_object = TaggedObjectRelatedField(queryset=TaggedItem.objects.all())
    class Meta:
        model = TaggedItem
        fields = ('slug', 'tagged_object')
