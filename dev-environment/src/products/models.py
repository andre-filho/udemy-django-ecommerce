import random
import os

from django.db import models

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

# large files upload guide: http://kirr.com/e1133t
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 91209319320)
    name, ext =  get_filename_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    # py3.6
    # final_name = f'{new_filename}{ext}'
    return "products/{r}/{name}".format(r=new_filename, name=final_name)

# Create your models here.
class Product(models.Model):    # CamelCase modafocka
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(
        decimal_places = 2,
        max_digits = 20,
        default = 0.99
    )
    image       = models.ImageField(    # pip install pillow
        upload_to = upload_image_path,
        null = True,
        blank = True
    )

    def __str__(self):      # python3
        return self.title

    # def __unicode__(self):    # python2
    #     return self.title
