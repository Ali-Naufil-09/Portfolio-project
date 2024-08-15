from django.db import models

# Create your models here.

#creating table(model) for storing projects
class Project(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    images=models.ImageField(upload_to='images/')  #folder of images is automatically created. we only need to add upload_to a statement and the respective folder    
#to resolve the issue of object1 , object2 in projects folder in admin
    def __str__(self):
       return self.title
    