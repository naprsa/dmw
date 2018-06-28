from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.core.urlresolvers import reverse

from mice.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(verbose_name='Hotel name', max_length=50)
    description = HTMLField(verbose_name='Description', blank=True)
    # top_image = FilerImageField(verbose_name='Hotel picture', null=True)
    # rooms = models.SmallIntegerField(verbose_name='Number of rooms',
    #                                  blank=True, null=True)
    # rooms_capacity = models.SmallIntegerField(verbose_name='Room capacity',
    #                                           blank=True, null=True)
    # conference_area = models.SmallIntegerField(verbose_name='Conference hall area',
    #                                            blank=True, null=True)
    # conference_seats = models.SmallIntegerField(verbose_name='Conference hall seats number',
    #                                             blank=True, null=True)
    # stars_rating = models.SmallIntegerField(verbose_name='Hotel rating',
    #                                         blank=True, null=True)
    # phone = models.CharField(verbose_name='Hotel phone', max_length=20, blank=True)
    # email = models.EmailField(verbose_name='Hotel email', blank=True)
    # web_url = models.URLField(verbose_name='Hotel WEB Site', blank=True)
    # adress = models.CharField(verbose_name='Hotel adress', max_length=150, blank=True)
    # direction = models.ForeignKey(MICEDirection, verbose_name='Hotel on direction',
    #                               blank=True)
    # latitude = models.DecimalField(max_digits=9, decimal_places=7,
    #                                verbose_name='Latitude')
    # longitude = models.DecimalField(max_digits=9, decimal_places=7,
    #                                 verbose_name='Longitude')
    slug = models.SlugField('Slug', max_length=50, unique=True, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'hotels'
        verbose_name = 'Hotel Represaentation'
        verbose_name_plural = 'Hotel Represaentations'

    def __str__(self):
        return 'Hotel ' + self.name

    @property
    def absolute_url(self):
        return reverse('hotels:hotel_detail', kwargs={'slug': self.slug})

    @property
    def get_next(self):
        next = self.__class__.objects.filter(pk__gt=self.pk)
        try:
            return next[0].absolute_url
        except IndexError:
            return False

    @property
    def get_prev(self):
        prev = self.__class__.objects.filter(pk__lt=self.pk).order_by('-pk')
        try:
            return prev[0].absolute_url
        except IndexError:
            return False


class HotelImage(models.Model):
    image = models.ImageField(upload_to='hotels', blank=True, null=True)
    hotel = models.ForeignKey(Hotel, verbose_name='Hotel')

    class Meta:
        verbose_name = 'Hotel Glaery Image'
        verbose_name_plural = 'Hotel Galery Images'

    def get_image(self):
        return self.image.url


@receiver(pre_save, sender=Hotel)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
