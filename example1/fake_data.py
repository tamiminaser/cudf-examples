import csv
from faker import Faker
import datetime
from tqdm import tqdm

def datagenerate(records, headers):
    fake = Faker('en_US')
    with open("data_10000000.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in tqdm(range(records)):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            
            writer.writerow({
                    "user_id": fake.unique.random_int(min=1111111111111, max=9999999999999),
                    "name": fake.name(),
                    "date_of_birth" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "country_of_birth": fake.country(),
                    "email": fake.email(),
                    "record_year": fake.year(),
                    "score": fake.random_int(min=1, max=999),
                    })
    
records = 100000000
headers = ["user_id", "name", "date_of_birth", "country_of_birth", "email", "record_year", "score"]
datagenerate(records, headers)
print("CSV generation complete!")
