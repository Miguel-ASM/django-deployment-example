#SetUp the django environment
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myTask.settings')

import django
django.setup()

#Script to populate my db with fake data of fake riders
from myApp.models import Rider
import random
from faker import Faker

#fake data generator
fakeGenerator = Faker()

#dictionary of bikes brands and models
bikes = {
    'orbea':['oiz','alma','orca','orca-aero','avant'],
    'giant':['defy','tcr'],
    'bianchi':['oltre','celeste'],
    'specialized':['venge','tarmac','roubaix']
}
bikes_brands = list(bikes.keys())

def create_fake_Rider():
    riderName = fakeGenerator.name()
    riderNationality = fakeGenerator.country()
    riderBirthData = fakeGenerator.date_of_birth(minimum_age=18, maximum_age=70)
    bikeBrand = random.choice(bikes_brands)
    bikeModel = random.choice(bikes[bikeBrand])

    Rider.objects.get_or_create(
        riderName=riderName,
        riderNationality=riderNationality,
        riderBirthData=riderBirthData,
        bikeBrand=bikeBrand,
        bikeModel=bikeModel
    )[0]

if __name__ == '__main__':
    for n in range(500):
        create_fake_Rider()
