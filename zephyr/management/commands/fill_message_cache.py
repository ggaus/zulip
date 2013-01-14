from optparse import make_option
from django.core.management.base import BaseCommand
from zephyr.lib.message_cache import populate_message_cache

class Command(BaseCommand):
    option_list = BaseCommand.option_list
    help = "Populate the memcached cache of messages."

    def handle(self, *args, **options):
        populate_message_cache()
