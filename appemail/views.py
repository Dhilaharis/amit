from django.shortcuts import render, redirect,HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage

def send_email_with_attachment(username, recipient_email, subject, message, file=None):
    # Create email subject and body using context
    email_subject = subject
    email_body = render_to_string('email_template.html', {
        'username': username,
        'message': message,
    })
    
    # Create the email
    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
    )
    
    # Attach file if provided
    if file:
        email.attach(file.name, file.read(), file.content_type)
    
    # Send email
    email.send()
    
def home_page(request):
    return render(request, 'index.html')
