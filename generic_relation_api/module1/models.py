from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey

from django_extensions.db.fields import SlugField

from generic_relation_api.slug_generator import get_unique_slug

# Create your models here.
class TaggedItem(models.Model):
    """
    Tags arbitrary model instances using a generic relation.

    See: https://docs.djangoproject.com/en/stable/ref/contrib/contenttypes/
    """
    slug = SlugField(db_index=True,
                     unique=True,
                     blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    tagged_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '%s - %s: %s' % (self.__class__.__name__, self.id, self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self)
        super().save(*args, **kwargs)

class Bookmark(models.Model):
    """
    A bookmark consists of a URL, and 0 or more descriptive tags.
    """
    slug = SlugField(db_index=True,
                     unique=True,
                     blank=True)
    url = models.URLField()
    tags = GenericRelation(TaggedItem)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s - %s: %s' % (self.__class__.__name__, self.id, self.slug)

class Note(models.Model):
    """
    A note consists of some text, and 0 or more descriptive tags.
    """
    slug = SlugField(db_index=True,
                     unique=True,
                     blank=True)
    text = models.CharField(max_length=1000)
    tags = GenericRelation(TaggedItem)


    def __str__(self):
        return '%s - %s: %s' % (self.__class__.__name__, self.id, self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self)
        super().save(*args, **kwargs)