from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='products', default='defaults/hetfield.jpg')

    class Meta:
        verbose_name = 'ürünler'
        verbose_name_plural = 'ürün'

    def __str__(self):
        return f'{self.name}'
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_relaesed = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return f'{self.product} - {self.review}'