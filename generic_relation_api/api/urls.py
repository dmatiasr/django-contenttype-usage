from django.conf.urls import url
from . import views

# Una mejora aqui es configurar de tal manera de capturar todas las URL's que no entren por los
# endpoints declarados


content_type = views.TaggedItemContentTypeViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    url(r'^list/$', content_type, name='get-content-type'),
]