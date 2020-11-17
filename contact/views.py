from django.views.generic.edit import FormView
from .models import ContactRequest
from .forms import ContactForm
from django.core.mail import send_mail


class ContactView(FormView):
    model = ContactRequest
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'

    def form_valid(self, form):
        send_mail(
            subject = form.cleaned_data.get('name'),
            message = form.cleaned_data.get('content'),
            from_email = form.cleaned_data.get('email'),
            recipient_list = ['blambor@gmail.com'])
        form.save()
        return super(ContactView, self).form_valid(form)
