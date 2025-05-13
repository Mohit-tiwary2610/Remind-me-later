from django.db import models

# Create your models here.
from django.db import models


class Reminder(models.Model):
    # Choices for the reminder method
    REMINDER_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]
    # Message to be sent
    message = models.TextField()

    # Date and time when the reminder should be triggered
    remind_at = models.DateTimeField()

    # Method of sending reminder (e.g., SMS or Email)
    remind_via = models.CharField(max_length=10, choices=REMINDER_CHOICES)

    # Timestamp of when the reminder was created
    created_at = models.DateTimeField(auto_now_add=True)

    """
    Can add fields for remind to user using users email, mobile number
    Or can use user as foreignkey and access his username and any other details like mobile number.
    """

    def __str__(self):
        return f"{self.remind_via} reminder at {self.remind_at}"
