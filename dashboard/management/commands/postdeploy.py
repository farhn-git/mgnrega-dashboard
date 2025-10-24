from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Run post-deploy setup"

    def handle(self, *args, **options):
        call_command("migrate")
        call_command("collectstatic", "--noinput")