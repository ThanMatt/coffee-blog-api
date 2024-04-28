from .models import BlogPost
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

  filterset_fields = ['title', 'created_at']
  search_fields = ['title', 'content']

  ordering_fields = ['title', 'created_at']
  default_ordering = ['created_at']

  def create(self, request, *args, **kwargs):
    print(request.data)
    serializer = self.serializer_class(data=request.data)

    if not serializer.is_valid():
      errors = serializer.errors
      return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    blog_post = serializer.save()
    data = BlogPostSerializer(blog_post).data

    return Response({'message': 'Success!', 'data': data})


