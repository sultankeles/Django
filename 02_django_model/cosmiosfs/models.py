from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    about = models.TextField()
    email = models.EmailField(blank=True)
    regester_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_activate = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="students")

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.number}"
    
    class Meta:
        ordering = ["number"]
        #ordering = ["-number"] Tersten sıralar.
        verbose_name_plural = "Student-Ogrenciler"
        verbose_name = "Ogrenciler"