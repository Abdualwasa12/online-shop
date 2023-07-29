from django.db import models

# Create your models here.


class Brand(models.Model):
    BRDName = models.CharField(max_length=40)
    BRDDesc = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.BRDName



class Variant(models.Model):
    VARName = models.CharField(max_length=40)
    VARDesc = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = ("Variant")
        verbose_name_plural = ("Variants")

    def __str__(self):
        return self.VARName



