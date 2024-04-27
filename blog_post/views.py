from .models import BlogPost
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializer

  def create(self, request, *args, **kwargs):
    print(request.data)
    serializer = self.serializer_class(data=request.data)

    if not serializer.is_valid():
      errors = serializer.errors
      return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    blog_post = serializer.save()
    data = BlogPostSerializer(blog_post).data

    return Response({'message': 'Success!', 'data': data})


