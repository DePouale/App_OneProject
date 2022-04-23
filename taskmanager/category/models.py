from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ('Категории')

    def __str__(self):
        return f'{self.name} | parent - {self.parent}' if self.parent else self.name