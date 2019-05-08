from django.core.management import BaseCommand
from core_app.models import User, Organization, EDisabledAccount
from django.db.models import Q, F
from django.conf import settings
from datetime import timedelta
from django.utils import timezone

from django.core.mail import send_mail

arcabot, _ = User.objects.get_or_create(
email=settings.ARCAMENS_BOT_EMAIL, name=settings.ARCAMENS_BOT_NAME)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Run the event/emails but doesnt disable the accounts at all.
        now = timezone.now().today().date()
        query = Q(paid=True, expiration__lte=now)
        users = User.objects.filter(query)

        users = users.prefetch_related('owned_organizations')
        users = users.only('id', 'email')

        for ind in users:
            self.disable(ind)

        # Fully disable the accounts just one day after
        # the expiration arouse.
        users = User.objects.filter(paid=True)
        query = Q(paid=True, expiration__lt=now)
        users = User.objects.filter(query)
        users.update(enabled=False)
        self.stdout.write('Checked expiration!')
    
    def disable(self, user):
        reason = 'Your accounnt expiration has ran over!'
        for ind in user.owned_organizations.all():
            event = EDisabledAccount.objects.create(organization=ind,
                user=arcabot, reason=reason)
            event.dispatch(user)

        send_mail('Your account has expired!', 
        'In order to proceed using arcamens, purchase a new period.',
                'noreply@arcamens.com', [user.email], fail_silently=True)

    






