from django.conf import settings
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.FileField(upload_to='media')
    price = models.IntegerField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, related_name='category_courses')

    def __str__(self):
        return self.title

    def get_image_url(self):
        return self.image.url

class Lectures(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    course = models.ForeignKey(Course, related_name='course_lectures', on_delete=models.CASCADE)
    stage = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['stage',]

class Material(models.Model):
    MaterialType= [('TEXT','text'),
                ('IMG' , 'image'),
                ('VIDEO' , 'video')]

    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='media', blank=True, null=True)
    type_file = models.CharField(max_length=10, choices=MaterialType, default=MaterialType[0])
    lecture = models.ForeignKey(Lectures, related_name='lecture_materials', on_delete=models.CASCADE)
    stage = models.IntegerField(default=1)

    def __str__(self):
        return self.title
