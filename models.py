from django.db import models

# Create your models here.
class menu_snk(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

def __str__(self):
    return self.name;

class menu_frst(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

def __str__(self):
    return self.name;

class menu_scnd(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

def __str__(self):
    return self.name;

class menu_dsrt(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

def __str__(self):
    return self.name;
 
class Voucher(models.Model): 
    menu = models.CharField(max_length=250) 
    number_of_guests = models.CharField(max_length=3) 
    date = models.DateField() 
    time = models.TimeField() 
    name_and_surname = models.CharField(max_length=100) 
    email_address = models.EmailField() 
    telephone = models.CharField(max_length=20) 

class BookTable(models.Model): 
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    phone = models.CharField(max_length=20) 
    email = models.EmailField() 
    message = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=200)    
    author = models.ForeignKey(
        'auth.User',        
        on_delete=models.CASCADE,
    )    
    body = models.TextField()
    def __str__(self):
        return self.title    
    def get_absolute_url(self):        
        return reverse('post_detail', args=[str(self.pk)])
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=400)    
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_on']
    def __str__(self):       
         return self.comment[:60]

