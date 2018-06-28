from django.db import models
from django.core.urlresolvers import reverse
from djangocms_text_ckeditor.fields import HTMLField

from mice.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.


class Platform(models.Model):
    name = models.CharField(verbose_name='Platform Name', max_length=50)
    # title = models.CharField(verbose_name='Platform Title',
    #                          max_length=150, blank=True)
    description = HTMLField(verbose_name='Platform Description', blank=True)
    top_image = models.ImageField(verbose_name='Preview image',
                                  upload_to='platforms')
    slug = models.SlugField('Slug', max_length=50, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'world'
        ordering = ['name', ]
        verbose_name = 'Platform Travel'
        verbose_name_plural = 'Platform Travels'

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return self.top_image.url

    @property
    def absolute_url(self):
        return reverse('world:platform_detail', kwargs={'slug': self.slug})

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


class PlatformImage(models.Model):
    image = models.ImageField(upload_to='platforms', blank=True, null=True)
    platform = models.ForeignKey(Platform, verbose_name='Platform')

    class Meta:
        verbose_name = 'Platform Glaery Image'
        verbose_name_plural = 'Platform Galery Images'

    def get_image(self):
        return self.image.url


@receiver(pre_save, sender=Platform)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
