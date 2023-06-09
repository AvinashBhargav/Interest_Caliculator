def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))

# Calculating SI
simple_interest = calculate_simple_interest(principal, rate, time)
print("Simple Interest: ₹", round(simple_interest, 2))

# Calculating CI
compound_interest = calculate_compound_interest(principal, rate, time)
print("Compound Interest: ₹", round(compound_interest, 2))
