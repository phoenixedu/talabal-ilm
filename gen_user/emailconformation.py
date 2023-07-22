from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse

def generate_conformation_token(user):
    token = default_token_generator.make_token(user)
    user.email_verification_token = token
    user.save()
    return token

def send_confirmation_email(user,request):
    token = generate_conformation_token(user)
    confirmation_link = request.build_absolute_uri(reverse('confirm_email', kwargs={'token': token}))
    subject = 'Confirm Your Email'
    message = render_to_string('emails/confirmation.html', {
        'user': user,
        'token': token,
        'confirmation_link':confirmation_link,
    })
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.content_subtype = "html"
    email.send()


    # send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])