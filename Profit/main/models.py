from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    status_list = (('in_stock', 'in_stock'), ('out_of_stock', 'out_of_stock'))
    product_name = models.CharField(max_length=90)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=status_list, max_length=255, null=True, blank=True)
    remains = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_name} {self.category} {self.price} {self.status} {self.remains}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Product's"




