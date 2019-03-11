from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    # print(f"Peticion {request.method}")
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) 
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Send email and redirect
            email = EmailMessage(
                "La Caffettiera: Nuewvo mensaje de contacto",
                f"De {name} <{email}>\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["luis.fernando.mtz.glez0970@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                # Everything went OK, redirect OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Something went wrong, redirect FAIL
                return redirect(reverse('contact')+"?fail")
        
    return render(request, "contact/contact.html", {'form': contact_form})