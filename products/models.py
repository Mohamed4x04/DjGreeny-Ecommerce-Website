from ctypes.wintypes import tagSIZE
from distutils.command.upload import upload
from email.charset import Charset
from email.mime import image
from itertools import product
from pickle import TRUE
from pyexpat import model
from statistics import mode
from unicodedata import category
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from django.forms import CharField
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from pytz import timezone
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.

FLAG_TYPE = [
    ('new' , 'new'),
    ('feature' , 'feature'),
]


class ProductQuerset(models.QuerySet):
    def price_greater_than(self,price):
        return self.filter(price__gt=price) 



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerset(self.model , using=self._db)
    
    
    
    def price_greater_than(self,price):
        return self.get_queryset().price_greater_than(price)
    



class Product(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    sku = models.FloatField(_("SKU"))
    brand = models.ForeignKey('Brand',verbose_name=("brand"),related_name='products_brand',on_delete=models.SET_NULL, null=True, blank=True )
    price = models.FloatField(_("price"),)
    desc = models.TextField(_("Desc"),max_length=1000)
    flag = models.CharField(max_length=10 , choices=FLAG_TYPE)
    category=models.ForeignKey('category',verbose_name=("category"),related_name='products_category',on_delete=models.SET_NULL,null=True,blank=True)
    slug = models.SlugField(null=True , blank=True)
    tags = TaggableManager(blank=True)
    image= models.ImageField(upload_to='Products/')
    quantity = models.IntegerField(default=0)
    
    objects=ProductManager()
    
    def save(self, *args , **kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)


    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={"slug": self.slug})
    
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product,verbose_name=_("Product"),related_name='product_image',on_delete=models.CASCADE)    
    image = models.ImageField(_("Image"),upload_to='Product/',)
    
    def __str__(self):
        return str(self.product)
    
class Brand(models.Model):
    name = models.CharField(_("Name"),max_length=50)    
    image = models.ImageField(_("Image"),upload_to='brand/',)
    slug = models.SlugField(null=True , blank=True)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args , **kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)

        

    

class Category(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    image = models.ImageField(_("Image"), upload_to='Category/')

    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=_("User"), related_name='review_author', on_delete=models.SET_NULL, null=True, blank=True )
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='product_review', on_delete=models.CASCADE)
    review = models.TextField(_("Review"),max_length=1000)
    rate = models.FloatField(_("Rate"),validators=[ MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(_("Created_at"),default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"