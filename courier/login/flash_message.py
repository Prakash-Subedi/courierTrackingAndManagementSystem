from django.contrib import messages
from django.contrib.auth.signals import user_logged_in

def logged_in_message(sender, user, request, **kwargs):
    """
    Add a welcome message when the user logs in
    """
    messages.info(request, "Welcome ...")
    user_logged_in.connect(logged_in_message)