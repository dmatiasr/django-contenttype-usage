import uuid


def generate_another_slug():
    new_slug = "{slug}".format(
        slug=uuid.uuid1(),
    )
    return new_slug


def get_unique_slug(instance):
    '''
    In this method a unique slug is created
    '''
    slug = generate_another_slug()
    unique_slug = slug
    while instance.__class__.objects.filter(slug=unique_slug).exists():
        unique_slug = generate_another_slug()
    return unique_slug
