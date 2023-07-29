from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

from django.utils.text import slugify

from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(("image"), upload_to='profile_img', blank=True, null=True)
    address = models.CharField(max_length=100)
    join_date = models.DateTimeField(("join date"),default = datetime.datetime.now)
    

    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.user.username)
        super(Profile , self).save( *args , **kwargs)


    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return  '%s' %(self.user)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})


def create_profile(sender , **kwargs):
    print(kwargs)
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile , sender=User)