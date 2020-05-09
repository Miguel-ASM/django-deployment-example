#SetUp the django environment
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myTask.settings')

import django
django.setup()

#Script to populate my db with fake data of fake riders
from myApp.models import Rider
from faker import Faker

#fake data generator
fakeGenerator = Faker()

def add_nationality(rider):
    rider.riderNationality = fakeGenerator.country()
    rider.save()
    return

if __name__ == '__main__':
    for rider in Rider.objects.all():
        add_nationality(rider)
