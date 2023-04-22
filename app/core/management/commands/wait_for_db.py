"""
Dajngo command to wait for databade to bee available

"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Dajngo command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("Wait for database .....")
        db_up = False
        while db_up is False:
            try:
                self.check(database=['default'])
                db_up = True
            except (Psycopg2Error,  OperationalError):
                self.stdout.write('Database not available, waiting 1 seccond...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

