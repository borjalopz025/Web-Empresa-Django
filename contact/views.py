from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms

# Create your views here.

def contact (req):
    
    contact_form = ContactForms()

    if req.method == "POST":
        contact_form = ContactForms(data=req.POST)
        if contact_form.is_valid():
            name = req.POST.get('name', '')
            email = req.POST.get('email', '')
            content = req.POST.get('content', '')
            mail = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n {}".format(name,email,content),
                "No-contestar@inbox.mailtrap.io",
                ['borjaswim1995@gmail.com'],
                reply_to=[email]
            )
            try:
                mail.send()
                return redirect('/con/?ok')
            except:
                return redirect('/con/?fail')
            

    return render(req, 'contact/contact.html', {'form': contact_form})
