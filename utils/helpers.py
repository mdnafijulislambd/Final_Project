import time


# Generate a dynamic test user with unique timestamp-based credentials
# Used for avoiding duplication issues in repeated test executions
def generate_user():
    ts = int(time.time())
    username = f"user{ts}"
    email = f"user{ts}@gmail.com"
    return username, email


# Generate dynamic recruiter test data with unique timestamp-based values
# Used in recruiter registration and login flow testing
def generate_recruiter():
    ts = int(time.time())

    # Dynamic company name for uniqueness
    company = f"Company{ts}"

    # Dynamic recruiter email to avoid duplication
    email = f"recruiter{ts}@gmail.com"

    # Generated phone number (basic timestamp-based variation)
    phone = f"017{ts}"[-11:]

    # Default secure password for test consistency
    password = "12345678"

    return company, email, phone, password