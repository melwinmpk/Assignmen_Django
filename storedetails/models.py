from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# <!--  > Full Name ,Phone number-->
# <!--  > Client Value(In USD)(This can be any monetary value in dummy data)-->
# <!--  > eMail , website address-->
class userdetails(models.Model):
    Name    = models.CharField(max_length=200)
    Phone   = models.CharField(max_length=200)
    Cv      = models.CharField(max_length=200)
    email   =  models.CharField(max_length=200)
    website =  models.CharField(max_length=200)