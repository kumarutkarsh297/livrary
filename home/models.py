from django.db import models

# Create your models here.
class Books(models.Model):
    bname = models.CharField(max_length=20)
    bisbn = models.CharField(max_length=20)
    bauthor = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.bname
class Members(models.Model):
    name = models.CharField(max_length=20)
    phno = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    doj = models.DateField()
    address = models.TextField()
    def __str__(self):
        return self.name
class Rates(models.Model):
    isbn = models.CharField(max_length=20)
    charge = models.CharField(max_length=5)
    def __str__(self):
        return self.isbn
class Issued(models.Model):
    ref = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)
    bookname = models.CharField(max_length=40)
    customername = models.CharField(max_length=40)
    from_date = models.DateField()
    to_date = models.DateField()
    charge = models.CharField(max_length=5)
    returned = models.BooleanField()
    charged = models.CharField(max_length=5, default='0')
    def __str__(self):
        return self.ref