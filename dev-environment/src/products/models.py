from django.db import models

# Create your models here.
class Product(models.Model):    # CamelCase modafocka
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(
        decimal_places = 2,
        max_digits = 20,
        default = 0.99
    )

    def __str__(self):      # python3
        return self.title

    # def __unicode__(self):    # python2
    #     return self.title
