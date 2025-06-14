from faker import Faker
import random

fake = Faker()

SOURCE_CHANNELS = ["Demo Request", "LinkedIn", "Cold Email", "Referral", "Webinar", "Paid Ad"]
INDUSTRIES = ["SaaS", "E-commerce", "Healthcare", "Fintech", "EdTech", "Manufacturing"]
JOB_TITLES = ["CEO", "CTO", "Head of Marketing", "Product Manager", "Sales Manager","VP of Engineering", "Director of Operations", "Data Analyst"]

# Sample inquiry messages
INQUIRIES = [
    "We are looking for a platform to improve our user onboarding process.",
    "Interested in your solution. Can you share pricing details?",
    "Just exploring options, not planning to buy right now.",
    "Saw your demo on LinkedIn and would like to try it out.",
    "Need a scalable tool to support our sales team growth."
]

def generate_fake_lead():
    lead = {
        "name": fake.name(),
        "email": fake.email(),
        "company": fake.company(),
        "title": random.choice(JOB_TITLES),
        "inquiry": random.choice(INQUIRIES),
        "source": random.choice(SOURCE_CHANNELS),
        "industry": random.choice(INDUSTRIES),
        "location": fake.city(),
    }
    return lead

# Testing
if __name__ == "__main__":
    for _ in range(1):
        lead = generate_fake_lead()
        print(lead)
