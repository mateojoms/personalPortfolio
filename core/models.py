from django.db import models

# Create your models here.
class about(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about',default='image')

    class meta:
        verbose_name = 'about me'
        verbose_name_plural = 'about me'

    def __str__(self):
        return 'about me'
class service(models.Model):
    name = models.CharField(max_length=200,verbose_name='service name')
    description = models.TextField(verbose_name='about service')

    def __str__(self):
        return self.name

class recentWorks(models.Model):
    title = models.CharField(max_length=200,verbose_name= 'work title')
    image = models.ImageField(upload_to='works',default= ' image.jpg')

    def __str__(self):
        return self.title

class client(models.Model):
    title = models.CharField(max_length=200,verbose_name='Client name')
    description = models.TextField(verbose_name='Client says')
    image = models.ImageField(upload_to='clients', default=' image.jpg')

    def __str__(self):
      return self.title
