from django.contrib import admin

# Register your models here.
from .models import (
    TaggedItem,
    Bookmark,
    Note
)

admin.site.register(TaggedItem)
admin.site.register(Bookmark)
admin.site.register(Note)