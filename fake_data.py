from faker import Faker
import random
import json

fake = Faker()

def generate_customer():
    return {
        "CustomerID": fake.user_name() + str(random.randint(10, 99)),
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "Gender": random.choice(["Male", "Female"]),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "Age": random.randint(18, 70),
        "City": fake.city(),
        "Country": fake.country(),
        "CurrentBalance": round(random.uniform(1000, 100000), 2),
        "Currency": "USD",
        "TotalTransactions": random.randint(50, 2000),
        "TotalDeposits": round(random.uniform(5000, 50000), 2),
        "TotalWithdrawals": round(random.uniform(5000, 50000), 2),
        "AverageTransactionAmount": round(random.uniform(50, 1000), 2),
        "TotalCashback": round(random.uniform(10, 500), 2),
        "LastTransactionDate": fake.date_this_year().isoformat(),
        "PreferredContactMethod": random.choice(["Email", "Phone", "SMS"]),
        "AverageMonthlySpending": round(random.uniform(500, 10000), 2),
        "HighestTransactionAmount": round(random.uniform(100, 20000), 2),
        "LowestTransactionAmount": round(random.uniform(1, 50), 2),
        "TotalNumberOfAccounts": random.randint(1, 5),
        "AccountStatus": random.choice(["Active", "Dormant", "Closed"]),
        "RiskProfile": random.choice(["Low", "Medium", "High"]),
        "DepositStatus": random.choice(["Yes", "No"])
    }

# Generate 3 fake customers
customers = [generate_customer() for _ in range(3)]

# Print as JSON
print(json.dumps(customers, indent=4))
