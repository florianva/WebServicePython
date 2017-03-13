from django.conf.urls import url, include
from webservice.models import Book, Member
from webservice.serializers import BookSerializer
from webservice import views
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Serializers define the API representation.
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'idBook', 'name')


# ViewSets define the view behavior.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^books/(?P<pk>[0-9]+)/$', views.book_detail),
]