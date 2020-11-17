from django.views.generic.edit import FormView
from .models import ContactRequest
from .forms import ContactForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage


class ContactView(FormView):
    model = ContactRequest
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'

    def form_valid(self, form):
        email = EmailMessage(
            form.cleaned_data.get('name'),
            form.cleaned_data.get('content'),
            form.cleaned_data.get('email'),
            ['debug@mir.de'],
            reply_to=[form.cleaned_data.get('email')])
        email.send()
        form.save()
        return super(ContactView, self).form_valid(form)
