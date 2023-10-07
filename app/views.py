from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
import os
from django.template.loader import get_template

# Create your views here.


def send_single(request):
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["huericnan@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Emails sent.")


def send_mass(request):
    mails = (
        ("Subject #1", "Message #1", "from@example.com", ["huericnan@gmail.com"]),
        ("Subject #2", "Message #2", "from@example.com", ["huericnan@gmail.com"]),
        ("Subject #3", "Message #3", "from@example.com", ["huericnan@gmail.com"]),
        ("Subject #4", "Message #4", "from@example.com", ["huericnan@gmail.com"]),
        ("Subject #5", "Message #5", "from@example.com", ["huericnan@gmail.com"]),
    )
    send_mass_mail(mails)

    return HttpResponse("Emails sent.")


def send_attachment(request):
    email = EmailMessage(
        "Hello",
        "Body goes here",
        "from@example.com",
        ["huericnan@gmail.com"],
    )

    image_path = os.path.join('files/image.excalidraw.png')
    with open(image_path, 'rb') as f:
        img_data = f.read()

    email.attach("image.png", img_data, "image/png")

    email.send()

    return HttpResponse("Email sent with attachment.")


def send_html(request):
    subject, from_email, to = "Hello!", "from@example.com", "huericnan@gmail.com"
    text_content = "This is a message written in HTML."
    html_content = "<p>This is an <strong>important</strong> message.</p>"
    email = EmailMultiAlternatives(subject, text_content, from_email, [to])
    email.attach_alternative(html_content, "text/html")
    email.send()

    return HttpResponse("HTML email sent.")

def send_html_template(request):
    subject, from_email, to = "Hello!", "from@example.com", "huericnan@gmail.com"
    
    text = get_template('email.txt')
    html = get_template('email.html')

    username = 'jack'

    d = { 'username': username }

    text_content = text.render(d)
    html_content = html.render(d)

    email = EmailMultiAlternatives(subject, text_content, from_email, [to])
    email.attach_alternative(html_content, "text/html")
    email.send()

    return HttpResponse("HTML email sent.")