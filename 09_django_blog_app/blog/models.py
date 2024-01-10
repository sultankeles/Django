from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    STATUS = (
        ('p', 'Public'),
        ('d', 'Draft'),
    )
    title = models.CharField(max_length= 300, unique=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    status = models.CharField(max_length=10, choices=STATUS, default='d')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.status}'