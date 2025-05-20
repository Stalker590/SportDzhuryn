from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    description = models.TextField(verbose_name="Опис товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='products/', verbose_name="Зображення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
