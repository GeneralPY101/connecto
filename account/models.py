from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Profile(models.Model) : 
	user = models.OneToOneField(User,on_delete = models.CASCADE,related_name='profile')
	user_image = models.ImageField(upload_to='Profiles',default='default/profile.png')
	bio = models.CharField(max_length=100,blank=True)
	connection = models.CharField(max_length=255,blank=True)
	follower = models.IntegerField(default=0)
	following = models.IntegerField(default =0 )

	def __str__(self) :
		return f'{self.user}'

@receiver(post_save,sender=User) 
def create_auth_token(sender,instance=None,created=False,**kwargs) :
	if created : 
		Token.objects.create(user=instance)