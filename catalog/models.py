from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название категории")

    def __str__(self):
        return f'NAME {self.name}'


class ProductModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название продукта")
    price = models.IntegerField(verbose_name="Цена")
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name="Категория")
    bought = models.BooleanField(verbose_name="Куплено")
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f'Name - {self.name}, price - {self.price} {self.category} {self.bought}, date - {self.date}'