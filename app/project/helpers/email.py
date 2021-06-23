from django.core.mail import send_mail


def send_email(subject, message, recipient):
    send_mail(subject,
              message,
              'notification.motionteam1@gmail.com',
              [recipient],
              fail_silently=False,
              )
