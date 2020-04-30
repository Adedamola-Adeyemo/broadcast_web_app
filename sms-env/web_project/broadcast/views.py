from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

def broadcast_sms(request):
    message_to_broadcast = ('Testing out AboCoders Covid19 response SMS app. See what we do at https://abocoders.org.ng')
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                    from_=settings.TWILIO_NUMBER,
                                    body=message_to_broadcast)
    return HttpResponse('Message sent', 200)
