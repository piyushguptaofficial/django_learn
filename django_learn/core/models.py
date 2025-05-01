########## Django ORM ###########
# ORM stands for Object-Relational Mapping.

# The Django ORM is a built-in feature that lets you interact
#  with your database using Python classes and objects instead 
# of raw SQL queries.


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemListView(ListView):
    model = ItemListView
    template_name = 'item_list.html'
    context_object_name = 'items'

# File Uploads
# class Document(models.Model):
#     title = models.CharField(max_length=100)
#     file = models.FileField(upload_to='documents/')
#     image = models.ImageField(upload_to='images/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# Create a new item instead of SQL INSERT
# item = Item(name="Shoes", price=59.99)
# item.save()

# Fetch items instead of SQL SELECT
# items = Item.objects.all()

# Filter items
# cheap_iteams = Item.objects.filter(price__lt=50)

# Update
# item.price = 49.99
# item.save()

# Delete
# item.delete()
