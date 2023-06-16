from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_ticket_reservation_email(user_name,email,phone,visit_date,tickets):
    subject = 'Ticket Reservation Confirmation'
    html_message = render_to_string('ticket_email.html', {
        'user': user_name,
        'visit_date': visit_date,
        'phone': phone,
        'tickets': tickets,
        'contact_email': 'support@RCM.com'
    })
    send_mail(subject, '', 'zicocomlimited@gmail.com', [email], html_message=html_message)
