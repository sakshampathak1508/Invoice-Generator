from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default="")
    price = models.PositiveSmallIntegerField(blank=True,null=True)
    desc  = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_name = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.order_name

class ItemList(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    price = models.PositiveSmallIntegerField(default=0)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        value = self.item.price
        price = value*self.quantity
        self.price = price
        super().save(*args,**kwargs)

    
