from django.core.management import BaseCommand

from customers.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = CustomUser.objects.create(
            email='egor@skypro.ru',
            is_superuser=True,
            is_staff=True,
        )
        user.set_password('EgorPash')
        user.save()