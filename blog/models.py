from django.db import models



class Blog(models.Model):
    blog_image = models.ImageField(upload_to="blog_image",default='blog_image/default.png',blank=True,null=True)
    blog_title = models.CharField(max_length=35)
    blog_creation_date = models.DateTimeField()
    blog_text = models.TextField(max_length=70)


    def __str__(self):
        return self.blog_title