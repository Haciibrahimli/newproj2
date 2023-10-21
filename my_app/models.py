from django.db import models

# Create your models here.

class Author(models.Model):
    author = models.CharField(max_length=255,verbose_name='author') 

def __str__(self):
    return self.author

class Meta:
    ordering = ('author',)
    verbose_name = 'author'
    verbose_name_plural = 'authors'

class Keywords(models.Model):
    tags = models.CharField (max_length=255,verbose_name='tags')

def __str__(self):
    return self.tags

class Meta:
    ordering = ('tags',)
    verbose_name = 'tag'
    verbose_name_plural = 'tags'

class Book(models.Model):
    image = models.ImageField(upload_to='media/',null=True,blank=True)

     
class Category(models.Model):
    cat = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255,verbose_name='kateqoriya')
    seria_number = models.CharField(max_length=255,verbose_name='seria nomresi')

def __str__(self):
    return self.name

class Meta:
    ordering = ('name',)
    verbose_name = 'kateqoriya'
    verbose_name_plural = 'kateqoriyalar'
