from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.core.urlresolvers import reverse

from mice.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.


class Destination(models.Model):
    name = models.CharField(verbose_name='Name of destination', max_length=100)
    description = HTMLField(verbose_name='Description', blank=True, null=True,)
    top_image = models.ImageField(verbose_name='Preview image',
                                  upload_to='destin')
    slug = models.SlugField('Slug', max_length=50, unique=True, blank=True, null=True)

    class Meta:
        app_label = 'destin'
        ordering = ['name', ]
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return self.top_image.url

    @property
    def absolute_url(self):
        return reverse('destin:destination_detail', kwargs={'slug': self.slug})

    @property
    def get_next(self):
        next = self.__class__.objects.exclude(name='zzz').filter(name__gt=self.name).order_by('name')
        try:
            return next[0].absolute_url
        except IndexError:
            return False

    @property
    def get_prev(self):
        prev = self.__class__.objects.exclude(name='zzz').filter(name__lt=self.name).order_by('-name')
        try:
            return prev[0].absolute_url
        except IndexError:
            return False


class DestinationImage(models.Model):
    image = models.ImageField(upload_to='destin', blank=True, null=True)
    destination = models.ForeignKey(Destination, verbose_name='Destination')

    class Meta:
        verbose_name = 'Destination Glaery Image'
        verbose_name_plural = 'Destination Galery Images'

    def get_image(self):
        return self.image.url


@receiver(pre_save, sender=Destination)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
