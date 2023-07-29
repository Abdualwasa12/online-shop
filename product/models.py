from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# from django.core.urlresolvers import reverse
# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=100 , verbose_name=("Product Name "))
    PRDCategory = models.ForeignKey('Category' , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=("Category "))
    PRDBrand = models.ForeignKey('settings.Brand' , on_delete=models.CASCADE , blank=True, null=True ,verbose_name=("Brand "))
    PRDDesc = models.TextField(verbose_name=("Description"))
    PRDImage = models.ImageField(upload_to='prodcut/' , verbose_name=("Image") , blank=True, null=True)
    PRDPrice = models.DecimalField(max_digits=5  , decimal_places=2 , verbose_name=("Price"))
    PRDDiscountPrice = models.DecimalField(max_digits=5  , decimal_places=2 , verbose_name=("Discount Price"))    
    PRDCost = models.DecimalField(max_digits=5 , decimal_places=2 , verbose_name=("Cost"))
    PRDCreated = models.DateTimeField(verbose_name=("Created At"))

    PRDSLug = models.SlugField(blank=True, null=True , verbose_name=("Product URL"))
    PRDISNew = models.BooleanField(default=True , verbose_name=("New Product "))
    PRDISBestSeller = models.BooleanField(default=False , verbose_name=("Best Seller"))

    
    def save(self , *args , **kwargs):
        if not self.PRDSLug :
            self.PRDSLug = slugify(self.PRDName)
        super(Product , self).save(*args , **kwargs)
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.PRDSLug})

    def __str__(self):
        return self.PRDName





class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name=("Product"))
    PRDIImage = models.ImageField(upload_to='prodcut/' , verbose_name=("Image"))

    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):
    CATName = models.CharField(max_length=50 , verbose_name=("Name"))
    CATParent = models.ForeignKey('self' ,limit_choices_to={'CATParent__isnull' : True}, verbose_name=("Main Category"), on_delete=models.CASCADE , blank=True, null=True)
    CATDesc = models.TextField( verbose_name=("Description"))
    CATImg = models.ImageField(upload_to='category/' , verbose_name=("Image"))

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.CATName



class Product_Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='main_prodcut' , verbose_name=("Product"))
    PALNAlternatives = models.ManyToManyField(Product , related_name='alternative_products'  , verbose_name=("Alternatives"))
    
    class Meta:
        verbose_name = ("Product Alternative")
        verbose_name_plural = ("Product Alternatives")

    def __str__(self):
        return str(self.PALNProduct)


class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='mainAccessory_prodcut' , verbose_name=("Product"))
    PACCAlternatives = models.ManyToManyField(Product , related_name='accessories_products' , verbose_name=("Accessories"))
      
    class Meta:
        verbose_name = ("Product Accessory")
        verbose_name_plural = ("Product Accessories")

    def __str__(self):
        return str(self.PACCProduct)





