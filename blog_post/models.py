from django.db import models

class BlogPost(models.Model):
  title = models.TextField()
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = "blog_post"

