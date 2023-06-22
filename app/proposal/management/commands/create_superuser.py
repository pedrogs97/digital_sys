from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Creating superuser...')
        User = get_user_model()
        try:
            User.objects.create_superuser('admin', 'admin@email.com', 'admin@123')
            self.stdout.write(self.style.SUCCESS('Created!'))
        except:
            self.stdout.write(self.style.SUCCESS('Already exists.'))
