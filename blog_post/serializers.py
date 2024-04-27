from rest_framework import serializers
from .models import BlogPost 

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost 
    fields = ['id', 'title', 'content', 'created_at', 'updated_at']

  def create(self, validated_data):
    blog_post = BlogPost(
      title=validated_data['title'],
      content=validated_data['content'],
    )
    blog_post.save()
    return blog_post