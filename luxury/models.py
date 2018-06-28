from django.db import models
from django.core.urlresolvers import reverse
from djangocms_text_ckeditor.fields import HTMLField

from mice.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.


class LuxuryTravel(models.Model):
    name = models.CharField(verbose_name='Luxury Name', max_length=50)
    # title = models.CharField(verbose_name='Luxury Title',
    #                          max_length=150, blank=True)
    description = HTMLField(verbose_name='Luxury Description', blank=True)
    top_image = models.ImageField(verbose_name='Preview image',
                                  upload_to='luxury')
    slug = models.SlugField('Slug', max_length=50, unique=True, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'luxury'
        ordering = ['name', ]
        verbose_name = 'Luxury Travel'
        verbose_name_plural = 'Luxury Travels'

    def __str__(self):
        return self.name

    @property
    def absolute_url(self):
        return reverse('luxury:luxury_detail', kwargs={'slug': self.slug})

    @property
    def get_next(self):
        next = self.__class__.objects.exclude(name='zzz').filter(name__gt=self.name).order_by('name')
        print('next: {}'.format(next))
        try:
            return next[0].absolute_url
        except IndexError:
            return False

    @property
    def get_prev(self):
        prev = self.__class__.objects.exclude(name='zzz').filter(name__lt=self.name).order_by('-name')
        print('prev: {}'.format(prev))
        try:
            return prev[0].absolute_url
        except IndexError:
            return False


class LuxuryTravelImage(models.Model):
    image = models.ImageField(upload_to='luxury', blank=True, null=True)
    luxury = models.ForeignKey(LuxuryTravel, verbose_name='Luxury')

    class Meta:
        verbose_name = 'Luxury Glaery Image'
        verbose_name_plural = 'Luxury Galery Images'

    def get_image(self):
        return self.image.url


@receiver(pre_save, sender=LuxuryTravel)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
