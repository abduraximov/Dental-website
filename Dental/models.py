from email.mime import image
from pydoc import describe
from pyexpat import model
from tkinter import CASCADE
from unicodedata import category
from django.db import models

class About(models.Model):
    description = models.TextField(null=True, blank=True)
    ex_dentist = models.IntegerField()
    mod_equip = models.IntegerField()
    friendly_staff = models.IntegerField()
    exp_year = models.IntegerField()
    happy_patients = models.IntegerField()
    certificate = models.IntegerField()

    def __str__(self):
        return self.description

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    blog_img = models.ImageField(null=True, blank=True, upload_to="images/")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title