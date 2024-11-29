from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from shopsite.forms import ContactForm
from shopsite.models import MenuItem
#from web.models import MenuItem

#from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(
        request,
        'index.html'
    )
def about(request):
    return render(
        request,
        'about.html'
    )
def cart(request):
    return render(
        request,
        'cart.html'
    )
def checkout(request):
    return render(
        request,
        'checkout.html'
    )
def contact_us(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'contact-us.html',
        context=context
    )

def gallery(request):
    return render(
        request,
        'gallery.html'
    )
def my_account(request):
    return render(
        request,
        'my-account.html'
    )
def shop(request):
    menu_veg = MenuItem.objects.filter(type__exact='VEG').order_by('?')[:6]
    menu_fru = MenuItem.objects.filter(type__exact='FRU').order_by('?')[:6]
    menu_mea = MenuItem.objects.filter(type__exact='MEA').order_by('?')[:6]
    context = {'menu_veg': menu_veg, 'menu_fru': menu_fru, 'menu_mea': menu_mea}
    return render(
        request,
        'shop.html', context
    )
def shop_detail(request):
    return render(
        request,
        'shop-detail.html'
    )
def wishlist(request):
    return render(
        request,
        'wishlist.html'
    )


def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()





