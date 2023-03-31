from django.db import models

# Create your models here.

class Sidebar(models.Model):

    img = models.ImageField('Sidebar Image', upload_to='images')
    home = models.CharField('Home', max_length=25)
    about = models.CharField('About', max_length=25)
    service = models.CharField('Services', max_length=25)
    price = models.CharField('Price List', max_length=25)
    contact = models.CharField('Contact', max_length=25)

    class Meta:

        verbose_name = 'Sidebar'
        verbose_name_plural = 'Sidebar'

class Home(models.Model):

    title = models.CharField('Home Title', max_length=25)
    subtitle = models.CharField('Home Subtitle', max_length=50)
    btn_name_1 = models.CharField('Home Button 1', max_length=15)
    btn_name_2 = models.CharField('Home Button 2', max_length=15)
    text = models.CharField('Home Text', max_length=40)
    btn_name_3 = models.CharField('Home Button 3', max_length=15)
    img = models.ImageField('Home Image', upload_to='images')
    img2 = models.ImageField('Home Image 2', upload_to='images')

    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class About(models.Model):

    img = models.ImageField('About Image', upload_to='images')
    title = models.CharField('About Title', max_length=25)
    text = models.TextField('About Text')
    subtitle = models.CharField('About Subtitle', max_length=30)
    discount = models.CharField('About Discount', max_length=30)
    offer = models.CharField('About Offer', max_length=40)
    promocode = models.CharField('About Promocode', max_length=30)

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutContent(models.Model):

    img = models.ImageField('About Content Image', upload_to='images')
    name = models.CharField('About Content Barber Name', max_length=20)
    social = models.CharField('About Content Barber Social', max_length=60)
    social_url = models.CharField('About Content Social Url', max_length=300)

class Service(models.Model):

    title = models.CharField('Service Image', max_length=25)

class ServiceContent(models.Model):

    img = models.ImageField('Service Content Image', upload_to='images')
    title = models.CharField('Service Content Title', max_length=20)
    price = models.CharField('Service Content Price', max_length=15)

class BookaSeat(models.Model):

    title = models.CharField('Book a Seat Title', max_length=20)
    subtitle = models.CharField('Book a Seat SubTitle', max_length=60)
    btn_name = models.CharField('Book a Seat Button Name', max_length=15)
    img = models.ImageField('Book a Seat Image', upload_to='images')

    class Meta:

        verbose_name = 'BookaSeat'
        verbose_name_plural = 'BookaSeat'

class BookaSeatContact(models.Model):

    user_name = models.CharField('User Name', max_length=50)
    user_phone = models.CharField('User Phone Number', max_length=35)
    user_time = models.TimeField('User Time')
    user_place = models.CharField('User Place', max_length=30)
    user_date = models.DateField('User Date')
    user_count = models.CharField('User Count', max_length=20)
    user_text = models.TextField('User Text')

    def __str__(self) -> str:
        return self.user_name
    
class PriceList(models.Model):

    title = models.CharField('Price List Title', max_length=25)
    subtitle = models.CharField('Price List SubTitle', max_length=40)
    img = models.ImageField('Price List Image', upload_to='images')

    class Meta:

        verbose_name = 'PriceList'
        verbose_name_plural = 'PriceList'


class PriceListContent(models.Model):

    version = models.CharField('Price List Version', max_length=25)
    price = models.CharField('Price List Price', max_length=15)

    def __str__(self) -> str:
        return self.version
    
class Contact(models.Model):

    title = models.CharField('Contact Title', max_length=25)
    subtitle = models.CharField('Contact SubTitle', max_length=40)
    phone_number = models.CharField('Contact Phone Number', max_length=40)
    email = models.EmailField('Contact Email')
    social = models.CharField('Contact Social', max_length=80)
    day = models.CharField('Contact Day', max_length=20)
    time = models.CharField('Contact Time', max_length=40)

class Footer(models.Model):

    title = models.CharField('Footer Title', max_length=30)
    subtitle = models.CharField('Footer Subtitle', max_length=60)
    symbol = models.CharField('Footer Symbol', max_length=40)

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

class FooterContent(models.Model):

    title = models.CharField('Footer Content Title', max_length=30)
    subtitle = models.CharField('Footer Content SubTitle', max_length=60)

    def __str__(self) -> str:
        return self.title