from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.db.models import F, Max
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
import datetime
import os

def get_upload_path(instance, filename):
        """ creates unique-Path & filename for upload """
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.pic_id, ext)
        
        return os.path.join(
            'art', filename
        )

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gold = models.IntegerField(default = 50)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Art(models.Model):
	creator  = models.ForeignKey(UserProfile, blank=True, null=True)
	category = models.CharField(max_length=15)
	text     = models.TextField()
	art_id = models.IntegerField(default=1) 
	art_votes = models.IntegerField(default=0) 
	submission_date  = models.DateTimeField(
        'submission date', default=timezone.now,blank=True)   
	def __unicode__(self):              # __unicode__ on Python 2
		return self.text
class WinningArt(models.Model):
    creator  = models.ForeignKey(UserProfile)
    category = models.CharField(max_length=15)
    text     = models.TextField()
    submission_date  = models.DateTimeField(
        'submission date', default=timezone.now,blank=True)

class Picture(models.Model):
    # Original
    file = models.ImageField(upload_to=get_upload_path)
    pic_id = models.IntegerField(default=0);

