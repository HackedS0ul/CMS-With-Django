from django.conf import settings
from django.db import models
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Out Wear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)
LABEL_TEXT_CHOICES = (
    ('BestSeller','Bestseller' ),
    ('New', 'New')
)



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=400)
    short_description = models.CharField(max_length=250)
    label = models.CharField(max_length=2, choices=LABEL_CHOICES)
    label_text = models.CharField(choices=LABEL_TEXT_CHOICES, max_length=20)
    slug = models.SlugField()




    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('cms:product', kwargs = {'slug': self.slug})
    
    

class OrderItem(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):

    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()



    def __str__(self):
        return self.title
