from django.db import models
# from filer.fields.image import FilerImageField
from solo.models import SingletonModel

# Create your models here.


class TeamMember(models.Model):
    name = models.CharField('Name', max_length=50)
    position = models.CharField('Position', max_length=50, blank=True)
    presentation = models.CharField('Presentation', max_length=300, blank=True)
    photo = models.ImageField(verbose_name='Photo',
                              upload_to='team')
    email = models.EmailField('Email', max_length=254)

    class Meta:
        app_label = 'aboutus'
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name


class CompanyInfo(SingletonModel):
    name = models.CharField('Name', max_length=50,
                            default='Company Name')
    email = models.EmailField('Email', max_length=254,
                              default='e@mail.com')
    phone = models.CharField('Phone', max_length=30,
                             default='+79999999999')
    adress = models.CharField('Adress',
                              max_length=200, blank=True)
    fb_url = models.URLField('Facebook Url', max_length=200,
                             default='fb.com')
    insta_url = models.URLField('Instagram Url', max_length=200,
                                default='inst.com')

    class Meta:
        verbose_name = 'Company Config'

    def __str__(self):
        return 'Company Config'
