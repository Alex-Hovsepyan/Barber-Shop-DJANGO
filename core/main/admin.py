from django.contrib import admin
from .models import Sidebar, Home, About, AboutContent, Service, ServiceContent, BookaSeat, BookaSeatContact
from .models import PriceList, PriceListContent, Contact, Footer, FooterContent
# Register your models here.

admin.site.register(Sidebar)
admin.site.register(Home)
admin.site.register(AboutContent)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(ServiceContent)
admin.site.register(BookaSeat)
admin.site.register(BookaSeatContact)
admin.site.register(PriceList)
admin.site.register(PriceListContent)
admin.site.register(Contact)
admin.site.register(Footer)
admin.site.register(FooterContent)