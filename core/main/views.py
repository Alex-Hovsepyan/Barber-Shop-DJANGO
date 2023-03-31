from django.shortcuts import render, redirect
from .models import Sidebar, Home, About, AboutContent, Service, ServiceContent, BookaSeat, BookaSeatContact
from .models import PriceList, PriceListContent, Contact, Footer, FooterContent
from .forms import ContactModelForm
# Create your views here.

def index(request):
    sidebar_content = Sidebar.objects.all()[0]
    home_content = Home.objects.all()[0]
    about_info = About.objects.all()[0]
    about_content = AboutContent.objects.all()
    service = Service.objects.all()[0]
    service_content = ServiceContent.objects.all()
    book_a_seat = BookaSeat.objects.all()[0]
    price_list = PriceList.objects.all()[0]
    price_list_content = PriceListContent.objects.all()
    contact = Contact.objects.all()[0]
    footer = Footer.objects.all()[0]
    footer_content = FooterContent.objects.all()
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            BookaSeatContact.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactModelForm()
    
    return render(request, 'main/index.html', context={
        'sidebar_content':sidebar_content,
        'home_content':home_content,
        'about_info':about_info,
        'about_content':about_content,
        'service_content':service_content,
        'service':service,
        'book_a_seat':book_a_seat,
        'form':form,
        'price_list':price_list,
        'price_list_content':price_list_content,
        'contact':contact,
        'footer':footer,
        'footer_content':footer_content,
    })