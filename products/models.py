from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shop', unique=True, blank=True)
    description = models.TextField()
    inStock = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated']


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    order = models.SlugField(primary_key=True, auto_created=True)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='orders')

    def save(self, *args, **kwargs):
        self.total = self.product.price * self.quantity
        super().save(*args, **kwargs)

