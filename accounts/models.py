from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.


TYPE_OF_PERSON= (
     ("M" , "Male"),
     ('F', 'Female'),
)

class Profile(models.Model):
  user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
  name = models.CharField(_("الاسم :"), max_length=80)
  subtitle = models.CharField(_("نبذة عنك"), max_length=300)
  address = models.CharField(_("المحافظة :"), max_length=50)
  address_detail = models.CharField(_("العنوان بالتفصيل :"), max_length=100)
  number_phone = models.CharField(_("الهاتف :"), max_length=50)
  working_hours = models.CharField(_("عدد ساعات العمل :"), max_length=50)
  waiting_time  = models.IntegerField(_("مدة الانتظار :"), blank=True, null=True)
  doctor = models.CharField(_("دكتور؟"), max_length=50,blank=True, null=True )
  who_i = models.TextField(_("من انا :"), max_length=250, blank=True, null=True)  
  price = models.IntegerField(_("سعر الكشف :"), null=True, blank=True)
  facebook = models.CharField(max_length=100, null=True, blank=True)
  twitter = models.CharField(max_length=100, null=True, blank=True)
  google = models.CharField(max_length=100, null=True, blank=True)
  specialist_doctor = models.CharField(_("متخصص في؟"), max_length=100,blank=True, null=True )
  tye_of_person = models.CharField(_("النوع :"),choices=TYPE_OF_PERSON , max_length=50)
  slug = models.SlugField(_("slug"), blank=True, null=True)

  def save(self, *args, **kwargs):
       if not self.slug:
            self.slug = slugify(self.user.username)
       super(Profile, self).save(*args, **kwargs)


  class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

  def __str__(self):
        return  '%s' %(self.user.username)
  

def create_profile(sender, **kwargs):
     if kwargs['created']:
          Profile.objects.create(user= kwargs['instance'])


post_save.connect(create_profile, sender=User)