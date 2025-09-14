from faker import Faker
import random
import json
from datetime import datetime, timedelta

fake = Faker()

def generate_customer():
    total_tx = random.randint(30, 2000)
    deposits = round(random.uniform(1000, 75000), 2)
    withdrawals = round(random.uniform(500, 60000), 2)
    balance = round(deposits - withdrawals + random.uniform(0, 50000), 2)
    avg_tx = round(random.uniform(20, 2000), 2)
    return {
        "CustomerID": fake.user_name() + str(random.randint(10, 999)),
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "Gender": random.choice(["Male", "Female"]),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "Age": random.randint(18, 75),
        "City": fake.city(),
        "Country": fake.country(),
        "CurrentBalance": balance,
        "Currency": random.choice(["USD","INR","EUR","GBP","AUD"]),
        "TotalTransactions": total_tx,
        "TotalDeposits": deposits,
        "TotalWithdrawals": withdrawals,
        "AverageTransactionAmount": avg_tx,
        "TotalCashback": round(random.uniform(0, 500), 2),
        "LastTransactionDate": fake.date_between(start_date='-60d', end_date='today').isoformat(),
        "PreferredContactMethod": random.choice(["Email", "Phone", "SMS"]),
        "AverageMonthlySpending": round(random.uniform(200, 20000), 2),
        "HighestTransactionAmount": round(random.uniform(100, 50000), 2),
        "LowestTransactionAmount": round(random.uniform(1, 50), 2),
        "TotalNumberOfAccounts": random.randint(1, 6),
        "AccountStatus": random.choice(["Active", "Dormant", "Closed"]),
        "RiskProfile": random.choice(["Low", "Medium", "High"]),
        "DepositStatus": random.choice(["Yes", "No"]),
    }

def generate_product(pid):
    categories = ["Home Loan", "Car Loan", "Personal Loan", "Credit Card", "Saving Account"]
    cat = random.choice(categories)
    return {
        "ProductID": pid,
        "ProductName": f"{cat} - {random.choice(['Standard','Premium','Flex'])}",
        "Category": cat,
        "InterestRate": round(random.uniform(3.5, 18.0), 2),
        "EligibilityCriteria": random.choice([
            "Min income 25k/month",
            "Min credit score 650",
            "Min 2 years job history",
            "No prior defaults"
        ]),
        "RiskLevel": random.choice(["Low","Medium","High"]),
        "Description": f"A {cat.lower()} product suitable for many customers. Offers flexible repayment."
    }

def create_dataset(n_customers=200, n_products=8, out_customers="customers.json", out_products="products.json"):
    customers = [generate_customer() for _ in range(n_customers)]
    products = [generate_product(i+1) for i in range(n_products)]
    with open(out_customers, "w") as f:
        json.dump(customers, f, indent=2)
    with open(out_products, "w") as f:
        json.dump(products, f, indent=2)
    print(f"Saved {len(customers)} customers to {out_customers}")
    print(f"Saved {len(products)} products to {out_products}")

if __name__ == "__main__":
    create_dataset()
