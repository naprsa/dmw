from django.db import models
# from filer.fields.image import FilerImageField

# Create your models here.


class Slider(models.Model):

    image = models.ImageField(verbose_name='Slider Image', upload_to='slider')
    title = models.CharField(blank=True, null=True,
                             max_length=255, verbose_name='Title')

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url


class ContactMessage(models.Model):
    message = models.TextField('Message', max_length=500)
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=30, blank=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-date_created', ]

    def __str__(self):
        return self.name
