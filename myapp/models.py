from django.db import models

# Create your models here.

def upload_location(instance, filename):
 return "%s/%s" %(instance.id, filename)

class Post(models.Model):
	Post_Name = models.CharField(max_length=100, null=True, blank=True)
	Post_Image = models.ImageField(upload_to = upload_location, null=True, blank=True)

	def __str__(self):
		return self.Post_Name
