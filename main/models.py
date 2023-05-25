from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Names", unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Product(models.Model):
    image = models.ImageField(upload_to="products/", verbose_name="Image")
    name_product = models.CharField(max_length=50, verbose_name="Name")
    description = models.TextField(max_length=300, verbose_name="Description")
    price = models.PositiveIntegerField(verbose_name="Price") #1 : 9999999
    # price = models.PositiveBigIntegerField     # 1 : infinity
    # price = models.PositiveSmallIntegerField   # 1 : 999999
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self) -> str:
        return f"Category: {self.category} | Name product: {self.name_product} | Price: {self.price}"
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Comment(models.Model):
    # on_delete=models.CASCADE удаляет всю связанную информацию о продукте
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Choose a product")
    username = models.CharField(max_length=50, verbose_name="Username")
    email = models.EmailField(max_length=155, verbose_name="Email")
    # help_text правила илиже вспогательная строка
    comment = models.TextField(max_length=200, verbose_name="Comments", help_text="the comment must be in the range of 200 characters")    

    def __str__(self) -> str:
        return f"Username: {self.username} | Comments: {self.comment}"
        
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"