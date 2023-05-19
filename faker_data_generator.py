import csv
import random
import string
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_sample_customers(num_customers):
    customers = []
    for i in range(1, num_customers + 1):
        customer = {
            'CustomerID': i,
            'FirstName': fake.first_name(),
            'LastName': fake.last_name(),
            'Email': generate_random_email()
        }
        customers.append(customer)
    return customers

def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'live.com', 'aol.com']
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)
    return f'{username}@{domain}'

def generate_sample_addresses(customers, num_addresses):
    addresses = []
    for customer in customers:
        for _ in range(num_addresses):
            start_date = datetime.now() - timedelta(days=random.randint(30, 365))
            end_date = None if random.random() < 0.8 else start_date + timedelta(days=random.randint(1, 365))
            active = end_date is None
            address = {
                'CustomerID': customer['CustomerID'],
                'Street': fake.street_address(),
                'City': fake.city(),
                'State': fake.state_abbr(),
                'ZipCode': random.randint(10000, 99999),
                'StartDate': start_date.strftime('%Y-%m-%d'),
                'EndDate': end_date.strftime('%Y-%m-%d') if end_date else None,
                'Active': active
            }
            addresses.append(address)
    return addresses

def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Generate and save customer data
num_customers = 10000
customers = generate_sample_customers(num_customers)
save_to_csv(customers, r'E:\code\PYTHON_TRAINING\files\csv_files\customers.csv')

# Generate and save customer address data
num_addresses = 3
addresses = generate_sample_addresses(customers, num_addresses)
save_to_csv(addresses, r'E:\code\PYTHON_TRAINING\files\csv_files\customer_addresses.csv')
