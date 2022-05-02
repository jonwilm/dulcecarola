from django.conf import settings
from applications.newsletter.forms import NewsletterForm


def NewsletterFormGlobal(request):
    return {
        'newsletter_form': NewsletterForm()
    }
