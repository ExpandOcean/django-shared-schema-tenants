from django.core.management.base import BaseCommand, CommandError
from shared_schema_tenants.models import Tenant
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Creates a new Tenant'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        name = input('Enter the Tenant name: ')
        slug = input('Enter the Tenant slug: (%s)' % slugify(name))

        if not slug:
            slug = slugify(name)

        Tenant.objects.create(name=name, slug=slug)

        self.stdout.write(self.style.SUCCESS('Successfully created Tenant %s' % name))