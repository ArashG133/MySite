from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to = 'blog/', default= 'blog/default.jpg')
    count = models.IntegerField(default= 0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): #dunder string
        return " {} - {}".format(self.title, self.id)

    class Meta:
        ordering = ["create_date"] # ordering = ["-create_date"] : '-' works like not
         




