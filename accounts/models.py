from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
  user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
  name = models.CharField(_("الاسم :"), max_length=50)
  who_i = models.TextField(_("من انا :"), max_length=250)  
  price = models.IntegerField(_("سعر الكشف :"), null=True, blank=True)
  

  class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

  def __str__(self):
        return '%s' %(self.user.username)
  

def create_profile(sender, **kwargs):
     if kwargs['created']:
          Profile.objects.create(user= kwargs['instance'])


post_save.connect(create_profile, sender=User)